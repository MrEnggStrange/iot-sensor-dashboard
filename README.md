# IoT Sensor Dashboard

A Python-based sensor data logger and dashboard for embedded systems.

## Features
- Simulates sensor readings (temperature, pressure, timestamp)
- Logs data in JSON Lines format (JSONL)
- Real-time terminal output
- Persistent file storage

## Project Structure
iot-sensor-dashboard/
├── sensor_reader.py # Main script that generates sensor readings
├── readings.jsonl # Log file with sensor data (gitignored)
├── README.md # This file
├── .gitignore # Files to ignore in version control
## How to Run


The script will:
1. Generate sensor readings every 2 seconds
2. Print them nicely to the terminal (JSON format)
3. Save them to `readings.jsonl` for later analysis

## Next Steps
- [ ] Add Flask web server
- [ ] Build REST API endpoints
- [ ] Create database for persistent storage
- [ ] Build frontend dashboard
- [ ] Deploy to production

## Technology Stack
- **Language**: Python 3
- **Data Format**: JSON Lines (JSONL)
