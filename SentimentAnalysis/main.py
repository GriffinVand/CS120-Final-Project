from instabot import Bot

# Initialize a bot instance
bot = Bot()

# Login to your Instagram account
bot.login(username="griffinthevander111", password="Bubby88!")

# Upload a story
bot.upload_story_photo("SentimentAnalysis/Images/Pirate.jpg")

# Logout from your Instagram account
bot.logout()