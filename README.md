# lab-02-weektwo-augustine-normanyo

# 🗳️ CLI Survey App

A command-line survey simulation tool for conducting simple user surveys, built using **Python**.  
Designed to demonstrate input validation, modular code structure, and the use of built-in libraries like `random`, `datetime`, and `os`.

---

## 📌 Features

- ✅ Greets the user
- 🎲 Randomly selects a survey question
- ✅ Validates user responses
- 🕓 Timestamps each response
- 📦 Modular and reusable code structure

---

## 🗂️ Project Structure

survey_app/
├── main.py # Main entry point for the app
├── survey/ # Core app modules
│ ├── init.py # Makes the folder a package
│ ├── greeter.py # Handles greeting logic
│ ├── question.py # Selects and returns survey questions
│ ├── validator.py # Validates user input
│ └── recorder.py # Records responses with timestamp

python main.py
