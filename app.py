from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('AVIATIONSTACK_API_URL')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/track-flights', methods=['POST'])
def track_flights():
    user_input = request.form.get('arrival_airport').lower()
    
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        flights = data.get('data', [])

        filtered_flights = []

        for flight in flights:
            if user_input in flight['arrival']['airport'].lower():
                filtered_flights.append({
                    'departure': flight['departure']['airport'],
                    'arrival': flight['arrival']['airport']
                    })
        
        if not filtered_flights:
            return render_template('results.html', error=f"No flights found arriving at: {user_input}")
        else:
            return render_template('results.html', flights=filtered_flights)

    else:
        return "Failed to retrieve flight data", 500


if __name__ == '__main__':
    app.run(debug=True)


