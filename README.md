# Rock, Paper, Scissors Game

This project is a simple graphical implementation of the classic Rock, Paper, Scissors game using Python's Tkinter library. The game allows the player to compete against the computer, with the computer making random selections each round.

## Overview

The application creates a window-based GUI that features:
- **Game Title and Instructions:** Clearly labeled headings and messages guide the user to start playing.
- **Selection Buttons:** Three buttons allow the player to choose between Rock, Paper, and Scissors.
- **Display Areas:** Two text boxes show the player's choice and the computer's random selection.
- **Score Tracking:** The game keeps a tally of the player's score and the computer's score based on wins in each round.

## Features

- **Graphical User Interface (GUI):**  
  Built using Tkinter, the interface includes labels, textboxes, and buttons arranged for an intuitive play experience.

- **Randomized Computer Choices:**  
  The computer's move is selected randomly from a list of options each time the player makes a selection.

- **Score Updates:**  
  Global score variables update after every round depending on the game rules:
  - Rock beats Scissors.
  - Scissors beat Paper.
  - Paper beats Rock.
  
  *Note:* The tie scenario is identified in the code, though it does not update the score values.

## Prerequisites

- **Python 3:**  
  Make sure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

- **Tkinter:**  
  Tkinter usually comes bundled with Python. If it's not installed, refer to your system's package manager or Python documentation to add it.

## How to Run

1. **Add the Shebang Line:**  
   If you wish to run the Python file directly from the terminal in a Unix-like environment, insert the following shebang line at the very top of the Python file:
   ```python
   #!/usr/bin/env python3
   ```

2. **Make the Script Executable:**  
   After adding the shebang line, run the following command in your terminal to make the file executable:
   ```bash
   chmod +x your_script_name.py
   ```

3. **Run the Game:**  
   Execute the program by running:
   ```bash
   ./your_script_name.py
   ```
   Alternatively, you can run it using Python:
   ```bash
   python your_script_name.py
   ```

## Code Structure

- **Main Window Setup:**  
  The code initializes a Tkinter window with a set title, background color, and dimensions.
  
- **Widgets Setup:**  
  Widgets such as labels, textboxes, and buttons are created and positioned using the `place` geometry manager.
  
- **Game Logic:**  
  Three functions (`rock()`, `paper()`, and `scissors()`) capture the player's selection, randomly generate the computer's response, update the displayed choices, and adjust the scores accordingly.

- **Event Loop:**  
  The Tkinter `mainloop()` keeps the window open and responsive until the user closes the game.

## Customization

Feel free to modify or extend the code by:
- Adding additional styling to improve the GUI layout.
- Enhancing the game logic to include more detailed tie handling or additional game features.
- Integrating sound effects or animations to increase interactivity.

## Contact

For any questions or suggestions, please feel free to open an issue or contact the project maintainer at rishabhbhangale@gmail.com.

---
