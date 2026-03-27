# Day 3: Loops for IT Automation

print("--- Phase 1: Equipment Relocation ---")
# FOR LOOP: Iterating through a specific list of items
equipment_list = ["Router-01", "Core-Switch-A", "Server-Rack-2"]

for item in equipment_list:
    print("Logged: Moving", item, "from Thane to Andheri office.")

print("\n--- Phase 2: Network Reconnection ---")
# WHILE LOOP: Running until a condition is met
connection_attempts = 0
is_connected = False

while connection_attempts < 3 and is_connected == False:
    connection_attempts = connection_attempts + 1
    print("Attempt", connection_attempts, "- Pinging Andheri network gateway...")
    
    # Simulating a successful connection on the final attempt
    if connection_attempts == 3:
        is_connected = True
        print("Success! Gateway is online and stable.")