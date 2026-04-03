counter = 0
username = []
domains = []
print("Email Analyzer System")
print("----------------------")
while True:
    email = input("enter the email or enter done to stop")
    
    clean_email = email.strip()
    clean_email = clean_email.lower()

    if clean_email == "":
        continue

    if clean_email == "done":
        break
    
    if "@" not in clean_email:
        print("invalid email")
        continue
    
    counter+=1

    atpos = clean_email.find("@")

    username.append(clean_email[:atpos])

    space_after_domain = clean_email.find(" ",atpos+1)
    if space_after_domain == -1:
        domain = clean_email[atpos+1:]
    else:
        domain = clean_email[atpos+1:space_after_domain]
    
    domains.append(domain)
print("\nusernames:")
for i in username:
    print(i)
print("\ndomains:")
for i in domains:
    print(i.upper())
print("\nTotal emails:")
print(counter) 