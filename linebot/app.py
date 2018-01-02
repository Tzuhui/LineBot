from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)


line_bot_api = LineBotApi('grAy28hMhuIg0OjJKwgDN2Tc5QejSD5okD/xFv2sHbeAOlRmx57coV2fw/fGj8Emk7vy3OUIL33Q5wymN5ZEx78MrzNsYjyTKw0BDeHOxw4p9r39e/XW1nU4F45u007aS+VGxUsZPCTtPf350O13ZQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e6134a76f878184a9b6df80f6d2a9db3')

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    #print(type(msg))
    msg = msg.encode('utf-8')  
    if event.message.text == "文字":
        print("文字get")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
    elif event.message.text == "貼圖":
        print("貼圖get")
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
    elif event.message.text == "圖片":
        print("圖片get")
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://agirls.aotter.net/media/20f2a623-d960-4903-9e6c-1d809586785a.jpg', preview_image_url='https://agirls.aotter.net/media/20f2a623-d960-4903-9e6c-1d809586785a.jpg'))
    elif event.message.text == "影片":
        line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url='https://www.youtube.com/watch?v=aUiMaz4BNKw', preview_image_url='https://i.ytimg.com/vi/GNnM-LSa5OQ/maxresdefault.jpg'))
    elif event.message.text == "音訊":
        line_bot_api.reply_message(event.reply_token,AudioSendMessage(original_content_url='https://www.youtube.com/watch?v=aUiMaz4BNKw', duration=100000))
    elif event.message.text == "位置":
        print("位置get")
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='my location', address='Tainan', latitude=22.994821, longitude=120.196452))
    elif event.message.text == "樣板":
        print("TEST1")       
        buttons_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ButtonsTemplate(
            title='Template-樣板介紹',
            text='Template分為四種，也就是以下四種：',
            thumbnail_image_url='https://i.ytimg.com/vi/GNnM-LSa5OQ/maxresdefault.jpg',
            actions=[
                MessageTemplateAction(
                    label='Buttons Template',
                    text='Buttons Template'
                ),
                MessageTemplateAction(
                    label='Confirm template',
                    text='Confirm template'
                ),
                MessageTemplateAction(
                    label='Carousel template',
                    text='Carousel template'
                ),
                MessageTemplateAction(
                    label='Image Carousel',
                    text='Image Carousel'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif event.message.text == "Buttons Template":
        print("TEST")       
        buttons_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ButtonsTemplate(
            title='這是ButtonsTemplate',
            text='ButtonsTemplate可以傳送text,uri',
            thumbnail_image_url='https://i.ytimg.com/vi/GNnM-LSa5OQ/maxresdefault.jpg',
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='VIDEO1',
                    uri='https://www.youtube.com/watch?v=ty1NTsWOm0A'
                ),
                URITemplateAction(
                    label='VIDEO2',
                    uri='https://www.youtube.com/watch?v=GNnM-LSa5OQ'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif event.message.text == "Carousel template":
        print("Carousel template")       
        Carousel_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://3.bp.blogspot.com/-aRzn2Zvku0s/V2z8_bpnn3I/AAAAAAAAeFg/aCwg2FzpEmkRvFUtn0yWI_ATDZa2myzjACLcB/s1600/LINE%2B%25E7%2586%258A%25E5%25A4%25A7%25E8%25BE%25B2%25E5%25A0%25B4.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://prtimes.jp/i/1594/363/resize/d1594-363-949581-1.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='連結2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.message.text == "Confirm template":
        print("Confirm template")       
        Confirm_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ConfirmTemplate(
            title='這是ConfirmTemplate',
            text='這就是ConfirmTemplate,用於兩種按鈕選擇',
            actions=[                              
                MessageTemplateAction(
                    label='Y',
                    text='Y'
                ),
                MessageTemplateAction(
                    label='N',
                    text='N'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)
    elif event.message.text == "Image Carousel":
        print("Image Carousel")       
        Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://prtimes.jp/i/1594/363/resize/d1594-363-949581-1.jpg',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://3.bp.blogspot.com/-aRzn2Zvku0s/V2z8_bpnn3I/AAAAAAAAeFg/aCwg2FzpEmkRvFUtn0yWI_ATDZa2myzjACLcB/s1600/LINE%2B%25E7%2586%258A%25E5%25A4%25A7%25E8%25BE%25B2%25E5%25A0%25B4.jpg',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Image_Carousel)
    return 'OK2'

if __name__ == "__main__":
    app.run(debug=True,port=80)
