from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_url = "https://bsby.siglab.co.id/api/test-programmer"
    email = "goldenseriousemail@gmail.com"
    
    # Make a GET request to the API
    response = requests.get(api_url, params={'email': email})
    if response.status_code == 200:
        json_data = response.json()

        # check results key
        if 'results' in json_data and isinstance(json_data['results'], list):
            data = json_data['results']

            # Convert the 'type' field to string title
            for item in data:
                item['type'] = get_type_title(item.get('type'))
                
            return render_template('table.html',data = data)
        else:
            return {'error': "Malformed response from the API"}

    else:
        return {'error': f"Failed to fetch data from the API. Status code: {response.status_code}"}

    


@app.route('/data', methods=['GET'])
def grid_data():
  # Fetch data from the API using the provided link
    api_url = "https://bsby.siglab.co.id/api/test-programmer"
    email = "goldenseriousemail@gmail.com"
    
    # Make a GET request to the API
    response = requests.get(api_url, params={'email': email})
    if response.status_code == 200:
        json_data = response.json()

        # check results key
        if 'results' in json_data and isinstance(json_data['results'], list):
            data = json_data['results']

            # Convert the 'type' field to string title
            for item in data:
                item['type'] = get_type_title(item.get('type'))
                
            return {'data': data}
        else:
            return {'error': "Malformed response from the API"}

    else:
        return {'error': f"Failed to fetch data from the API. Status code: {response.status_code}"}

# Fun for Int Type to Str Type
def get_type_title(type_id):
    type_mapping = {
        1: "Food & Beverage",
        2: "Pharmaceuticals",
        3: "Government",
        4: "Traditional Medicine & Supplement",
        13: "Beauty, Cosmetics & Personal Care",
        14: "Media RTU",
        15: "K3L Products",
        16: "ALKES & PKRT",
        17: "FEED, Pesticides & PSAT",
        18: "Others L",
        19: "Research / Academic Purpose",
        20: "Dioxine Udara"
        # This is manual mapping, better if have access to type in DB
    }

    # Check if 'type_id' is already a string title
    if isinstance(type_id, str):
        return type_id

    return type_mapping.get(type_id, f"Unknown Type ({type_id})")

if __name__ == '__main__':
    app.run()