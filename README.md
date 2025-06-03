# Privacy-Preserving Traffic Monitoring Using Machine Learning Analytics

## Overview
This project is a **Flask-based web application** that collects, processes, and visualizes real-time traffic data while ensuring privacy using **geo-indistinguishability** techniques. The system utilizes **OpenStreetMap (OSM)** with a heatmap for traffic visualization and applies **machine learning** to predict congestion patterns.

## Features
- **Real-time Traffic Data Collection**: Vehicles and Road-Side Units (RSUs) send traffic data.
- **Privacy-Preserving Mechanism**: Geo-indistinguishability ensures anonymity.
- **Machine Learning-Based Congestion Prediction**: Predicts traffic congestion levels.
- **Interactive Heatmap**: Displays traffic conditions using OpenStreetMap.
- **Flask API**: Backend handles data processing and ML model integration.

## Project Structure
```
Traffic-Monitoring-System/
│── app.py                # Main Flask application
│── ml_model.py           # Machine Learning module for congestion prediction
│── requirements.txt      # Dependencies
│── static/
│   ├── styles.css        # Styling for frontend
│── templates/
│   ├── index.html        # Frontend UI with OpenStreetMap heatmap
│── data/
│   ├── traffic_data.csv  # Sample traffic data
│── README.md             # Project documentation
```

## Installation
### Prerequisites
- Python 3.8+
- Pip
- Virtual environment (recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Traffic-Monitoring-System.git
   cd Traffic-Monitoring-System
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open **http://127.0.0.1:5000/** in your browser.

## Usage
- The homepage displays an **interactive heatmap** of traffic congestion.
- The heatmap updates with **real-time data** collected from the backend.
- The ML model predicts future congestion levels.

## Technologies Used
- **Backend**: Flask, Pandas
- **Frontend**: HTML, CSS, JavaScript (Leaflet.js, Leaflet.heat)
- **Machine Learning**: Scikit-learn
- **Data Visualization**: OpenStreetMap, Leaflet.js

## Future Enhancements
- Integration with **real-world traffic APIs** (Google Maps, HERE API).
- Implement **Blockchain** for secure traffic data exchange.
- Deploy on a cloud platform like **AWS or Heroku**.

## License
This project is licensed under the MIT License.

---
**Author**: Muhammed Yazeen S | 

