import zeep

# URL of the WSDL (Replace with your actual WSDL URL)
wsdl = 'http://localhost:8080/ws/countries.wsdl'

# Create a client to interact with the SOAP service
client = zeep.Client(wsdl=wsdl)

# Print available operations (optional, to see what methods are available)
print(client.service)

# Call the getCountry method (assuming your service has a 'getCountry' method)
# 'Spain' is the example country from your SOAP response
response = client.service.getCountry('Spain')

# Print the response (which should match the XML example you provided)
print(response)
