import requests
# Replace with the URL of the Node
node_url = input("input Url: ")
# Set a timeout value for the request (in seconds)
timeout = 5
# Make a request to the Node
try:
    response = requests.get(node_url, timeout=timeout)
    if response.status_code == 200:
        print(f"Node is available: {node_url}")
        print(f"Response time: {response.elapsed.total_seconds()} seconds")
        print(f"Server: {response.headers.get('Server')}")
        print(f"Content type: {response.headers.get('Content-Type')}")
        print(f"Content length: {response.headers.get('Content-Length')}")
    else:
        print(f"Unexpected status code: {response.status_code}")
except requests.exceptions.Timeout:
    print(f"Node is not available: {node_url} (timeout)")
except requests.exceptions.RequestException as e:
    print(f"Node is not available: {node_url} ({e})")
