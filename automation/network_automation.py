import json
import yaml

# Home Topology

with open("../configuration/home_topology/router1.json") as file:
    home_router1 = json.load(file)

with open("../configuration/home_topology/router2.json") as file:
    home_router2 = json.load(file)

with open("../configuration/home_topology/laptop1.json") as file:
    home_laptop1 = json.load(file)

with open("../configuration/home_topology/laptop2.json") as file:
    home_laptop2 = json.load(file)

with open("../configuration/home_topology/mobile1.json") as file:
    home_mobile1 = json.load(file)

with open("../configuration/home_topology/mobile2.json") as file:
    home_mobile2 = json.load(file)

with open("../configuration/home_topology/printer1.json") as file:
    home_printer1 = json.load(file)

with open("../configuration/home_topology/switch1.yaml") as file:
    home_switch1 = yaml.safe_load(file)

with open("../configuration/home_topology/switch2.yaml") as file:
    home_switch2 = yaml.safe_load(file)

# Office Topology

with open("../configuration/office_topology/laptop1.json") as file:
    office_laptop1 = json.load(file)

with open("../configuration/office_topology/laptop2.json") as file:
    office_laptop2 = json.load(file)

with open("../configuration/office_topology/mobile1.json") as file:
    office_mobile1 = json.load(file)

with open("../configuration/office_topology/mobile2.json") as file:
    office_mobile2 = json.load(file)

with open("../configuration/office_topology/pc1.json") as file:
    office_pc1 = json.load(file)

with open("../configuration/office_topology/pc2.json") as file:
    office_pc2 = json.load(file)

with open("../configuration/office_topology/printer1.json") as file:
    office_printer1 = json.load(file)

with open("../configuration/office_topology/printer2.json") as file:
    office_printer2 = json.load(file)

with open("../configuration/office_topology/router1.json") as file:
    office_router1 = json.load(file)

with open("../configuration/office_topology/router2.json") as file:
    office_router2 = json.load(file)

with open("../configuration/office_topology/router3.json") as file:
    office_router3 = json.load(file)

with open("../configuration/office_topology/router4.json") as file:
    office_router4 = json.load(file)

with open("../configuration/office_topology/switch1.yaml") as file:
    office_switch1 = yaml.safe_load(file)

with open("../configuration/office_topology/switch2.yaml") as file:
    office_switch2 = yaml.safe_load(file)

# Cloud

with open("../configuration/cloud/servers/api_server.json") as file:
    api_server = json.load(file)

with open("../configuration/cloud/servers/authentication_server.json") as file:
    authentication_server = json.load(file)

with open("../configuration/cloud/servers/database_server.json") as file:
    database_server = json.load(file)

routers = [
    home_router1, 
    home_router2
   ]

laptops = [
    home_laptop1, 
    home_laptop2
  ]

mobiles = [
    home_mobile1, 
    home_mobile2
  ]

printers = [
    home_printer1
]

switches = [
    home_switch1,
    home_switch2
]

servers = [
    api_server,
    authentication_server,
    database_server
]

office_routers = [
    office_router1,
    office_router2,
    office_router3,
    office_router4
]


office_switches = [
    office_switch1,
    office_switch2
]


office_laptops = [
    office_laptop1,
    office_laptop2
]


office_pcs = [
    office_pc1,
    office_pc2
]


office_mobiles = [
    office_mobile1,
    office_mobile2
]


office_printers = [
    office_printer1
]

home_devices = (
    routers +
    switches +
    laptops +
    mobiles +
    printers
)


office_devices = (
    office_routers +
    office_switches +
    office_laptops +
    office_pcs +
    office_mobiles +
    office_printers
)


devices = (
    routers +
    switches +
    laptops +
    mobiles +
    printers +
    office_routers +
    office_switches +
    office_laptops +
    office_pcs +
    office_mobiles +
    office_printers +
    servers
)

print("\n ALL NETWORK DEVICES")
print("======================")

for device in devices:
    print("----------------------")
    print("Hostname:", device["hostname"])

    if "vendor" in device:
        print("Vendor:", device["vendor"])

    if "role" in device:
        print("Role:", device["role"])

    if "ip_address" in device:
        print("IP Address:", device["ip_address"])

    if "management_ip" in device:
        print("Management IP:", device["management_ip"])

    if "device_type" in device:
        print("Device Type:", device["device_type"])