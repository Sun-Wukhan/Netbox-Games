import requests

def get_manufacturer_data():
    # Gather manufacturer details from the user
    name = input("Enter the manufacturer name: ")
    slug = input("Enter the manufacturer slug (use hyphens and lowercase letters): ")
    description = input("Enter the manufacturer description (optional): ")
    return {
        "name": name,
        "slug": slug,
        "description": description
    }

def post_manufacturer_data(manufacturer_data):
    # URL of the Flask application's add_manufacturer endpoint
    url = 'http://localhost:9040/add_manufacturer'
    
    # Making the POST request to the Flask app
    response = requests.post(url, json=manufacturer_data)
    
    # Printing the response from the server
    # print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    manufacturer_data = get_manufacturer_data()
    post_manufacturer_data(manufacturer_data)
