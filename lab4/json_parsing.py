import sample_data
for item in sample_data.data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    print(attributes["dn"], attributes["descr"], attributes["speed"], attributes["mtu"])