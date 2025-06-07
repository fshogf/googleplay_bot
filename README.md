
# Google Play Review Bot (@Googleplay_review_bot)

This Telegram bot provides detailed information about Android apps from Google Play, along with user reviews and additional fun features like random facts and jokes. It uses data from CSV files (Kaggle dataset) and integrates Persian calendar dates.

---

## Features

- **🔍 App Search (Inline Mode)**  
  Search any Android app by typing `@Googleplay_review_bot <app name>` in any chat. The bot returns a list of matching apps with key info.

- **App Details**  
  View app details including:  
  → Title, Rating, Category  
  → Number of Reviews, Size, Installs  
  → Price (free/paid), and more

- **User Reviews**  
  After selecting an app, click the `Show 5Reviews` button to view five real user reviews, each labeled with sentiment (positive/negative/neutral).

- **Random Facts**  
  Use `/fact` to get a random interesting fact from an online API.

- **Random Jokes**  
  Use `/joke` to receive a funny, family-safe joke.

- **Persian Date**  
  Use `/date` to get today’s date in the Persian (Jalali) calendar.

- **Time Feature**  
  Use `/time` to get the **current time (hour, minute, second)** in local timezone.

- **Help Menu**  
  Use `/help` to see the list of all supported commands and how to use them.

---

## How to Use

1. Open Telegram and search for: [`@Googleplay_review_bot`](https://t.me/Googleplay_review_bot)
2. Send `/start` to initiate the bot
3. To search for an app, type:
   ```
   @Googleplay_review_bot facebook
   ```
4. Tap on a result to see app details
5. Click `Show 5Reviews` for real user reviews
6. Try `/fact`, `/joke`, `/date`, `/time`, or `/help` at any time

---

## Technical Details

| Component           | Description |
|--------------------|-------------|
| **Language**        | Python |
| **Library**         | `python-telegram-bot` (v20+) |
| **Data Handling**   | `pandas` for reading CSV datasets |
| **Date/Time**       | `persiantools.jdatetime` for Jalali date & `datetime.now()` for time |
| **APIs**            | Fetches random facts and jokes via public REST APIs |
| **Inline Support**  | Yes |
| **Callback Handling** | Yes (e.g., for `Show 5Reviews`) |
| **Error Handling**  | Included |

---

## Commands Summary

| Command   | Description                      |
|-----------|----------------------------------|
| `/start`  | Begin interaction with the bot   |
| `/help`   | List of available commands       |
| `/fact`   | Get a random fun fact            |
| `/joke`   | Get a random joke                |
| `/date`   | Show today's Persian date        |
| `/time`   | Show the current system time     |

---

## Project Purpose
Developed as a course project for Software Engineering at Semnan University (2nd Semester of 1403_4). The goal was to practice bot development, working with external 
datasets, API integration, and user interaction design.

---

## 🔗 Useful Links

- 🔗 GitHub: [github.com/fshogf/googleplay_bot](https://github.com/fshogf/googleplay_bot)
- 🔗 Telegram Bot: [@Googleplay_review_bot](https://t.me/Googleplay_review_bot)
- 🔗 Dataset: [Kaggle App Reviews](https://www.kaggle.com/datasets/lava18/google-play-store-apps)


