 # welcome to simple profile builder with python
# fist asl user to enter his personal information
name = input("enter your name : ")
email = input("enter your email : ")
phone_number = input("enter your phone number : ")
bio = input("enter a simple idea about you : ")
skills = input("enter your skills : ")
# save info in tuple 
personal_info = (name , email , phone_number , bio)
print("Simple profile builder")
print("-"*60)
print("-"*60)
# foramat  the name 
name.strip()
name.title()
# format the skiils
list_of_skills = skills.split()
list_of_skills.append("personal pranding")
list_of_skills.remove(list_of_skills[1])
# print the onformation that user entered
print(f"Name : {personal_info[0]} \nSkills : {list_of_skills} \nPhone number : {personal_info[2]} ")
print(f"Email : {personal_info[1]} \nBio : {personal_info[3]} ")
print("-"*60)
print("-"*60)
# end of project