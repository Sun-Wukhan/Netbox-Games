import requests

def get_site_data():
    # Gather site details from the user
    name = input("Enter the site name: ")
    slug = input("Enter the site slug (use hyphens and lowercase letters): ")
    status = input("Enter the site status (e.g., active, planned): ")
    description = input("Enter the site description: ")

    return {
        "name": name,
        "slug": slug,
        "status": status,
        "description": description
    }

def post_site_data(site_data):
    # URL of the Flask application's add_site endpoint
    url = 'http://localhost:9040/add_site'
    
    # Making the POST request to the Flask app
    response = requests.post(url, json=site_data)
    
    # Printing the response from the server
    # print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    site_data = get_site_data()
    post_site_data(site_data)
