# Student Score total_marks 
print("=== Student Score Calculator ===")
print("Hello! This program will calculate your total, minimum, maximum, and average scores.")
user_dict ={
    "name":"",
    "age":0,
    "marks":[]
}
total_subject=0
total_marks  = 0
name = input("Enter Your Name : ")
user_dict["name"]=name
try:
    age=int(input("Enter Your Age : "))
    user_dict["age"]=age
    total_subject = int(input("Enter Your Number of subjects : "))
    for i in range(total_subject):
         mark = int(input(f"Enter Your Mark for subject No {i+1} : "))
         user_dict["marks"].append(mark)
         total_marks  = total_marks  + mark
    
except(ValueError):
        print("Please Enter a Valid input. ")
except Exception as e:
    print("Something went wrong:", e)
print("\n--- Summary ---")
print(f"Name: {user_dict['name']}")
print(f"Age: {user_dict['age']}")
print("Marks:", ", ".join(map(str, user_dict["marks"])))
print("Maximum Score:", max(user_dict["marks"]))
print("Minimum Score:", min(user_dict["marks"]))
print("Total Score:", total_marks)
print(f"Average Score: {total_marks / total_subject:.2f}" if total_subject > 0 else "Average Score: 0")
