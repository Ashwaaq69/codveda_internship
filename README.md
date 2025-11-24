# Codveda Internship – Task 1 (Simple Calculator)

This project is part of the Codveda Technology Python Development Internship.
The calculator performs basic operations:

- Addition
- Subtraction
- Multiplication
- Division (with division-by-zero handling)
 
This repository contains small Python exercises for the internship. Each task is in its own folder with a short script you can run with Python.

## Task 2 — Number Guessing

- **File:** `Task2NumberGuessing/NumberGuessing.py`
- **Description:** A simple interactive game where the program chooses a random number and the user tries to guess it. The script gives hints (higher/lower) until the correct number is guessed.
- **Run:**
	```powershell
	python Task2NumberGuessing/NumberGuessing.py
	```

## Task 3 — Word Counter

- **File:** `Task3WordCounter/WordCounter.py`
- **Description:** Reads a file and counts the number of words. The script now detects when you pass a directory and offers to count words in all `.txt` files in that directory. It also handles common errors like file-not-found and permission errors.
- **Included sample file:** `Task3WordCounter/word.txt` (small sample to test the script)
- **Run:**
	```powershell
	python Task3WordCounter/WordCounter.py
	```

	Example interactions:

	- To count a single file, enter the full or relative path when prompted, for example:

		`C:/Users/pc/OneDrive/Desktop/codveda_internship/Task3WordCounter/word.txt`

	- To count `.txt` files in the current directory, enter `.` and then confirm with `y` when the script asks:

		Enter the path to the file you want to count words in: .
		The path '.' is a directory.
		Count words in all '.txt' files inside this directory? (y/n): y

	The script will print per-file counts and a total.

