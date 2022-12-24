from transitions.extensions import GraphMachine
import petfunction
from utils import send_text_message, send_another_message
import os
#feed drink play sleep study
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_show_situation(self, event):
        print("show situation")
        text = event.message.text
        return text == "顯示狀態"
    
    def on_enter_situation(self, event):
        msg = show_situation()
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()

    def is_going_to_interact(self, event):
        text = event.message.text
        return text == "在嗎"
    
    def on_enter_interaction(self, event):
        print("show interact interface")

        reply_token = event.reply_token
        msg = interaction()
        send_another_message(reply_token, msg)
    
    def is_going_to_eating(self, event):
        print(event)
        text = event.message.text
        return text == "吃東西吧"
    
    def on_enter_choose_what_to_eat(self, event):
        situation[0] -= random.randint(1,10)
        situation[1] -= random.randint(1,10)
        situation[2] -= random.randint(1,5)
        situation[3] -= random.randint(1,5)

        reply_token = event.reply_token
        msg = choose_what_to_eat()
        send_another_message(reply_token, msg)
           
    def is_going_to_eat_breakfast(self, event):
        text = event.message.text
        return text == "吃早餐"
    
    def on_enter_eat_breakfast(self, event):
        situation[1] -= random.randint(1,20)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,20)
        reply_token = event.reply_token
        msg = eating("breakfast")
        send_text_message(reply_token, msg)
        self.go_back()
    
    def is_going_to_eat_lunch(self, event):
        text = event.message.text
        return text == "吃午餐"
    
    def on_enter_eat_lunch(self, event):
        situation[1] -= random.randint(1,20)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,20)
        msg = eating("lunch")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
    
    def is_going_to_eat_dinner(self, event):
        text = event.message.text
        return text == "吃晚餐"
    
    def on_enter_eat_dinner(self, event):
        situation[1] -= random.randint(1,20)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,20)
        msg = eating("dinner")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
    
    def is_going_to_eat_snack(self, event):
        text = event.message.text
        return text == "吃點心"
    
    def on_enter_eat_snack(self, event):
        situation[1] -= random.randint(1,20)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,20)
        msg = eating("snack")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
    
    def is_going_to_choose_what_to_drink(self, event):
        text = event.message.text
        return text == "喝點飲料吧"
    
    def on_enter_choose_what_to_drink(self, event):
        situation[0] -= random.randint(1,10)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,10)
        msg = choose_what_to_drink()
        reply_token = event.reply_token
        send_another_message(reply_token, msg)
    
    def is_going_to_drink_water(self, event):
        text = event.message.text
        return text == "喝點水吧"
    
    def on_enter_drink_water(self, event):
        situation[0] -= random.randint(1,5)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,10)
        msg = drinking("water")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
    
    def is_going_to_drink_milktea(self, event):
        text = event.message.text
        return text == "喝奶茶好不好"
    
    def on_enter_drink_milktea(self, event):
        situation[0] -= random.randint(1,5)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,10)
        msg = drinking("milktea")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
    
    def is_going_to_drink_tea(self, event):
        text = event.message.text
        return text == "要不要來喝茶啊"
    
    def on_enter_drink_tea(self, event):
        situation[0] -= random.randint(1,5)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,10)
        msg = drinking("tea")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
    
    def is_going_to_wake(self, event):
        text = event.message.text
        return text == "起床囉"
    
    def on_enter_wake(self, event):
        situation[0] -= random.randint(1,10)
        situation[1] -= random.randint(1,10)
        situation[2] -= random.randint(1,20)
        msg = decision()
        msg += petfunction.go_to_wake()
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
    
    def is_going_to_sleep(self, event):
        text = event.message.text
        return text.lower() == "去睡覺吧~"
    
    def on_enter_sleep(self, event):
        situation[0] -= random.randint(1,30)
        situation[1] -= random.randint(1,30)
        situation[2] -= random.randint(1,10)
        msg = go_to_sleep()
        reply_token = event.reply_token
        send_another_message(reply_token, msg)
    
    def is_going_to_playing(self, event):
        text = event.message.text
        return text.lower() == "來玩點遊戲吧"
    
    def on_enter_playing(self, event):
        situation[0] -= random.randint(1,10)
        situation[1] -= random.randint(1,10)
        situation[2] -= random.randint(1,20)
        situation[3] -= random.randint(1,10)
        msg = choose_what_to_play()
        reply_token = event.reply_token
        send_another_message(reply_token, msg)
    
    def is_going_to_rps(self, event):
        text = event.message.text
        return text.lower() == "來猜拳吧"
    
    def on_enter_rps(self, event):
        situation[0] -= random.randint(1,10)
        situation[1] -= random.randint(1,10)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,10)
        msg = choose_what_to_shoot()
        reply_token = event.reply_token
        send_another_message(reply_token, msg)
        
    def is_going_to_shoot(self, event):
        text = event.message.text
        return ((text == "剪刀")|(text == "石頭")|(text == "布"))
    
    def on_enter_shoot(self, event):
        situation[0] -= random.randint(1,30)
        situation[1] -= random.randint(1,30)
        situation[2] -= random.randint(1,30)
        situation[3] -= random.randint(1,30)
        msg = shoot(event.message.text)
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
    
    def is_going_to_bas(self, event):
        text = event.message.text
        return text == "你來骰 我來猜大小"
    
    def on_enter_bas(self, event):
        situation[0] -= random.randint(1,5)
        situation[1] -= random.randint(1,5)
        situation[3] -= random.randint(1,5)
        msg = choose_what_to_guess()
        reply_token = event.reply_token
        send_another_message(reply_token, msg)
    
    def is_going_to_shake(self, event):
        text = event.message.text
        return (text == '大') | (text == '小') | (text == '豹子')
    
    def on_enter_shake(self, event):
        situation[0] -= random.randint(1,10)
        situation[1] -= random.randint(1,10)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,10)
        msg = shake(event.message.text)
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
        
    def is_going_to_be_company(self, event):
        text = event.message.text
        return text.lower() == "我們來找點有趣的吧"
    
    def on_enter_company(self, event):
        msg = company()
        reply_token = event.reply_token
        send_another_message(reply_token, msg)
    
    def is_going_to_YT(self, event):
        print("yt")
        text = event.message.text
        return text.lower() == "yt"
    
    def on_enter_YT(self, event):
        msg = "要看什麼呢"
        reply_token = event.reply_token
        print(msg)
        send_text_message(reply_token, msg)
        
    def is_going_to_search_YT(self, event):
        text = event.message.text
        print(text)
        return type(text) == str
    
    def on_enter_search_YT(self, event):
        situation[0] -= random.randint(1,10)
        situation[1] -= random.randint(1,20)
        situation[2] -= random.randint(1,10)
        situation[3] -= random.randint(1,10)
        situation[4] += random.randint(1,20)
        msg = youtube_video_parser(event.message.text)
        reply_token = event.reply_token
        line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None))
        line_bot_api.reply_message(reply_token,msg)
        self.go_back()
       


#==================================
#control pet's behavior
#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================
#===============library=============================================
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time as time
import schedule
import pandas as pd
import numpy as np
import matplotlib as plt
import random
from web_crawler import youtube_video_parser
#===============library=============================================

#now = datetime.datetime.now()
random.seed(time.time())
Types = ["food", "thirst", "happiness", "sleep", "exp"]
situation = [50,50,50,50,0]#food, drink, happiness, sleep, exp
motion = 0 #0 is wake, 1 is eating, 2 is drinking, 3 is sleepinc:\Users\0221p\Downloads\RNN_HW_(1).ipynbg, 4 is playing

def decision():
    message = TemplateSendMessage(
        alt_text='要做什麼',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="嗨嗨~~",
            text="要做什麼嗎",
            actions=[
                MessageTemplateAction(
                    label="顯示狀態",
                    text="顯示狀態"
                ),
                MessageTemplateAction(
                    label="互動",
                    text="在嗎"
                )
            ]
        )
    )
    return message


def show_situation():
    message = f'''飽食度：{situation[0]}
口渴值：{situation[1]}
幸福值：{situation[2]}
睡眠值：{situation[3]}
經驗值：{situation[4]}'''

    return message


def interaction():
    message = TemplateSendMessage(
        alt_text='要做什麼事呢',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(#food
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/3/3d/The_Kitchen_Nigeria.png',
                    title=f'飽食度：{situation[0]}',
                    text='要餵食請點擊按鈕',
                    actions=[
                        MessageTemplateAction(
                            label="吃東西",
                            text="吃東西吧",
                            data="feed"
                        )
                    ]
                ),
                CarouselColumn(#drink
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/8/82/Milktea_of_Shin-shin-do.jpg',
                    title=f'飲水度：{situation[1]}',
                    text='要不要喝水呢',
                    actions=[
                        MessageTemplateAction(
                            label='喝水',
                            text='喝點飲料吧',
                            data= 'drink'
                        )
                    ]
                ),
                CarouselColumn(#sleep
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/f/fa/Kitten_sleeping.jpg',
                    title=f'睡眠值：{situation[2]}',
                    text='要去睡覺嗎',
                    actions=[
                        MessageTemplateAction(
                            label='睡吧',
                            text='去睡覺吧~',
                            data = 'sleep'
                        )
                    ]
                ),
                CarouselColumn(#play
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/d/d9/Opening_chess_position_from_black_side.jpg',
                    title=f'幸福值：{situation[3]}',
                    text='玩遊戲嗎',
                    actions=[
                        MessageTemplateAction(
                            label='來玩遊戲吧',
                            text='來玩點遊戲吧',
                            data = 'play'
                        )
                    ]
                ),
                CarouselColumn(#study
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/c/c3/Red_Diamond_Play_Button.png',
                    title=f'經驗值：{situation[4]}',
                    text='來點什麼東西吧',
                    actions=[
                        MessageTemplateAction(
                            label='找點樂子',
                            text='我們來找點有趣的吧',
                            data = 'company'
                        )
                    ]
                )
            ]
        )
    )
    return message

def choose_what_to_eat():
    message = TemplateSendMessage(
        alt_text='要吃點什麼呢',
        template=ButtonsTemplate(
            thumbnail_image_url="https://upload.wikimedia.org/wikipedia/commons/3/3d/The_Kitchen_Nigeria.png",
            title="要吃哪一餐呢？",
            text="請點選哪一餐",
            actions=[
                PostbackTemplateAction(
                    label="早餐",
                    text="吃早餐",
                    data="eat breakfast"
                ),
                PostbackTemplateAction(
                    label="午餐",
                    text="吃午餐",
                    data="eat lunch"
                ),
                PostbackTemplateAction(
                    label="晚餐",
                    text="吃晚餐",
                    data="eat dinner"
                ),
                PostbackTemplateAction(
                    label="點心",
                    text="吃點心",
                    data="eat snack"
                ),
            ]
        )
    )
    return message

def eating(food):
    random.seed(time.time())
    message = ""
    count = random.randrange(0,2)
    if(situation[0] >= 80):
        message = "我現在還不想吃"
        return message
    else:
        match food:
            case "breakfast":
                msg = ["我要吃蛋餅~","我要吃吐司~","我吃漢堡~"]
                message = msg[count]
                match count:
                    case 0:
                        situation[0]+=30
                        situation[1]-=5
                    case 1:
                        situation[0]+=40
                        situation[1]-=5
                    case 2:
                        situation[0]+=50
                        situation[1]-=5
            case "lunch":
                msg = ["我要吃麥當勞~","我要吃鍋燒意麵~","我要吃便當~"]
                message = msg[count]
                match count:
                    case 0:
                        situation[0]+=30
                        situation[1]-=5
                    case 1:
                        situation[0]+=40
                    case 2:
                        situation[0]+=50
                        situation[1]-=5
            case "dinner":
                msg = ["我要吃麥當勞~","我要吃咖哩飯~","我要吃丼飯~"]
                message = msg[count]
                match count:
                    case 0:
                        situation[0]+=30
                        situation[1]-=5
                    case 1:
                        situation[0]+=40
                        situation[1]-=5
                    case 2:
                        situation[0]+=50
                        situation[1]-=5
            case "snack":
                msg = ["我要吃餅乾~","我要吃水果~","我要吃蛋糕~"]
                message = msg[count]
                match count:
                    case 0:
                        situation[0]+=20
                        situation[1]-=10
                    case 1:
                        situation[0]+=25
                        situation[1]+=5
                    case 2:
                        situation[0]+=35
                        situation[1]-=5
    print(message)
    return message
            
def choose_what_to_drink():
    message = TemplateSendMessage(
        alt_text='要喝什麼呢？',
        template=ButtonsTemplate(
            thumbnail_image_url="https://upload.wikimedia.org/wikipedia/commons/8/82/Milktea_of_Shin-shin-do.jpg",
            title="要喝什麼呢？",
            text="請點選要喝什麼",
            actions=[
                PostbackTemplateAction(
                    label="白開水",
                    text="喝點水吧",
                    data="water"
                ),
                PostbackTemplateAction(
                    label="奶茶",
                    text="喝奶茶好不好",
                    data='milktea'
                ),
                PostbackTemplateAction(
                    label="茶",
                    text="要不要來喝茶啊",
                    data='tea'
                ),
            ]
        )
    )
    return message

def drinking(beverage):
    message = ""
    match beverage:
        case "water":
            situation[1]+=30
            situation[2]-=5
            message = "怎麼是水啦 我想喝奶茶啦"
        case "milktea":
            situation[1]+=15
            situation[2]+=20
            message = "耶~~ 是我最喜歡的奶茶欸"
        case "tea":
            situation[1]+=20
            situation[2]+=5
            message = "只有茶嗎 我想加牛奶"
            
    return message

def go_to_sleep():
    message = TemplateSendMessage(
        alt_text='睡覺囉',
        template=ButtonsTemplate(
            text="睡就睡嘛 晚安\n 要叫我起床喔",
            actions=[
                PostbackTemplateAction(
                    label="起床",
                    text='起床囉',
                    data="wake"
                )
            ]
        )
    )
    return message

def go_to_wake():
    random.seed(time.time())
    situation[3] += random.randint(30,60)
    if situation[3]<=70:
        message = "還沒睡飽啦 幹嘛叫我起床"
    else:
        message = "早安啊~~~"
    return message

def choose_what_to_play():
    message = TemplateSendMessage(
        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/d/d9/Opening_chess_position_from_black_side.jpg',
        alt_text='要玩什麼呢？',
        template=ConfirmTemplate(
            text="要玩什麼呢？",
            actions=[
                PostbackTemplateAction(
                    label="猜拳",
                    text="來猜拳吧",
                    data="rps"
                ),
                PostbackTemplateAction(
                    label="猜大小",
                    text="你來骰 我來猜大小",
                    data='bigandsmall'
                )
            ]
        )
    )
    return message

def choose_what_to_shoot():
    message = TemplateSendMessage(
        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/d/d9/Opening_chess_position_from_black_side.jpg',
        alt_text='要玩什麼呢？',
        template=ButtonsTemplate(
            title = "好啊 來猜拳吧",
            text="剪刀石頭布？",
            actions=[
                PostbackTemplateAction(
                    label="剪刀",
                    text="剪刀",
                    data="scissors"
                ),
                PostbackTemplateAction(
                    label="石頭",
                    text="石頭",
                    data="stone"
                ),
                PostbackTemplateAction(
                    label="布",
                    text="布",
                    data='paper'
                )
            ]
        )
    )
    return message

def shoot(type):
    random.seed(time.time())
    shoot = random.randint(0,2)
    match type :
        case "石頭":
            type = 0
        case "剪刀":
            type = 1
        case "布":
            type = 2
            
    if(type == shoot):
        print(1111)
        msg = "even"
    elif(type == 0 and shoot == 1)or(type == 1 and shoot == 2)or(type == 2 and shoot == 0):
        print(2222)
        msg = "loss"
    else :
        print(3333)
        msg = "win"
        
    match shoot :
        case 0:
            message = "我出石頭"
        case 1:
            message = "我出剪刀"
        case 2:
            message = "我出布"
    
    match msg:
        case "loss":
            message += " 你贏了 你好壞QQ"
            situation[3]-= 5
        case "even":
            message += " 平手~"
            situation[3]+= 0
        case "win":
            message += " 我贏了 耶~~"
            situation[3]+= 15
    
    print(type)
    print(shoot)
    return message    

def choose_what_to_guess():
    message = TemplateSendMessage(
        alt_text='要猜什麼呢？',
        template=ButtonsTemplate(
            thumbnail_image_url="https://upload.wikimedia.org/wikipedia/commons/d/d2/Amusements_in_mathematics_-_A_Trick_with_Dice.png",
            text="要猜什麼呢？",
            actions=[
                PostbackTemplateAction(
                    label="大",
                    text='大',
                    data="big"
                ),
                PostbackTemplateAction(
                    label="小",
                    text='小',
                    data="small"
                ),
                PostbackTemplateAction(
                    label="豹子",
                    text='豹子',
                    data='even'
                )
            ]
        )
    )
    return message

def shake(guess):
    random.seed(time.time())
    if guess == '小':
        guess = 0
    elif guess == '大':
        guess = 1
    else:
        guess = 2
    
    print(guess)
    number1 = random.randint(1,6)
    number2 = random.randint(1,6)
    number3 = random.randint(1,6)
    message = f"點數是：{number1} {number2} {number3} \n"
    if ((number1+number2+number3)>=11 and guess == 1) or ((number1+number2+number3)<=10 and guess == 0) or ((number1 == number2 == number3) and guess == 2):
        print(number1+number2+number3)
        situation[3] -= 5
        message += "你贏了 可惡"
    else:
        print(number1+number2+number3)
        situation[3] += 15
        message += "耶 我贏了"
    return message

def company():
    situation[0] -= random.randint(1,10)
    situation[1] -= random.randint(1,10)
    situation[2] -= random.randint(1,10)
    situation[3] -= random.randint(1,10)
    situation[4] += random.randint(1,10)
    message = TemplateSendMessage(
        alt_text='要做什麼',
        template=ButtonsTemplate(
            thumbnail_image_url="https://upload.wikimedia.org/wikipedia/commons/c/c3/Red_Diamond_Play_Button.png",
            title="要看什麼嗎",
            text="點擊下面按鈕",
            actions=[
                MessageTemplateAction(
                    label="Youtube",
                    text="yt"
                )
            ]
        )
    )
    return message
    
#=============pet behavior====================
def job():
    print("do job")
    print(motion)
    if motion == 0: #wake
        situation[0] -= 10
        situation[1] -= 5
        situation[2] -= 5
        situation[3] -= 5
    if (motion == 1 | motion == 2): #eating and drinking 
        situation[0] -= 10
        situation[1] -= 10
        situation[2] -= 10
        situation[3] -= 5
    if motion == 3: #sleeping
        situation[0] -= 10
        situation[1] -= 5
        situation[2] += 15
        situation[3] -= 5
    if motion == 4: #playing
        situation[0] -= 20
        situation[1] -= 20
        situation[2] -= 20
        situation[3] += 30
        situation[4] += 5
        
scheduler = BackgroundScheduler(timezone="Asia/Shanghai")       
scheduler.add_job(job, 'interval', seconds=10)

if __name__ == "__main__":
    while time.localtime().tm_sec == 0:
        print(time.localtime().tm_sec)       
        job()

# while True:
#     for i in range(0,4):
#       print(situation[i])
#     time.sleep(11)
    
