# 🎴 Hazari Score Counter

A modern multiplayer Hazari score counter built with Django.

---

## ✨ Features

- 🎮 Modern Dashboard
- 👑 Live Leaderboard
- 😂 Funny Rank Messages
- ✨ Auto Fill Score
- 📊 Animated Progress Bar
- 📜 Round History
- ✏️ Edit Round
- 🗑 Delete Round
- 🔄 Reset Game
- 📱 Responsive Design
- 🎯 360 Points Validation

---

## 🛠 Tech Stack

- Python
- Django
- Bootstrap 5
- HTML
- CSS
- JavaScript

---

## Installation

```bash
git clone <repo>

cd hazari-score-counter

python -m venv .venv

source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install

```bash
pip install -r requirements.txt
```

Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

Run

```bash
python manage.py runserver
```

---

## Game Rules

- Fixed 4 Players
- Every Round Total = 360
- First Player to Target Score Wins
- Any Player can use Auto Fill
- Wrong Round can be Edited
- Round can be Deleted

---

## Folder Structure

```
hazari-score-counter/

config/

game/

templates/

static/

manage.py

requirements.txt
```

---

## Future Features

- Dark Mode
- Confetti
- Export PDF
- Share Result
- Sound Effect
- Tournament Mode

---

Made with ❤️ using Django