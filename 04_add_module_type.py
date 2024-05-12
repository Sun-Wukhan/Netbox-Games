import requests

def get_module_type_data():
    model = input("Enter the model for the module type: ")
    manufacturer = input("Enter the manufacturer for the module type: ")

    # Construct the data dictionary with only required fields
    module_type_data = {
        "model": model,
        "manufacturer": manufacturer  # Assuming manufacturer's name or ID as required
    }
    return module_type_data

def post_module_type_data(module_type_data):
    url = 'http://localhost:9040/add_module_type'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=module_type_data, headers=headers)
    # print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    module_type_data = get_module_type_data()
    post_module_type_data(module_type_data)
