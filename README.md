# 🪨📄✂️ Rock-Paper-Scissors Simulator

A smart, interactive, and terminal-based Rock-Paper-Scissors game implemented in Python. It features live score tracking, inputs validation, and an automated PC opponent.

<p align="center">
  <img src="game-animation.svg" alt="Rock Paper Scissors Animation" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
</p>

---

## 🚀 Key Features

- **🤖 Random AI Opponent:** Built using Python's native `random` module to ensure unpredictable PC moves.
- **📊 Win Record Tracker:** Dynamically stores and displays the player's and PC's total score across multiple consecutive rounds.
- **🛡️ Robust Input Validation:** Prevents crashes or unintended behaviors by continuously validating user input.
- **🔄 Infinite Replayability:** Loops seamlessly, allowing the user to play as many rounds as desired and exit anytime.

---

## 🎮 How to Play

The game follows the classic international rules:
* 🪨 **Rock** beats ✂️ Scissor
* ✂️ **Scissor** beats 📄 Paper
* 📄 **Paper** beats 🪨 Rock

### Score Keeping System
The application persists your score in volatile memory during runtime. Every time you win or lose, the persistent metrics update instantly:

| Outcome | Score Update |
| :--- | :--- |
| 🎉 **User Won** | `user_win += 1` |
| 💻 **PC Won** | `pc_win += 1` |
| 🤝 **Draw** | No score changes |

---

## 💻 Code Structure

The project is designed clean and modularly with specific functions:

- `get_user_input()`: Safely fetches and sanitizes terminal input.
- `get_pc_input()`: Generates a computerized random move.
- `determine_winner()`: Applies the core logical matrix to determine the round victor.
- `main()`: Acts as the runner function to sync data flowing between user and PC.

```python
# Core Game Logic Matrix Preview
elif (user_input == "rock" and pc_input == "scissor") \
  or (user_input == "scissor" and pc_input == "paper") \
  or (user_input == "paper" and pc_input == "rock"):
    return "user won"
