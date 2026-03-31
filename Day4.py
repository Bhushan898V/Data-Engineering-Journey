site_info = {
    "Site ID" : "Mum- 04",
    "Location" : "Mumbai",
    "Type" : "Commercial",  
    "Active patient count" : 100,
    "pi name" : "Dr. Anjali Mehta",
}
print("\n--- Site Information ---")
for key, value in site_info.items():
    print(key + ":", value)

# A list with many duplicates
raw_logs = ["Admin", "User1", "Admin", "User2", "Admin", "User1"]

# Convert the list to a set
unique_users = set(raw_logs)

print("Original List:", raw_logs)
print("Unique Users (Set):", unique_users)