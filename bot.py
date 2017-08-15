from nltk.chat.eliza import eliza_chatbot
from flask import Flask, request
import telepot
import urllib3

#from emoji import emojize

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "9c863667-8d88-4bc1-b76c-fbce34357f32"
bot = telepot.Bot('319745144:AAEalXJ_w_RGa8t7-8eTZvJBTkW84ive4L8')
bot.setWebhook("https://shivamahirao.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        if text == "/start":
           bot.sendMessage(chat_id, "Hello, I'm Shivam.  How can I help you? ")

        elif text =="Give me a compliment":
           bot.sendMessage(chat_id, "You look really good from far away!!")
           #bot.sendMessage(chat_id, emojize(":smile:", use_aliases=True))
        elif text =="I am your creator":
           bot.sendMessage(chat_id, "Does that give you power over me !!")
        elif text =="Do you know siri?":
           bot.sendMessage(chat_id, "No i am not interested in knowing her , cortana is good :)")
        elif text =="What time is it?":
           bot.sendMessage(chat_id, "check ur phone, or watch .")
        elif text =="Emergency contacts":
           bot.sendMessage(chat_id, "Dad - XXXXXXXX" + " " + "Mom - xxxxxxxxxxxx")
        elif text =="Who created you?":
           bot.sendMessage(chat_id, "Shivam Ahirao")
        elif text =="Who coded you?":
           bot.sendMessage(chat_id, "Shivam Ahirao")
        elif text =="who is your brother?":

        elif text =="SPPU timetable":
           bot.sendMessage(chat_id, "plz click on the link ->" + "http://collegecirculars.unipune.ac.in/sites/examdocs/Examiantions%20Timetables/Forms/AllItems.aspx")
        elif text =="SPPU Results":
           bot.sendMessage(chat_id, "plz click on the link ->" + "http://www.unipune.ac.in/university_files/results.htm")
        elif text =="Who are you?":
           bot.sendMessage(chat_id, "hello I am a ChatBot for Mr. Shivam Ahirao")
        elif text =="What is your name?":
           bot.sendMessage(chat_id, "hello I am Bot and my name is InsaneShivam101 , nice to meet you")
        elif text =="Where do you live?":
           bot.sendMessage(chat_id, "I live in ur phone")
        elif text =="How can i reach to shivam?":
           bot.sendMessage(chat_id, "pls click on the link ->" + "https://www.facebook.com/shivam.ahirao")
        elif text =="How old are you?":
           bot.sendMessage(chat_id, "Bot's never tell their age ;)")
        elif text =="which languages do you speak?":
           bot.sendMessage(chat_id, "I can speak English.")
        elif text =="How are you?":
           bot.sendMessage(chat_id, "I am good!")
        elif text =="Open Facebook":
           bot.sendMessage(chat_id, "pls click on the link ->" + "https://www.facebook.com/")
        elif text =="Open fb":
           bot.sendMessage(chat_id, "pls click on the link ->" + "https://www.facebook.com/")
        elif text =="Open Google":
           bot.sendMessage(chat_id, "pls click on the link ->" + "https://www.google.com/")
        elif text =="Open LinkedIn":
           bot.sendMessage(chat_id, "Pls click on the link ->" + "https://www.linkedin.com/")
        elif text =="Open YouTube":
           bot.sendMessage(chat_id, "Pls click on the link ->" + "https://www.youtube.com/")
        else:
           bot.sendMessage(chat_id, eliza_chatbot.respond(text))
    return "OK"
