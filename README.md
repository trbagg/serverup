# Minecraft Server-Up Bot

A simple python script for a discord bot for checking whether a minecraft server is up or not.

## Installation
1. Clone the repository
    ```bash
    git clone https://github.com/trbagg/serverup.git
    ```
2. Navigate to the directory
    ```bash
    cd repo
    ```
3. Install requirements
    ```bash
    pip install requirements.txt
    ```
3. Create a dot-env file in the directory with the following contents
    ```
    DISCORD_TOKEN=YOUR_API_TOKEN_HERE
    DISCORD_GUILD=SPECIFIED_GUILD_HERE
    ADDRESS=SPECIFIED_SERVER_ADDRESS_HERE:SPECIFIED_PORT_HERE
    ```

## Usage
1. Run the python script
    ```
    pip
    ```
2. [Add the bot](https://discord.com/oauth2/authorize?client_id=1470114967402582076) to the specified server
3. Use the /status command in the specified server