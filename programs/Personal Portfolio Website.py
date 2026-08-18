# Personal Portfolio Program

email=input("enter the gmail:")
for i in email:
    if i in ('ajay@gmail.com'):
        password=input("enter the password:")
        if password in ('anter@1178'):
            print("=" * 50)
            print("        PERSONAL PORTFOLIO")
            print("=" * 50)

            name = input("enter the name:")
            role = "Python Developer"
            phone = int(input("enter the phone number:"))

            about = """ 
            I am a passionate Python programmer interested in
            Data Science, Web Development, UI/UX Design,
            and Full Stack Development.
            """
            
            skills = ["Python", "HTML", "CSS", "JavaScript", "SQL", "Flask"]

            projects = ["Portfolio Website", "Student Management System", "Recipe Data Analysis", "Task Automation"]

            print("\nName :", name)
            print("Role :", role)

            print("\nABOUT ME")
            print("-" * 30)
            print(about)

            print("SKILLS")
            print("-" * 30)
            for skill in skills:
                print("•", skill)

            print("\nPROJECTS")
            print("-" * 30)
            for project in projects:
                    print("•", project)

            print("\nCONTACT")
            print("-" * 30)
            print("Email :", email)
            print("Phone :", phone)

            print("\nThank you for visiting my portfolio!")
            break
