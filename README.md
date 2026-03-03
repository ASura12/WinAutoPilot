# WinAutoPilot

A simple Python automation script that demonstrates how to control Windows applications using keyboard simulation. This project uses the `pyautogui` library to automate opening Notepad and typing predefined text.

---

## 🚀 Project Overview

This script performs the following actions:

1. Opens the Windows Start Menu
2. Searches for Notepad
3. Launches Notepad
4. Automatically types predefined text into it

It demonstrates basic desktop automation using Python.

---

## 🛠 Technologies Used

* Python 3
* pyautogui
* time (built-in module)

---

## 📂 Project Structure

```
WinAutoPilot/
│
├── main.py
└── README.md
```

---

## 📦 Installation

1. Install Python (if not already installed)
2. Install required library:

```
pip install pyautogui
```

---

## ▶️ How to Run

```
python main.py
```

Make sure:

* You are running this on a Windows machine
* No other active window interrupts the automation

---

## 🧠 How It Works

* `pyautogui.press()` simulates key presses
* `pyautogui.write()` simulates typing
* `time.sleep()` creates delays to allow applications to load

The script automates:

```
Win key → Type "notepad" → Press Enter → Type messages
```

---

## ⚠️ Important Notes

* Do not move your mouse or interrupt keyboard input while the script runs.
* Automation depends on screen focus.
* This script is designed specifically for Windows OS.

---

## 📈 Future Improvements

* Add support for other applications
* Add GUI for dynamic message input
* Add scheduling feature
* Add fail-safe key to stop execution
* Convert into a mini desktop automation toolkit

---

## 🎯 Learning Outcome

This project helps in understanding:

* Desktop automation basics
* Keyboard event simulation
* Process timing and execution flow
* Real-world automation concepts

---

## 📄 License

This project is for educational purposes.
