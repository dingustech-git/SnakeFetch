import platform
print("SnakeFetch")
print(" ")
osName = platform.system()
osVersion = platform.release()
if osName == "Windows":
    print(f"OS: Windows {osVersion}")
else:
    print(f"OS: {osName}")
    print(osVersion)
cpuModel = platform.processor()
print(f"CPU: {cpuModel}")
cpuArch = platform.machine()
print(f"CPU Architecture: {cpuArch}")
pythonVersion = platform.python_version()
print(f"Python Version: {pythonVersion}")
if osName == "Linux":
    with open("/etc/os-release") as f:
        for line in f:
            if line.startswith("PRETTY_NAME"):
                name = line.split("=")[1].strip().strip('"')
                print(f"Distro: {name}")
print(" ")
input("Press enter to quit...")