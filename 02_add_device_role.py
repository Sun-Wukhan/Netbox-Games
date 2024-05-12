import requests

def get_device_role_data():
    # Gather device role details from the user
    name = input("Enter the device role name: ")
    slug = input("Enter the device role slug (use hyphens and lowercase letters): ")
    description = input("Enter the device role description: ")
    return {
        "name": name,
        "slug": slug,
        "description": description
    }

def post_device_role_data(role_data):
    # URL of the Flask application's add_device_role endpoint
    url = 'http://localhost:9040/add_device_role'
    
    # Making the POST request to the Flask app
    response = requests.post(url, json=role_data)
    
    # Printing the response from the server
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    role_data = get_device_role_data()
    post_device_role_data(role_data)
