
# README - Google Play Review Bot (@Googleplay_review_bot)

This Telegram bot provides detailed information about Android apps from Google Play, along with user reviews and additional fun features like random facts and jokes. It uses data from CSV files (Kaggle dataset) and integrates Persian calendar dates.

---

## ▎Features

- **App Search via Inline Query:**  
  Search apps by name anywhere in Telegram by typing `@Googleplay_review_bot <app name>`. The bot will return a list of matching apps with key details.

- **App Details:**  
  View detailed information for each app such as rating, category, number of reviews, size, installs, price, and more.

- **User Reviews:**  
  After selecting an app, click the "Show 5Reviews" button to see the first five user reviews with sentiment analysis.

- **Random Facts:**  
  Use `/fact` command to get a random interesting fact from an external API.

- **Random Jokes:**  
  Use `/joke` command to receive a random funny joke.

- **Date and Time:**  
  Use `/date` to see today’s date in the Persian (Jalali) calendar and `/time` to get the current exact time.

- **Help:**  
  The `/help` command lists all available commands and instructions.

---

## ▎How to Use

1. Search for **@Googleplay_review_bot** in Telegram and send `/start` to initiate interaction.

2. To find an app, type `@Googleplay_review_bot <app name>` in any chat’s message input field and select the desired app from the inline search results.

3. Read app details displayed in the message.

4. Tap the **Show 5Reviews** button under the app details to see user reviews.

5. Use the commands `/fact`, `/joke`, `/date`, `/time`, and `/help` for additional functionality.

---

## ▎Technical Details

- Written in **Python** using the `python-telegram-bot` library (v20+).  
- Uses **Pandas** to read and filter CSV files containing app info and user reviews.  
- Fetches random facts and jokes via public REST APIs.  
- Displays Persian dates using `persiantools.jdatetime`.  
- Supports inline queries and callback queries for interactive experience.  
- Includes error handling and logging for robustness.

---

## ▎Project Purpose

Developed as a course project for Software Engineering at Semnan University (2nd Semester of 1403_4). The goal was to practice bot development, working with external datasets, API integration, and user interaction design.



