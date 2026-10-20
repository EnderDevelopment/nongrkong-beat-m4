# Nongrkong Beat M4: Discord Music Bot

Nongrkong Beat M4 is a Discord bot designed to enhance your server's music experience. It allows users to play, pause, resume, and stop music from YouTube directly in your Discord voice channels. The bot is built using Python and the discord.py library, ensuring a seamless and interactive music experience for your community.

## Install

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project directory and add your Discord bot token and YouTube API key:
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   YOUTUBE_API_KEY=your_youtube_api_key_here
   ```

## Use

1. Invite the bot to your Discord server using the OAuth2 URL generated from the Discord Developer Portal.
2. Connect the bot to a voice channel using the `!join` command.
3. Use the following commands to control the music:
   - `!play <url>`: Play music from a YouTube URL.
   - `!pause`: Pause the currently playing music.
   - `!resume`: Resume the paused music.
   - `!stop`: Stop the currently playing music.

---

More Discord bot projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/ca398a1f-1f40-4936-8309-e29b76d7ba5b?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=ca398a1f-1f40-4936-8309-e29b76d7ba5b
