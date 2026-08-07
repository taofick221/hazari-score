import random

ROUND_TOTAL = 360


KING_MESSAGES = [
    "👑 King of Bed 🛏️",
    "🔥 Cheat Code Activated",
    "🐐 GOAT",
    "💰 Money Collector",
    "🎯 Aim Bot",
    "🚀 Unstoppable",
    "😎 Sigma Male",
    "⚡ CEO of Hazari",
    "💀 Lobby Destroyer",
    "👽 Alien Player",
    "🥶 Ice Cold",
    "🦁 Alpha Player",
    "🏆 Respect +999",
    "🤴 Daddy of Hazari",
    "💎 Diamond Hands",
]


SECOND_MESSAGES = [
    "🛢️ Use More Oil",
    "😤 Almost Crying",
    "🏃 Catch Him If You Can",
    "😂 Better Luck Next Round",
    "⚡ Runner-Up Forever",
    "🐌 Loading...",
    "📈 Improving Slowly",
    "🥲 So Close",
    "🙄 NPC Energy",
    "🔥 Don't Give Up",
    "😎 Backup Hero",
    "🤏 Mini Boss",
]


THIRD_MESSAGES = [
    "😂 Bou Thakbe Na",
    "🛏️ King of Bed",
    "😴 Wake Up Bro",
    "🐌 Slow Motion",
    "🤡 Circus Player",
    "📶 Weak Network",
    "🥔 Potato Player",
    "🙈 Blind Mode",
    "🧠 Brain Not Found",
    "💤 Sleeping Beauty",
    "🐸 Frog Power",
    "😅 Better Than Last",
]


LAST_MESSAGES = [
    "😂 Halar Dari Na",
    "☕ Tea Sponsor",
    "🍌 Banana Rank",
    "🪑 Bench Player",
    "📦 Delivery Boy",
    "🐢 Turtle Mode",
    "🧂 Salt Collector",
    "🧹 Room Cleaner",
    "📉 Stock Market Crash",
    "🫠 Mission Failed",
    "🚑 Call Ambulance",
    "💀 Respawn Required",
    "😵 Lost Connection",
    "🤦 Skill Issue",
    "🛌 AFK Player",
]


GAME_START_MESSAGES = [
    "🔥 Friendship Ends Today",
    "😂 Loser Buys Tea",
    "👑 Only One King",
    "💀 No Mercy Today",
    "😈 Prepare To Cry",
    "🍔 Loser Pays The Bill",
    "☕ Tea Is Ready",
    "🏆 Winner Gets Respect",
    "🎯 Let The War Begin",
    "⚡ Skill Check Time",
    "😎 Today We Roast Everyone",
    "🤣 Survival Starts Now",
]


WINNER_MESSAGES = [
    "👑 ALL HAIL THE KING!",
    "🔥 Respect +9999",
    "🐐 GOAT CONFIRMED!",
    "😎 Built Different!",
    "🏆 Easy Game!",
    "💰 Richest Player Today!",
    "🚀 Too Easy!",
    "💀 Everyone Got Destroyed!",
]


def random_king_message():
    return random.choice(KING_MESSAGES)


def random_second_message():
    return random.choice(SECOND_MESSAGES)


def random_third_message():
    return random.choice(THIRD_MESSAGES)


def random_last_message():
    return random.choice(LAST_MESSAGES)


def random_game_banner():
    return random.choice(GAME_START_MESSAGES)


def random_winner_message():
    return random.choice(WINNER_MESSAGES)
