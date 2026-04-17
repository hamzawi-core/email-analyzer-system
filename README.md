# 📧 Email Analyzer System

## 📌 Description

This is a simple Python program that analyzes email addresses entered by the user.
It extracts useful information such as usernames and domains, and provides statistics about them.

---

## ⚙️ Features

* ✅ Accepts multiple email inputs from the user
* ✅ Cleans and normalizes input (removes spaces, converts to lowercase)
* ✅ Validates email format (must contain `@` and a valid domain)
* ✅ Prevents duplicate email entries
* ✅ Extracts:

  * Username (before `@`)
  * Domain (after `@`)
* ✅ Displays all usernames
* ✅ Displays unique domains (sorted alphabetically)
* ✅ Counts how many times each domain appears
* ✅ Finds the most used domain
* ✅ Calculates average emails per domain
* ✅ Finds:

  * Longest username
  * Shortest username

---

## 🧠 How It Works

1. The user enters emails one by one
2. The program validates each email
3. Valid emails are stored and processed
4. The program analyzes the data and prints results

---

## ▶️ How to Run

1. Make sure you have Python installed
2. Run the program:

```bash
python email_analyzer.py
```

3. Enter emails when prompted
4. Type `done` to finish input

---

## 📊 Example Output

```
Usernames:
hamza
mohammed

Domains:
GMAIL.COM
YAHOO.COM

Total emails:
2
```

---

## 🚀 Future Improvements

* Store emails using tuples instead of separate lists
* Improve email validation (more strict rules)
* Save results to a file
* Add a graphical interface (GUI)

---

## 👨‍💻 Author

Developed by Hamza
Computer Science student 🚀
