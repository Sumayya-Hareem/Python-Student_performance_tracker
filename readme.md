# Student Performance Tracker

## Overview
The **Student Performance Tracker** is a Python program that allows teachers to input and manage student scores for multiple subjects. It calculates individual and class averages, tracks performance, and provides feedback on whether students are passing or need improvement.

---

## Features
- **Add Students**:
  - Input student names and scores for subjects (Math, Science, English).
  - Validates input to ensure scores are integers between 0 and 100.
  
- **Track Performance**:
  - Calculate individual average scores.
  - Determine pass/fail status for each student based on a passing threshold (default is 40).

- **Class Metrics**:
  - Calculate and display the overall class average score.
  - Summarize all student performances in a clean, readable format.

- **Error Handling**:
  - Handles invalid input gracefully (e.g., non-numeric scores or out-of-range values).
  - Allows continuous input until the user decides to stop.

---

## How It Works
1. **Input Students**:
   - Enter the name of each student.
   - Input their scores for Math, Science, and English.

2. **Performance Calculation**:
   - The program calculates:
     - Each student's average score.
     - Whether the student is passing or needs improvement.
   - The overall class average.

3. **Output Results**:
   - Displays performance for each student (name, average score, pass/fail status).
   - Shows the class average score.

---

## Usage
### Prerequisites
- Python 3.x installed on your system.

### Running the Program
1. Clone this repository or copy the code into a `.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using:
   ```bash
   python student_performance_tracker.py
