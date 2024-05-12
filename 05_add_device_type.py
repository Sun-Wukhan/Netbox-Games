import requests

def get_device_type_data():
    model = input("Enter the device type model (e.g., X500): ")
    while not model:  # Ensure model is provided
        print("Model is required and cannot be empty.")
        model = input("Enter the device type model (e.g., X500): ")

    manufacturer = input("Enter the manufacturer name: ")
    while not manufacturer:  # Ensure manufacturer name is provided
        print("Manufacturer name is required and cannot be empty.")
        manufacturer = input("Enter the manufacturer name: ")

    slug = model.lower().replace(' ', '-')  # Automatically generate a slug from the model

    return {
        "model": model,
        "manufacturer": manufacturer,  # Send as a string as specified
        "slug": slug  # Use a simple slug generation rule
    }

def post_device_type_data(device_type_data):
    url = 'http://localhost:9040/add_device_type'
    response = requests.post(url, json=device_type_data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    device_type_data = get_device_type_data()
    post_device_type_data(device_type_data)
