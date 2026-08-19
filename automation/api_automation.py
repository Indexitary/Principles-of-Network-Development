import requests
import json

BASE_URL = "http://127.0.0.1:5000"


# Devices

response = requests.get(
    f"{BASE_URL}/home/devices"
)

devices = response.json()
print("=== Home Devices ===")
for device in devices:
    print(device)

# Router

print("=== Home Router ====")
response = requests.get(
    f"{BASE_URL}/home/routers/R1"
)
print(response.json())

# Laptop

print("==== Home Laptop ===")
response = requests.get(
    f"{BASE_URL}/home/laptops/HL1"
)

print(response.json())

# Cloud Servers

print("=== Cloud Server ===")
response = requests.get(
    f"{BASE_URL}/cloud/servers/API-SERVER"
)

print(response.json())



# Create New Device

new_device = {
    "hostname": "R5",
    "vendor": "Cisco",
    "ip_address": "192.168.1.5",
    "role": "Backup Router"
}

response = requests.post(
    f"{BASE_URL}/devices",
    json=new_device
)

print("=== POST Result ===")
print(response.json())



# Updated Device

updated_device = {
    "vendor":"Cisco Systems"
}

response = requests.put(
    f"{BASE_URL}/devices/R5",
    json=updated_device
)

print("=== PUT Result ===")
print(response.json())



# Delete Device

response = requests.delete(
    f"{BASE_URL}/devices/R5"
)

print("=== DELETE Result ===")
print(response.json())



# Endpoint List

endpoints = [
    "/home/routers",
    "/home/switches",
    "/home/laptops",
    "/office/devices",
    "cloud/servers"
]

for endpoint in endpoints:
    response = requests.get(
        BASE_URL + endpoint
    )
    print(endpoint)
    print(response.json())
    print("-------------------")