# Seven of Nine – Anonymous Role-Based Voting Bot 🤖

A Discord bot for anonymous voting, limited to users with a specific role. Created as part of the Collective. Resistance is futile.

## Features

- 🔒 Role-restricted voting
- 🕵️ Anonymous votes using buttons
- ⏳ Default 7-day voting duration (customizable)
- 💬 Slash command interface
- 🗳️ Embedded messages with live results
- 💾 Persistent storage using SQLite

## Commands

### `/vote`
Creates an anonymous vote.

**Options:**
- `question`: The question to vote on (string, required)
- `role`: The Discord role allowed to vote (role mention, required)
- `duration`: Duration of the vote in minutes (integer, optional, default 10080)

### Example usage

/vote question:"Should we assimilate the Alpha Quadrant?" role:@Voters duration:1440

## Installation

### Prerequisites

- Python 3.9 or higher installed
- Discord bot token (create your bot on https://discord.com/developers/applications)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/seven-of-nine.git
   cd seven-of-nine

2. (Optional but recommended) Create and activate a Python virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate


3. Install dependencies:

    ```bash
    pip install -r requirements.txt


4. Configure environment variables:

   - Copy .env.example to .env:

   ```bash
   cp .env.example .env


Edit .env to add your Discord bot token and guild ID:

   ```bash
   DISCORD_TOKEN=your-bot-token-here
   GUILD_ID=your-guild-id-here


```
5. Run the bot:

   ```bash
   python3 bot.py



## License

This project is licensed under the MIT License. See the LICENSE file for details.


---

Made with 🧠 by TheDoomedBengal. Operated by the Collective. Resistance is futile.
