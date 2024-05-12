import requests

def get_device_data():
    name = input("Enter the device name: ")
    device_type_id = input("Enter the device type ID (numeric): ")
    device_role_id = input("Enter the device role ID (numeric): ")
    site_id = input("Enter the site ID (numeric): ")
    status = input("Enter the device status (e.g., active, planned, offline): ")

    # Convert numeric inputs to integers
    try:
        device_type_id = int(device_type_id)
        device_role_id = int(device_role_id)
        site_id = int(site_id)
    except ValueError:
        print("Error: Device type, role, and site IDs must be numeric.")
        return

    return {
        "name": name,
        "device_type": device_type_id,
        "role": device_role_id,
        "site": site_id,
        "status": status
    }

def post_device_data(device_data):
    if device_data is None:
        return  # Exit if there was an error in data entry
    url = 'http://localhost:9040/add_device'
    response = requests.post(url, json=device_data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    device_data = get_device_data()
    post_device_data(device_data)
