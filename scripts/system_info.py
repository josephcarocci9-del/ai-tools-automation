import platform

def system_info():
    print("System:", platform.system())
    print("Node:", platform.node())
    print("Release:", platform.release())
    print("Version:", platform.version())

if __name__ == "__main__":
    system_info()
