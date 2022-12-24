#control pet's behavior
#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================
#===============library=============================================
import datetime
import time as time
import schedule
import pandas as pd
import numpy as np
import matplotlib as plt
import random
#===============library=============================================

#now = datetime.datetime.now()
random.seed(time.time())
Types = ["food", "thirst", "happiness", "sleep", "exp"]
situation = [100,100,100,100,0]#food, drink, happiness, sleep, exp
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
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/5/54/Pictograms-nps-food_service.svg',
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
                    thumbnail_image_url='https://commons.wikimedia.org/wiki/File:Alcohol_glass_copper_mug.svg#/media/File:Alcohol_glass_copper_mug.svg',
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
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/e/e2/Sleep_thumbnail.png',
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
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/e/e2/Sleep_thumbnail.png',
                    title=f'幸福值：{situation[3]}',
                    text='玩遊戲嗎',
                    actions=[
                        MessageTemplateAction(
                            label='好啊',
                            text='來玩點遊戲吧',
                            data = 'play'
                        )
                    ]
                ),
                CarouselColumn(#study
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/e/e2/Sleep_thumbnail.png',
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
        alt_text='要做點什麼呢',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
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
                        situation[1]+=30
                        situation[1]+=5
                    case 2:
                        situation[2]+=35
                        situation[1]-=5
    print(message)
    return message
        
            
        
        
def choose_what_to_drink():
    message = TemplateSendMessage(
        alt_text='要喝什麼呢？',
        template=ConfirmTemplate(
            text="要喝什麼呢？",
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
    motion = 3
    message = "睡就睡嘛 晚安"
    return message

def go_to_wake():
    motion = 0
    message = "早安啊~~"
    return message

rps = 0
def choose_what_to_play():
    random.seed(time.time())
    motion = 4
    message = TemplateSendMessage(
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
                    label="1A2B",
                    text="玩1A2B吧 你來出題",
                    data='1A2B'
                )
            ]
        )
    )
    rps = random.randrange(0, 2)
    return message

def shoot(type):
    shoot = random.randint(0,2)
    match type :
        case "石頭":
            type = 0
        case "剪刀":
            type = 1
        case "布":
            type = 2
            
    if(type == 0 & rps == 1)|(type == 1 & rps == 2)|(type == 2 & rps == 0):
        msg = "loss"
    elif(type == rps):
        msg = "even"
    else :
        msg = "win"
        
    match rps :
        case 0:
            message = "我出石頭"
        case 1:
            message = "我出剪刀"
        case 2:
            message = "我出布"
    
    match msg:
        case "loss":
            message += "你贏了"
            situation[3]-= 5
        case "even":
            message += "平手~"
            situation[3]+= 0
        case "win":
            message += "我贏了 耶~~"
            situation[3]+= 5
            
    return message    
    
#=============pet behavior====================
def job():
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
        
        
schedule.every().hour.do(job)

# while True:
#     schedule.run_pending()
    
