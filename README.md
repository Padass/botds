# Official Discord Bot

This is an official Discord bot version of the keyword-response self-bot.

## Setup

1.  **Create a Discord Application and Bot:**
    *   Go to [Discord Developer Portal](https://discord.com/developers/applications).
    *   Create a new Application.
    *   Go to the "Bot" tab and click "Add Bot".
    *   **IMPORTANT:** Under "Privileged Gateway Intents", enable **"Message Content Intent"**. This is required to read messages.
    *   Copy the "Token".

2.  **Configuration:**
    *   Rename `.env.example` to `.env`.
    *   Open `.env` and paste your Bot Token:
        ```
        BOT_TOKEN=your_token_here
        ```
    *   Fill in the Channel IDs:
        ```
        CHANNEL_ID_NGUON=123456789012345678
        CHANNEL_ID_DICH=987654321098765432
        ```

3.  **Invite the Bot:**
    *   Go to the "OAuth2" tab -> "URL Generator".
    *   Select `bot` scope.
    *   Select permissions: `Read Messages/View Channels`, `Send Messages`.
    *   Copy the generated URL and invite the bot to your server.

4.  **Run the Bot:**
    *   Open a terminal in the project root.
    *   Run:
        ```bash
        python official_bot/bot.py
        ```
# botds
