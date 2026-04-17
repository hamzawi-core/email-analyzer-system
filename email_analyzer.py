# =========================
# Email Analyzer System
# =========================

total_emails = 0
usernames = []
domains = []
emails = []

print("Email Analyzer System")
print("----------------------")

# 🔹 Input loop
while True:
    email_input = input("Enter the email or type 'done' to stop: ")

    # Clean input (remove spaces + convert to lowercase)
    clean_email = email_input.strip().lower()

    # Skip empty input
    if not clean_email:
        continue

    # Stop condition
    if clean_email == "done":
        break

    if clean_email in emails:
        print("Email already entered, skipping.")
        continue
        
    #skipping emails with spaces in between
    if " " in clean_email:
        print("Invalid email: contains spaces")
        continue

    # Validate email format
    if "@" not in clean_email:
        print("Invalid email")
        continue

    # Find position of '@' symbol
    at_position = clean_email.find("@")

    # Validate domain format (must contain a dot)
    if "." not in clean_email[at_position + 1:]:
        print("Invalid email")
        continue

    emails.append(clean_email)

    # Extract username
    usernames.append(clean_email[:at_position])

    # Extract domain
    domain = clean_email[at_position + 1:]

    domains.append(domain)

unique_domains = []

for domain in domains:
    if domain not in unique_domains:
        unique_domains.append(domain)

# Sort domains alphabetically
unique_domains.sort()

longest_username = ""
for i in usernames:
    if len(i)>len(longest_username) or longest_username == "":
        longest_username = i

shortest_username = ""
for i in usernames:
    if len(i)<len(shortest_username) or shortest_username == "":
        shortest_username = i

most_used_domain = ""
most_used_count = 0

for current_domain in unique_domains:
    occurrence_count = 0

    # Count how many times this domain appears
    for d in domains:
        if d == current_domain:
            occurrence_count += 1

    # Update most used domain
    if occurrence_count > most_used_count:
        most_used_domain = current_domain
        most_used_count = occurrence_count

    # Print occurrences
    print(f"The repetition number of {current_domain} is {occurrence_count}")

# Print most used domain
print(f"The most used domain is {most_used_domain} with {most_used_count} times")

# =========================
# (Average emails per domain)
# =========================

if unique_domains:
    average_emails_per_domain = len(domains) / len(unique_domains)
    print(f"Average emails per domain: {average_emails_per_domain:.2f}")

# =========================
# Output Section
# =========================

# Print usernames (each on a new line)
print("\nUsernames:")
for name in usernames:
    print(name)

# Print domains (uppercase)
print("\nDomains:")
for domain in unique_domains:
    print(domain.upper())

# Print total emails
print("\nTotal emails:")
print(len(usernames))

# Challenge 1: Print usernames in one line
print(",".join(usernames))

# Printing the longest and the shortest username
print(f"Longest username: {longest_username}")
print(f"Shortest username: {shortest_username}")