# Delima, Sheena Mae D.
# BSCPE 1-2
# March 23, 2024

# -----------------------------------------------------------------------------

# ========= PSEUDO CODE =========
# || LIBRARIES/PACKAGES ||
import json


# || VARIABLES || 
ask_user_name = input("Enter your name: ")
ask_dream_job = input("What is your dream job?: ")
ask_passion = input("What is your passion?: ")
ask_skills = input("What are your skills: ")
ask_idol_in_coding = input("Who is your professional idol in coding?: ")


# || ACTUAL CODE ||
# - Data
users_data = {
    "Name" : ask_user_name,
    "Dream Job" : ask_dream_job,
    "Passion" : ask_passion,
    "Skills" : ask_skills,
    "Professional Idol in Coding" : ask_idol_in_coding
}

# - Printing the data in json 
data = json.dumps(users_data, indent=2)

print(data)

# - Code for creating a json file 
with open('users_data.json', 'w') as file:
    file.write(data)