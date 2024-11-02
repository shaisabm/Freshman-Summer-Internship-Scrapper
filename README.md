# Summer 2025 Internships Scraper

This repository contains a Python project that scrapes internship listings from a specified URL and sends updates to a Telegram bot. The bot collects chat IDs of users who interact with it and sends them updates about new internships.

## Features

- Scrapes internship listings from a specified URL.
- Sends updates about new internships to a Telegram bot.
- Collects chat IDs of users who interact with the bot.
- Sends messages to all collected chat IDs.

## Prerequisites

- Python 3.7+
- `pip` (Python package installer)
- A Telegram bot token (You can create a bot using [BotFather](https://core.telegram.org/bots#botfather))

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/Summer2025-Internships-Scraper.git
    cd Summer2025-Internships-Scraper
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Telegram bot token:
    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    ```

5. Create a `data.json` file in the root directory with the following content:
    ```json
    {
        "last_visited": ""
    }
    ```

6. Create a `chat_ids.json` file in the root directory with the following content:
    ```json
    {
        "chat_ids": []
    }
    ```

## Usage

1. Run the Telegram bot:
    ```sh
    python telegram_bot.py
    ```

2. Run the job scraper:
    ```sh
    python job_scrapper.py
    ```

The bot will start collecting chat IDs of users who interact with it and the scraper will periodically check for new internships and send updates to all collected chat IDs.

## Files

- `telegram_bot.py`: Contains the code for the Telegram bot.
- `job_scrapper.py`: Contains the code for scraping internship listings and sending updates.
- `data.json`: Stores the last visited job title to avoid duplicate notifications.
- `chat_ids.json`: Stores the chat IDs of users who interact with the bot.
- `requirements.txt`: Lists the required Python packages.

