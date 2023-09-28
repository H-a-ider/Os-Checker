import psutil

print("""Available Information is about:
        (1) disks
        (2) memory 
        (3) network
        (4) battery
        (5) users
        """)
entry = input("Want to know information about:\n ")

if entry=="memory":
    memory = psutil.virtual_memory()
    print(memory)
if entry=="disks":
    disk = psutil.disk_partitions()
    print(disk)
if entry=="network":
    network = psutil.net_if_addrs()
    print(network)
if entry=="battery":
    battery = psutil.sensors_battery()
    print(battery)
if entry=="users":
    users = psutil.users()
    print(users)
