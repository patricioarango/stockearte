from zeep import Client

# URL of the WSDL (Replace with your actual WSDL URL)
wsdl = 'http://localhost:8080/wsu/users.wsdl'

# Create a client to interact with the SOAP service
client = Client(wsdl=wsdl)

# Prepare the request data for adding a user
new_user_data = {
    'name': 'John',
    'lastname': 'Doe',
    'username': 'johndoe12345',
    'password': 'securepassword',
    'storeCode': 'tienda1'
}

# Call the addUser operation
response = client.service.addUser(user=new_user_data)

print(f"Status: {response.status}")

if hasattr(response, 'user') and response.user:
    print(f"User added: {response.user.id_user} - {response.user.username}")
else:
    print("No user data returned")
