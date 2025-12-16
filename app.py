from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

# File where sensor readings are stored
READINGS_FILE = "readings.json1"

def load_readings():
    """Load all readings froom the JSONL file"""
    readings = []
    try:
        with open(READINGS_FILE, "r") as f:
            for line in f:
                if line.strip():
                    readings.append(json.loads(line))
    except FileNotFoundError:
        pass
    return readings

# ===== API ENDPOINTS =====

@app.route("/api/readings", methods=["GET"])
def get_readings():
    """Get all sensor readings"""
    readings = load_readings()
    return jsonify({
        "status": "success",
        "count": len(readings),
        "data": readings
    })

@app.route("/api/readings/latest", methods=["GET"])
def get_latest_reading():
    """Get the most recent sensor reading"""
    readings = load_readings()
    if not readings:
        return jsonify({
            "status": "error",
            "message": "No readings found"
        }), 404
    return jsonify({
        "status": "success",
        "data": readings[-1]
    })

@app.route("/api/readings", methods=["POST"])
def add_reading():
    """Add a new sensor reading (for future hardware integration)"""
    data = request.get_json()
    
    # Validate the reading has required fields
    if not data or "temperature" not in data or "pressure" not in data:
        return jsonify({
            "status": "error",
            "message": "temperature and pressure are required"
        }), 400
    
    # Add timestamp if not provided
    if "timestamp" not in data:
        data["timestamp"] = datetime.now().isoformat()
    
    # Append to file
    with open(READINGS_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
    
    return jsonify({
        "status": "success",
        "message": "Reading saved",
        "data": data
    }), 201

@app.route("/health", methods=["GET"])
def health():
    """Simple health check endpoint"""
    return jsonify({"status": "ok"})

# ===== ERROR HANDLERS =====

@app.errorhandler(404)
def not_found(error):
    return jsonify({"status": "error", "message": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == "__main__":
    print("Starting Flask API server...")
    print("Visit http://localhost:5000/api/readings in your browser")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host="0.0.0.0", port=5000)