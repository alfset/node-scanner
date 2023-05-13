import time
import requests
# Define the base URL of the node
base_url = input("input URL: ")
# Define the endpoint to test the scalability
endpoint = "/api/v1/blocks"
# Define the number of requests to make
num_requests = 1000
# Make the requests and measure the time taken
start_time = time.time()
for i in range(num_requests):
    url = base_url + endpoint
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        break
end_time = time.time()
# Calculate the time taken per request
total_time = end_time - start_time
time_per_request = total_time / num_requests
print(f"Total time taken: {total_time:.4f} seconds")
print(f"Time per request: {time_per_request:.4f} seconds")
