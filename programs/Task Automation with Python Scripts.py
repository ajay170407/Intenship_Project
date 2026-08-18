emails = (r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

file=open("emails.txt","w")
for email in emails:
    file.write(email)

file = open("emails.txt","r")
file.read()

print("Email addresses extracted successfully!")
print("Total Emails Found:", len(emails))
