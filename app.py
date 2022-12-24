import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
import fsm
from utils import send_text_message,send_another_message
from web_crawler import youtube_video_parser

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time as time

load_dotenv()

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

machine = TocMachine(
    states=["interaction", "situation", "choose_what_to_eat", "eat_breakfast", "eat_lunch", "eat_dinner", "eat_snack",
            "choose_what_to_drink", "drink_water", "drink_milktea",  "drink_tea", "wake", "sleep",
            "playing","company", "rps", "shoot", "bas", "shake", "YT", "search_YT"],
    transitions=[
        {#顯示狀態
            "trigger": "advance",
            "source": ["wake","sleep"],
            "dest": "situation",
            "conditions": "is_going_to_show_situation",
        },
        {#顯示狀態
            "trigger": "advance",
            "source": ["wake","sleep"],
            "dest": "interaction",
            "conditions": "is_going_to_interact",
        },
        {#吃飯選要吃什麼
            "trigger": "advance",
            "source": "interaction",
            "dest": "choose_what_to_eat",
            "conditions": "is_going_to_eating",
        },
        {#吃早餐
            "trigger": "advance",
            "source": "choose_what_to_eat",
            "dest": "eat_breakfast",
            "conditions": "is_going_to_eat_breakfast",
        },
        {#吃午餐
            "trigger": "advance",
            "source": "choose_what_to_eat",
            "dest": "eat_lunch",
            "conditions": "is_going_to_eat_lunch",
        },
        {#吃晚餐
            "trigger": "advance",
            "source": "choose_what_to_eat",
            "dest": "eat_dinner",
            "conditions": "is_going_to_eat_dinner",
        },
        {#吃點心
            "trigger": "advance",
            "source": "choose_what_to_eat",
            "dest": "eat_snack",
            "conditions": "is_going_to_eat_snack",
        },
        {#喝東西並選擇要喝什麼
            "trigger": "advance",
            "source": "interaction",
            "dest": "choose_what_to_drink",
            "conditions": "is_going_to_choose_what_to_drink",
        },
        {#喝水
            "trigger": "advance",
            "source": "choose_what_to_drink",
            "dest": "drink_water",
            "conditions": "is_going_to_drink_water",
        },
        {#喝奶茶
            "trigger": "advance",
            "source": "choose_what_to_drink",
            "dest": "drink_milktea",
            "conditions": "is_going_to_drink_milktea",
        },
        {#喝茶
            "trigger": "advance",
            "source": "choose_what_to_drink",
            "dest": "drink_tea",
            "conditions": "is_going_to_drink_tea",
        },
        {#睡覺
            "trigger": "advance",
            "source": "interaction",
            "dest": "sleep",
            "conditions": "is_going_to_sleep",
        },
        {#起床
            "trigger": "advance",
            "source": "interaction",
            "dest": "wake",
            "conditions": "is_going_to_wake",
        },
        {#玩遊戲
            "trigger": "advance",
            "source": "interaction",
            "dest": "playing",
            "conditions": "is_going_to_playing",
        },
        {#猜拳
            "trigger": "advance",
            "source": "playing",
            "dest": "rps",
            "conditions": "is_going_to_rps",
        },
        {#出拳
            "trigger": "advance",
            "source": "rps",
            "dest": "shoot",
            "conditions": "is_going_to_shoot",
        },
        {#big and small
            "trigger": "advance",
            "source": "playing",
            "dest": "bas",
            "conditions": "is_going_to_bas",
        },
        {#shake
            "trigger": "advance",
            "source": "bas",
            "dest": "shake",
            "conditions": "is_going_to_shake",
        },
        {#陪伴
            "trigger": "advance",
            "source": "interaction",
            "dest": "company",
            "conditions": "is_going_to_be_company",
        },
        {#YT
            "trigger": "advance",
            "source": "company",
            "dest": "YT",
            "conditions": "is_going_to_YT",
        },
        {#search YT
            "trigger": "advance",
            "source": "YT",
            "dest": "search_YT",
            "conditions": "is_going_to_search_YT",
        },
        {#返回
            "trigger": "go_back", 
            "source": ["wake", "interaction", "situation", "choose_what_to_eat","eat_breakfast", "eat_lunch", "eat_dinner","eat_snack",
                       "choose_what_to_drink", "drink_water", "drink_milktea", "drink_tea", 
                       "playing","rps", "shoot", "bas", "shake", 
                       "company", "YT", "search_YT"], 
            "dest": "wake"
        },
    ],
    initial="interaction",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_another_message(event.reply_token, fsm.decision())
            machine.go_back(event)

    
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
    while time.localtime(time.time()).tm_sec == 0:     
        print(time.localtime(time.time()))   
        fsm.job()
