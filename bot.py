import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID_NGUON_STR = os.getenv('CHANNEL_ID_NGUON')
CHANNEL_ID_DICH_STR = os.getenv('CHANNEL_ID_DICH')

if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found in .env file.")
    # We don't raise error immediately to allow user to set it up
    
CHANNEL_ID_NGUON = int(CHANNEL_ID_NGUON_STR) if CHANNEL_ID_NGUON_STR else None

# Configuration for Destination Channels
# Each channel has 3 roles:
# role_1: Fruits (Dưa hấu, Bí ngô...)
# role_2: Tools (Vòi xanh, Đơn hàng...)
# role_3: Weather (Ánh trăng, Bão...)
DESTINATIONS = [
    # Channel 1
    {
        "id": 1442320850417225799,
        "name": "Channel 1",
        "roles": {
            "role_1": 1444284941172215888, 
            "role_2": 1444284941172215888, 
            "role_3": 1444284941172215888 # Example of multiple roles
        }
    },
    # Channel 2
    {
        "id": 1444167053568114748,
        "name": "Channel 2",
        "roles": {
            "role_1": 1444166788723249284, 
            "role_2": 1444166850719121530, 
            "role_3": 1444166935158980778,
        }
    },
    # Channel 3
    {
        "id": 1444240097829716000,
        "name": "Channel 3",
        "roles": {
            "role_1": 71111, 
            "role_2": 82222, 
            "role_3": 9
        }
    },
    # Channel 4
    {
        "id": 0,
        "name": "Channel 4",
        "roles": {
            "role_1": 0, 
            "role_2": 0, 
            "role_3": 0
        }
    },
    # Channel 5
    {
        "id": 0,
        "name": "Channel 5",
        "roles": {
            "role_1": 0, 
            "role_2": 0, 
            "role_3": 0
        }
    },
    # Channel 6
    {
        "id": 0,
        "name": "Channel 6",
        "roles": {
            "role_1": 0, 
            "role_2": 0, 
            "role_3": 0
        }
    },
    # Channel 7
    {
        "id": 0,
        "name": "Channel 7",
        "roles": {
            "role_1": 0, 
            "role_2": 0, 
            "role_3": 0
        }
    },
    # Channel 8
    {
        "id": 0,
        "name": "Channel 8",
        "roles": {
            "role_1": 0, 
            "role_2": 0, 
            "role_3": 0
        }
    },
    # Channel 9
    {
        "id": 0,
        "name": "Channel 9",
        "roles": {
            "role_1": 0, 
            "role_2": 0, 
            "role_3": 0
        }
    },
    # Channel 10
    {
        "id": 0,
        "name": "Channel 10",
        "roles": {
            "role_1": 0, 
            "role_2": 0, 
            "role_3": 0
        }
    },
]

# Configure intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Keyword mapping with Role Categories
KEYWORD_DATA = {
    "dưa hấu": {"msg": "**Dưa hấu** đang bán trong Shop!!", "role": "role_1"},
    "bí ngô": {"msg": "**Bí ngô** đang bán trong Shop!!", "role": "role_1"},
    "xoài": {"msg": "**Xoài** đang bán trong Shop!!", "role": "role_1"},
    "táo đường": {"msg": "**Táo đường** đang bán trong Shop!!", "role": "role_1"},
    "đậu": {"msg": "**Đậu** đang bán trong Shop!!", "role": "role_1"},
    "khế": {"msg": "**Khế** đang bán trong Shop!!", "role": "role_1"},
    
    "vòi xanh": {"msg": "**Vòi Xanh** đang bán trong Shop!!", "role": "role_2"},
    "vòi đỏ": {"msg": "**Vòi Đỏ** đang bán trong Shop!!", "role": "role_2"},
    "đơn hàng": {"msg": "**Đơn hàng** đã được làm mới!!", "role": "role_2"},
    
    "ánh trăng": {"msg": "**Ánh Trăng** xuất hiện!! có thể xuất hiện biến thể **[ Ánh Trăng ]**", "role": "role_3"},
    "cực quang": {"msg": "**Cực Quang** xuất hiện!! có thể xuất hiện biến thể **[ Cực Quang ]**", "role": "role_3"},
    "bão": {"msg": "**Bão** xuất hiện!! có thể xuất hiện biến thể **[ Nhiễm Điện ]**", "role": "role_3"},
    "mưa": {"msg": "**Mưa** xuất hiện!! có thể xuất hiện biến thể **[ Ẩm ướt ]**", "role": "role_3"},
    "sương mù": {"msg": "**Sương Mù** xuất hiện!! có thể xuất hiện biến thể **[ Ẩm ướt ]**", "role": "role_3"},
    "sương sớm": {"msg": "**Sương Sớm** xuất hiện!! có thể xuất hiện biến thể **[ Sương]**", "role": "role_3"},
    "gió": {"msg": "**Gió** xuất hiện!! có thể xuất hiện biến thể **[ Gió ]**", "role": "role_3"},
    "nắng nóng": {"msg": "**Nắng Nóng** xuất hiện!! có thể xuất hiện biến thể **[ Khô ]**", "role": "role_3"},
    "gió cát": {"msg": "**Gió Cát** xuất hiện!! có thể xuất hiện biến thể **[ Cát ]**", "role": "role_3"},
    "ảo ảnh": {"msg": "**Ảo Ảnh** xuất hiện!! có thể xuất hiện biến thể **[ Ảo Ảnh ]**", "role": "role_3"},
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    if not CHANNEL_ID_NGUON:
        print("WARNING: Source Channel ID not set in .env file.")
    if not DESTINATIONS:
        print("WARNING: No destination channels configured in bot.py.")

@bot.event
async def on_message(message):
    print(f"\n--- New Message Received ---")
    print(f"Time: {message.created_at}")
    print(f"Author: {message.author} (ID: {message.author.id})")
    print(f"Channel: {message.channel} (ID: {message.channel.id})")
    print(f"Content: '{message.content}'")

    # Ignore messages from self
    if message.author == bot.user:
        print("-> Ignored: Message from self.")
        return

    # Only process messages from source channel
    if message.channel.id != CHANNEL_ID_NGUON:
        print(f"-> Ignored: Channel ID {message.channel.id} does not match source {CHANNEL_ID_NGUON}")
        return

    print(f"-> Processing valid message...")

    content_lower = message.content.lower()
    
    keyword_found = False
    for keyword, data in KEYWORD_DATA.items():
        if keyword in content_lower:
            keyword_found = True
            print(f"-> Found keyword: '{keyword}'. Sending to {len(DESTINATIONS)} destinations...")
            
            role_key = data["role"]
            base_message = data["msg"]
            
            for dest in DESTINATIONS:
                dest_id = dest.get("id")
                
                # Skip if ID is not set or invalid
                if not dest_id or dest_id == 0:
                    continue

                role_val = dest["roles"].get(role_key)
                
                # Handle both single ID and list of IDs
                role_mentions = ""
                if isinstance(role_val, list):
                    role_mentions = " ".join([f"<@&{rid}>" for rid in role_val])
                elif role_val:
                    role_mentions = f"<@&{role_val}>"
                else:
                    role_mentions = "" # No role configured

                # Construct message with specific role(s)
                if role_mentions:
                    final_message = f"{base_message}\n|| {role_mentions} ||"
                else:
                    final_message = base_message
                
                dest_channel = bot.get_channel(dest_id)
                if dest_channel:
                    try:
                        await dest_channel.send(final_message)
                        print(f"-> Sent to {dest_channel.name} ({dest_id}) with Roles: {role_val}")
                    except discord.Forbidden:
                        print(f"-> Error: Missing permissions in {dest_id}")
                    except Exception as e:
                        print(f"-> Error sending to {dest_id}: {e}")
                else:
                    print(f"-> Error: Could not find channel {dest_id}")
            break
            
    if not keyword_found:
        print("-> No keyword found.")

if __name__ == '__main__':
    if BOT_TOKEN:
        bot.run(BOT_TOKEN)
    else:
        print("Please set BOT_TOKEN in .env file")
