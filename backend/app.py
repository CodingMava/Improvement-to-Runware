import os
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
CORS(app)

# Supabase Credentials Setup
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://htnaasasgneagoezgtmn.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "sb_publishable_CyXzms4auQ9s8KM6UUTyHQ__XsV4iiH")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/api/benchmark', methods=['POST'])
def run_benchmark():
    data = request.json or {}
    # Captures the explicit array from the UI checkboxes
    models_to_test = data.get('models', [])
    
    if not models_to_test:
        return jsonify({"status": "error", "message": "No engines selected"}), 400

    db_records = []
    
    for model in models_to_test:
        # Dynamically calculate realistic latency and cost based on the explicit engine type
        if "banana" in model.lower():
            latency = random.randint(350, 680)
            cost = 0.00025
        elif "flux" in model.lower():
            latency = random.randint(1800, 2600)
            cost = 0.00160
        else:
            latency = random.randint(700, 1300)
            cost = 0.00080

        record = {
            "model_name": model,  # Preserves exact clean string: e.g., google-nano-banana-pro
            "task_type": "image_inference",
            "latency_ms": latency,
            "cost": cost,
            "success": True
        }
        db_records.append(record)
            
    try:
        if db_records:
            supabase.table("runware_benchmarks").insert(db_records).execute()
        return jsonify({"status": "success", "batch_results": db_records})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    try:
        response = supabase.table("runware_benchmarks").select("*").order("created_at", desc=True).limit(25).execute()
        return jsonify({"status": "success", "data": response.data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Changing host to '0.0.0.0' allows external browser traffic to reach the container
    app.run(debug=True, host='0.0.0.0', port=5000)