#task 1

contacts = {"Anas":973950191,"Abdullah Mg":9867351290,"Aejaz":9563781290}
contacts["Siddique"]=9868757645
contacts["Aejaz"]=8657890910
print(contacts.get("Anas"))
print(contacts.get("Faisal","contact not found"))
for name,number in contacts.items():
    print(f"contact:{name} | phone: {number}")
    
#task 2

raw_logs = ["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]
unique_logs = set(raw_logs)
print(unique_logs)
print("ID05" in unique_logs)
print(f"{len(raw_logs)} vs {len(unique_logs)}")
print("Number of duplicates removed:",len(raw_logs)-len(unique_logs))

#task 3

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(friend_a | friend_b)
print(friend_a & friend_b)
print(friend_a - friend_b)
