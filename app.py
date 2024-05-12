from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

NETBOX_API_URL = "http://worker01:8000/api/"
API_TOKEN = "6c429a73f6008cecd7074cab036a85ee0eb01385"

@app.route('/', methods=['GET'])
def home():
    print("Home endpoint was accessed")
    return "Welcome to NetBox API!"

@app.route('/add_site', methods=['POST'])
def add_site():
    site_data = request.get_json()
    print("Received data for new site:", site_data)
    response = make_netbox_request("POST", "dcim/sites/", data=site_data)
    # Check if response is an error message dictionary
    if 'error' in response:
        return jsonify(response), 400
    return jsonify(response), response.get('status_code', 200)


@app.route('/add_device_role', methods=['POST'])
def add_device_role():
    role_data = request.get_json()
    print("Received data for new device role:", role_data)
    response = make_netbox_request("POST", "dcim/device-roles/", data=role_data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify(response), response.get('status_code', 200)

@app.route('/add_manufacturer', methods=['POST'])
def add_manufacturer():
    manufacturer_data = request.get_json()
    print("Received data for new manufacturer:", manufacturer_data)
    response = make_netbox_request("POST", "dcim/manufacturers/", data=manufacturer_data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify(response), response.get('status_code', 200)

@app.route('/add_module_type', methods=['POST'])
def add_module_type():
    data = request.get_json()
    print("Received data for new module type:", data)
    response = make_netbox_request("POST", "dcim/module-types/", data=data)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify(response), response.get('status_code', 200)

@app.route('/add_device_type', methods=['POST'])
def add_device_type():
    device_type_data = request.get_json()
    print("Received data for new device type:", device_type_data)
    response = make_netbox_request("POST", "dcim/device-types/", data=device_type_data)
    if 'error' in response or response.get('status_code', 200) != 200:
        return jsonify(response), response.get('status_code', 400)
    return jsonify(response), 200

@app.route('/add_device', methods=['POST'])
def add_device():
    device_data = request.get_json()
    print("Received data for new device:", device_data)
    response = make_netbox_request("POST", "dcim/devices/", data=device_data)
    if 'error' in response or response.get('status_code', 200) != 200:
        return jsonify(response), response.get('status_code', 400)
    return jsonify(response), 200

def make_netbox_request(method, path, data=None):
    url = NETBOX_API_URL + path
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {API_TOKEN}"
    }
    print(f"Making a {method} request to {url} with data: {data}")
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            print(f"API Error Response: {response.text}")
            return {'error': response.text, 'status_code': response.status_code}
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {'error': str(e), 'status_code': 500}



if __name__ == '__main__':
    print("Starting Flask development server...")
    app.run(debug=True, port=9040)
