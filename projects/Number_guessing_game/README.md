# STATIC WEBSITE FOR PORTFOLIO

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : DHARUN PRASHOB M M

*INTERN ID* : CT04DY2328

*DOMAIN* : SOFTWARE DEVELOPMENT

*DURATION* : 4 WEEEKS

*MENTOR* : NEELA SANTOSH

**OUTPUT** : 

<img width="455" height="206" alt="image" src="https://github.com/user-attachments/assets/6b97dc01-025a-4929-a87a-10719b928ba7" />

Report on Refactoring – Number Guessing Game
1. Introduction

For Task 4, I selected the Number Guessing Game from the Python Mini Projects repository
 and worked on my own fork of the repository hosted at:

👉 My Forked Repository

The project was chosen because it is simple, widely understood, and allows for meaningful improvements in readability, maintainability, and robustness without altering its core logic.

2. Issues Found in Original Code

Entire code placed in global scope (no modularization).

No input validation (program crashes on invalid input).

Hardcoded range values (1–100).

No documentation or comments.

3. Refactoring Changes

Functions introduced → get_random_number(), get_user_guess(), and play_game().

Input validation added with try-except to handle non-numeric inputs.

Configurable range support added (instead of hardcoding 1–100).

Docstrings and comments provided for clarity.

Added a main guard (if __name__ == "__main__":) for Python best practices.

4. Impact on Performance

Runtime performance: No measurable difference (game logic remains lightweight).

Readability: Greatly improved due to modular functions and comments.

Maintainability: Easier for other developers to extend the game (e.g., new difficulty levels).

Robustness: Input validation prevents unexpected crashes.

5. Conclusion

Through this refactoring, the Number Guessing Game project became more structured, readable, and user-friendly, while maintaining the same functionality and performance.

📂 Refactored Code Location:
Available in my forked repository → My GitHub Fork

This demonstrates the importance of code readability and maintainability in real-world projects and satisfies the requirements of Task 4 – Code Refactoring and Performance Optimization.


# Number Guessing Game

This game allows you to check your luck and intuition :)
You should find the number computer guessed

### Usage
Just run "python main.py" in cmd command line after setting the project directory

### Here you can see sample
![Image](./image.png)

## *Author Name*

[Dharun Prashob M M](https://github.com/drun16/)
