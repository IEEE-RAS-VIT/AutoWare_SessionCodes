from instabot import Bot
import secretKey
bot=Bot()
username="techie_231"
bot.login(username=username,password=secretKey.password())
print("Login Successful")
img="demo.jpg"
bot.upload_photo(img,caption="This is a demo image")
bot.logout()
