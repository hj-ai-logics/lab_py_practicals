# Constant system logging profile
logging_profile = ("192.168.1.10", 8080)

# Unpacking the tuple
ip_address, server_port = logging_profile

print("IP Address:", ip_address)
print("Server Port:", server_port)

# Attempt to modify the tuple
try:
    logging_profile[0] = "192.168.1.20"
except TypeError:
    print("Error: Logging profile cannot be modified.")
