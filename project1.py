name=input("enter your name:")
age=int(input("enter your age:"))
city=input("enter your city:")
course=input("enter your course:")

name=name.strip().title()
city=city.strip().title()
course=course.strip().upper()

print()
print("Student Information")
print("------------")
print(f"name:{name}")
print(f"age:{age}")
print(f"city:{city}")
print(f"course:{course}")

skills=["python","C","SQL","Git"]

print()
print(f"initial skills:{skills}")

skills.append("GenAI")
skills.append("promt engineering")

print("Updated skills:",skills)
print("First skill:",skills[0])
print("Last skill:",skills[-1])

academic_location=(city,course)
print()
print("Academic Location:",academic_location)
print("City:",academic_location[0])
print("course:",academic_location[1])

skills_with_duplicate=["python","SQL","python","Git","GenAI","SQL"]
unique_skills=set(skills_with_duplicate)
print()
print("skills entered:",skills_with_duplicate)
print("unique_skills:",unique_skills)

print("know python:","python" in unique_skills)
print("know java:","java" in unique_skills)

student={"name":name,"age":age,"city":city,"course":course,"skills":skills}
print()
print("Student Dictionary:",student)
print("student_name:",student["name"])
print("student_course:",student["course"])
student["level"]="Beginner" 
student["age"]=age+1
print()
print("updated_student:",student)
print()
print ("collection summary")
print("-----------")
print(f"no. of skills in the list:{len(skills)} ")
print(f"no. of unique skills:{len(unique_skills)}")
print(f"python is in the skills list:{'python'in skills}")
print(f"java is in the skills list:{'java' in skills}")
print()
profile_summary=(f"{name} is {age} years old and live in {city}.")
print()
print("PROFILE SUMMARY")
print("------------")
print("profile_summary")
print()
print("=================================")
print("       STUDENT PROFILE")
print("=================================")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"City: {student['city']}")
print(f"Course: {student['course']}")
print(f"Level: {student['level']}")
print(f"Skills: {student['skills']}")
print(f"Unique: {unique_skills}")
print("=================================")