# 🎮 Tic Tac Toe – Player vs Computer

Welcome to a classic **Tic Tac Toe** game built in Python! This is a simple 2-player game between a **user** and the **computer** on a 3x3 grid.

---

## 🧠 Game Logic & Flow

Before jumping into the code, it’s important to map out the solution and understand the structure behind the game. Here's a breakdown of the problem and how the game flows:

### 📝 Problem Description

Tic Tac Toe is a two-player game played on a 3x3 board. Each player takes turns marking a square. The **first player** to align three of their marks either **horizontally**, **vertically**, or **diagonally** wins the game. If all 9 squares are filled without a winner, the game ends in a **tie**.

---

## 🔄 Gameplay Overview

1. **Display** the initial empty 3x3 board.
2. **Ask the user** to choose a square to mark.
3. **Computer** selects and marks a square.
4. **Display** the updated board state.
5. **Check** for a win:
   - If a player has 3 in a row → **declare the winner**.
6. **Check** for a full board:
   - If full and no winner → **declare a tie**.
7. If no winner and the board isn't full → **repeat from step 2**.
8. After game over → **Ask to play again**:
   - If yes → restart from step 1.
   - If no → **say goodbye and exit**.

---

## ✅ Features

- Interactive console-based gameplay
- Turn-based user vs computer
- Detects all win conditions
- Handles invalid user inputs gracefully
- Option to replay the game

---

## 📸 Example Output

```plaintext
   1 | 2 | 3
  ---+---+---
   4 | 5 | 6
  ---+---+---
   7 | 8 | 9

Your move (choose a position 1-9): 5

   X |   |  
  ---+---+---
     | O |  
  ---+---+---
          

...
Game Over! Player wins!
Play again? (y/n): 
```

---

## 🚀 Getting Started

To run the game:

```bash
python tic_tac_toe.py
```

---

## 🛠️ Requirements

- Python 3.x
- No additional libraries required

---

## 🤝 Contributions

Pull requests are welcome! If you'd like to improve the logic, add difficulty levels, or build a GUI version, feel free to fork and contribute.

---

## 📄 License

This project is open source under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙌 Credits

Built with ♥ by [YourName] as part of a hands-on learning journey into software development and game logic. Thanks for checking it out!

---
