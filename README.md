# Telegram Bot for Database Queries

This repository contains a Python-based Telegram bot that queries a local SQLite database and returns records based on user-provided search terms. The bot supports multiple search modes, including searching by first name, last name, city, or exact ID. It’s designed to handle large datasets efficiently by leveraging SQL queries rather than loading entire files into memory.

## Features

- **Search by ID**:  
  A single numeric query returns exact matches by ID.
  
- **Search by Name**:  
  - **Single Term (Non-numeric)**: Partial matches by first or last name.
  - **Two Terms**: Exact matches for first and last name.
  - **Three Terms**: Partial matches for first name, last name, and city.
  
- **RTL (Right-to-Left) Language Support**:  
  Hebrew or other RTL languages display correctly by using Unicode directional markers.

- **Secure Configuration via `.env`**:  
  - Store sensitive data (like bot tokens) in a `.env` file rather than hard-coding them.

## Requirements

- **Python 3.8+**
- **Dependencies**:
  - `python-telegram-bot` version 20+
  - `python-dotenv` for reading environment variables from `.env`
  - `sqlite3` (part of standard Python)
  - Other dependencies listed in `requirements.txt` (if provided)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/buzagloidan/database-explorer.git
   cd database-explorer
   ```

2. **Create and Activate a Virtual Environment (Recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   If no `requirements.txt` is provided, install essential packages:
   ```bash
   pip install python-telegram-bot --upgrade
   pip install python-dotenv
   ```

4. **Create a `.env` File**:
   Create a file named `.env` in the project directory:
   ```env
   BOT_TOKEN=your-telegram-bot-token
   DB_PATH=path/to/records.db
   ```
   
   Replace `your-telegram-bot-token` and `path/to/records.db` with your actual token and database path.

   **Important**: Do not commit `.env` to your public repository. Add `.env` to your `.gitignore` file.

5. **Prepare the Database**:
   - Ensure you have a properly structured SQLite database with the `records` table.
   - If you need to import data from a CSV, run any provided import scripts or follow instructions in the repo’s documentation.
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

- **/start**: Show a welcome message and instructions.
- **/help**: Display help and search modes.
- **/search <query>**: Perform a search.
  
**Examples**:
- `/search עידן`  
  Searches partial matches for first or last name containing "עידן".
  
- `/search 123456`  
  Searches exact ID match for ID 123456.
  
- `/search עידן בוזגלו`  
  Searches exact matches where first name = "עידן" and last name = "בוזגלו".
  
- `/search עידן בוזגלו תל`  
  Searches partial matches for first name "עידן", last name "בוזגלו", and city containing "תל" (e.g. "תל אביב").

## Security Considerations

- **.env File for Secrets**:  
  Store your bot token and other sensitive information in `.env`. This file should not be committed to the repository.  
  Add `.env` to `.gitignore` to prevent accidental commits.

- **Limit Access (Optional)**:  
  If needed, you can implement a whitelist of user IDs to restrict who can use the bot.  
  For example, check `update.message.from_user.id` against a set of allowed IDs.

- **Database and Server Security**:  
  Keep the database file private and ensure it’s not publicly accessible.  
  If running on a server, ensure proper firewalls and no open ports for public database access.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and update tests if applicable.
4. Submit a pull request with a clear description of the changes.

## License

This project is available under the MIT License. See the [LICENSE](LICENSE) file for details.
