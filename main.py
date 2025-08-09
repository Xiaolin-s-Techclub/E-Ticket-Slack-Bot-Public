import os
import re
import csv
import pprint

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import handler

from dotenv import load_dotenv

load_dotenv("./.env")

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

app = App(token=SLACK_BOT_TOKEN)
shuukei={}
@app.event("")

# @app.message("hello")  # 送信されたメッセージ内に"hello"が含まれていたときのハンドラ
# def ask_who(say):
#     say("can I help you?")


@app.event("app_mention")
def respond_to_mention(event, say):
    thread_ts = event.get("thread_ts", None) or event.get("ts", None)

    message = re.sub(r'^<.*>', '', event['text']).lower()
    print(message)
    if "help" in message:
        msg = "List of commands:\n\
            - total number of users\n\
            - total number of tickets\n\
            - current entry status\n\
            - current exit status\n"
        say(text=msg, thread_ts=thread_ts)

    elif "total number of users" in message:
        say(text=str(handler.get_total_number_user()), thread_ts=thread_ts)
    elif "total number of tickets" in message:
        say(text=str(handler.get_total_number_ticket()), thread_ts=thread_ts)
    elif "current entry status" in message:
        say(text=str(handler.get_total_number_entry()), thread_ts=thread_ts)
    elif "current exit status" in message:
        say(text=str(handler.get_total_number_exit()), thread_ts=thread_ts)
    elif "number of users in hour" in message:
        with open('shuukei.csv') as f:
            reader = csv.reader(f)
            l = [row for row in reader]
            say(text=str(l[-1][1]-l[-2][1]), thread_ts=thread_ts)
    elif "number of tickets in hour" in message:
        with open('shuukei.csv') as f:
            l = [row for row in csv.reader(f)]
            say(text=str(int(l[-1][2])-int(l[-2][2])), thread_ts=thread_ts)
    elif "number of entry in hour" in message:
        with open('shuukei.csv') as f:
            l = [row for row in csv.reader(f)]
            say(text=str(int(l[-1][3])-int(l[-2][3])), thread_ts=thread_ts)
    elif "number of exit in hour" in message:
        with open('shuukei.csv') as f:
            l = [row for row in csv.reader(f)]
            say(text=str(int(l[-1][4])-int(l[-2][4])), thread_ts=thread_ts)
    elif "count start:" in message:
        shuukei[message[-3:]+"start"]=dict(handler.get_total_number_entry())["result"]
    elif "count lap:" in message:
        say("total_number_entry"+str(dict(handler.get_total_number_entry())["result"]-shuukei[message[-3:]+"start"]), thread_ts=thread_ts)
    elif "count list" in message:
        say(shuukei, thread_ts=thread_ts)
    elif "shuukei exh" in message:
        with open('shuukei.csv') as f:
            reader = csv.reader(f)
            l = [row for row in reader]
            say(str(l), thread_ts=thread_ts)
    elif "shuukei set" in message:
        with open('shuukei.csv') as f:
            reader = csv.reader(f)
            l = [row for row in reader]
            say(l, thread_ts=thread_ts)
    else:
        say(text="Invalid command. Tye 'help' to see the list of commands.", thread_ts=thread_ts)


@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
