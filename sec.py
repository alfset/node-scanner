import requests
node_url = input("input Url : ")
timeout = 5
# Check if the node is using HTTPS
if not node_url.startswith('https://'):
    print("Node is not using HTTPS")
else:
    print("Node is using HTTPS")
# Check the web server being used
response = requests.get(node_url, timeout=timeout)
server_header = response.headers.get('Server')
if server_header is None:
    print("Server header not found")
else:
    print(f"Server: {server_header}")
    if 'nginx' in server_header.lower():
        print("Node is using Nginx web server, which has a good reputation for security")
    elif 'apache' in server_header.lower():
        print("Node is using Apache web server")
    else:
        print(f"Node is using {server_header} web server")
