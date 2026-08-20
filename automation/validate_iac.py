import yaml

with open("../infrastructure/network_infrastructure.yaml") as file:
    infrastructure = yaml.safe_load(file)

print("Infrastructure Name:")
print(infrastructure["network"]["name"])

print("----------------------------")
print("Routers:")

for router in infrastructure["devices"]["routers"]:
    print(router["hostname"])
    print(router["ip_address"])

print("----------------------------")
print("Servers:")


# for server in infrastructure["servers"]:
#     print(server["hostname"])
#     print(server["role"])