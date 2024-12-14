# Telegram Bot for Database Queries

This repository contains a Python-based Telegram bot that queries a local SQLite database and returns records based on user-provided search terms. The bot supports multiple search modes, including searching by first name, last name, city, or exact ID. It’s designed to handle large datasets efficiently by leveraging SQL queries rather than loading entire files into memory.

## Features

- **Search by ID:**  
  A single numeric query returns exact matches by ID.
  
- **Search by Name:**  
  - **Single Term (Non-numeric):** Partial matches by first or last name.
  - **Two Terms:** Exact matches for first and last name.
  - **Three Terms:** Partial matches for first name, last name, and city.
  
- **RTL (Right-to-Left) Language Support:**  
  Hebrew or other RTL languages display correctly by using Unicode directional markers.

- **Secure Configuration:**  
  - Token stored in environment variables (not hard-coded).
  - Optional user whitelisting to restrict access.

## Requirements

- **Python 3.8+**
- **Dependencies:**
  - `python-telegram-bot` version 20+
  - `sqlite3` (part of the standard Python library)
  - Other dependencies listed in `requirements.txt` (if provided)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/buzagloidan/database-explorer.git
   cd database-explorer
   ```

2. **Create and Activate a Virtual Environment (Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   If a `requirements.txt` file is not provided, install `python-telegram-bot`:
   ```bash
   pip install python-telegram-bot --upgrade
   ```

4. **Set Your Environment Variables:**
   Set your Telegram bot token in an environment variable:
   ```bash
   export BOT_TOKEN="your-telegram-bot-token"
   ```
   
   If your database is named differently or located elsewhere, set `DB_PATH` as well:
   ```bash
   export DB_PATH="path/to/records.db"
   ```

5. **Prepare the Database:**
   - Ensure you have a properly structured SQLite database with the `records` table.
   - If you need to import data from a CSV, see instructions or scripts in this repo (if provided).
   - Confirm the database schema matches the queries in the Python code.

## Running the Bot

Once everything is set up, run:

```bash
python bot.py
```

(The script name may differ depending on your implementation; update accordingly.)

The bot will start polling Telegram’s servers. Press **Ctrl + C** to stop.

## Usage

In Telegram:

- **/start**: Show welcome message and instructions.
- **/help**: Display help and search modes.
- **/search <query>**: Perform a search.
  
**Examples:**
- `/search עידן`  
  Searches for partial matches in first or last name.
  
- `/search 123456`  
  Searches for an exact ID match.
  
- `/search עידן בוזגלו`  
  Searches for a record where first name = עידן and last name = בוזגלו.
  
- `/search עידן בוזגלו ראשון`  
  Searches for partial matches where first name and last name match עידן and בוזגלו respectively, and city contains ראשון.

## Security Considerations

- **Do not share your bot token publicly.**  
  Store it in environment variables or a secure secret manager.
  
- **Optional Whitelisting:**  
  If you want only certain user IDs to use the bot, add a check in the `search_command` function.

- **Database Access:**  
  Keep the database file private and ensure it’s not publicly accessible. Use local paths and do not expose ports to the internet.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and update tests if applicable.
4. Submit a pull request with a clear description of your changes.

## License

This project is available under the MIT License. See the [LICENSE](LICENSE) file for details.
