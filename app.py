# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_button_message,send_image_message

load_dotenv()


machine = TocMachine(
	states=["user" ,"start" , "preparelist","makelist" ,"newitemtolist" ,"inputitemname" ,"chooseunit" ,"inputnumber","inputbudget" ,"showmakelist" , "shopping" ,"showlist" ,"addnewbuyitem" ,"buyitemname" ,"realexpense","check" ,"finishremind" ,"dangerousprice","dangerous" , "endshopping" ,"goodend" ,"callNcheck"],
	transitions=[
		# user to start
		{
			"trigger": "advance",
			"source": "user",
			"dest": "start",
			"conditions": "is_going_to_start",
		},

		# start to makelist
		{
			"trigger": "advance",
			"source": "start",
			"dest": "preparelist",
			"conditions": "is_going_to_preparelist",
		},

		# start to makelist
		{
			"trigger": "advance",
			"source": "preparelist",
			"dest": "makelist",
			"conditions": "is_going_to_makelist",
		},

		#makelist to shopping
		{
			"trigger": "advance",
			"source": "makelist",
			"dest": "shopping",
			"conditions": "is_going_to_shopping",
		},

		#cycle for adding new item
		{
			"trigger": "advance",
			"source": "makelist",
			"dest": "newitemtolist",
			"conditions": "is_going_to_newitemtolist",
		},

		{
			"trigger": "advance",
			"source": "newitemtolist",
			"dest": "inputitemname",
			"conditions": "is_going_to_inputitemname",
		},
		{
			"trigger": "advance",
			"source": "inputitemname",
			"dest": "chooseunit",
			"conditions": "is_going_to_chooseunit",
		},
		{
			"trigger": "advance",
			"source": "chooseunit",
			"dest": "inputnumber",
			"conditions": "is_going_to_inputnumber",
		},
		{
			"trigger": "advance",
			"source": "inputnumber",
			"dest": "inputbudget",
			"conditions": "is_going_to_inputbudget",
		},
		{
			"trigger": "advance",
			"source": "inputbudget",
			"dest": "makelist",
			"conditions": "confirm_add_item",
		},
		#end cycle

		#cycle of showmakelist
		{
			"trigger": "advance",
			"source": "makelist",
			"dest": "showmakelist",
			"conditions": "is_going_to_showmakelist",
		},
		{
			"trigger": "advance",
			"source": "showmakelist",
			"dest": "makelist",
			"conditions": "is_going_to_makelist",
		},
		#end cycle

		#show list cycle
		{
			"trigger": "advance",
			"source": "shopping",
			"dest": "showlist",
			"conditions": "is_going_to_showlist",
		},
		{
			"trigger": "advance",
			"source": "showlist",
			"dest": "shopping",
			"conditions": "back_to_shopping",
		},
		#end of cycle

		# add new buy item cycle
		{
			"trigger": "advance",
			"source": "shopping",
			"dest": "addnewbuyitem",
			"conditions": "is_going_to_addnewbuyitem",
		},
		{
			"trigger": "advance",
			"source": "addnewbuyitem",
			"dest": "buyitemname",
			"conditions": "is_going_to_buyitemname",
		},
		{
			"trigger": "advance",
			"source": "buyitemname",
			"dest": "realexpense",
			"conditions": "is_going_to_realexpense",
		},
		{
			"trigger": "advance",
			"source": "realexpense",
			"dest": "check",
			"conditions": "is_going_to_check",
		},
		{
			"trigger": "advance",
			"source": "check",
			"dest": "shopping",
			"conditions": "check_and_goto_shopping",
		},

		# end cycle
		
		#shopping to endshopping
		{
			"trigger": "advance",
			"source": "shopping",
			"dest": "endshopping",
			"conditions": "is_going_to_endshopping",
		},

		#check node
		{
			"trigger": "advance",
			"source": "check",
			"dest": "dangerous",
			"conditions": "listunmatch",
		},
		{
			"trigger": "advance",
			"source": "check",
			"dest": "dangerousprice",
			"conditions": "overbudget",
		},
		{
			"trigger": "advance",
			"source": "check",
			"dest": "finishremind",
			"conditions": "is_going_to_finishremind",
		},

		#end of node

		#finishremind node
		{
			"trigger": "advance",
			"source": "finishremind",
			"dest": "shopping",
			"conditions": "back_to_shopping",
		},
		{
			"trigger": "advance",
			"source": "finishremind",
			"dest": "endshopping",
			"conditions": "is_going_to_endshopping",
		},
		#end of node
		
		#endshopping node
		{
			"trigger": "advance",
			"source": "endshopping",
			"dest": "dangerous",
			"conditions": "warning",
		},

		{
			"trigger": "advance",
			"source": "endshopping",
			"dest": "goodend",
			"conditions": "is_going_to_goodend",
		},
		#end of node

		#dangerousprice to callNcheck
		{
			"trigger": "advance",
			"source": "dangerousprice",
			"dest": "callNcheck",
			"conditions": "is_going_to_callNcheck",
		},

		#dangerous to callNcheck
		{
			"trigger": "advance",
			"source": "dangerous",
			"dest": "callNcheck",
			"conditions": "is_going_to_callNcheck",
		},
		
		#callNcheck to shopping
		{
			"trigger": "advance",
			"source": "callNcheck",
			"dest": "shopping",
			"conditions": "back_to_shopping",
		},
		
		# restart
		{
			"trigger": "advance",
			"source": "goodend",
			"dest": "start",
			"conditions": "restart",
		},

		{	"trigger": "go_back",
			"source":["user" ,"start" , "makelist" ,"newitemtolist" ,"inputitemname" ,"chooseunit" ,"inputnumber","inputbudget" ,"showmakelist" , "shopping" ,"showlist" ,"addnewbuyitem" ,"buyitemname" ,"realexpense","check" ,"finishremind" ,"dangerousprice","dangerous" , "endshopping" ,"goodend" ,"callNcheck"],		
			"dest": "start"
		},
		
	],
	initial="user",
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

		##TODO
		response = machine.advance(event)
		if response == False:
			if event.message.text.lower() == 'fsm':
				send_image_message(event.reply_token, 'https://shopping-helper-toc.herokuapp.com/show-fsm')
			elif machine.state != 'user' and event.message.text.lower() == 'restart':
				send_text_message(event.reply_token, '輸入『start』即可開始使用買菜助手。\n隨時輸入『restart』可以重新開始。\n隨時輸入『fsm』可以得到狀態圖。')
				machine.go_back()
			else:
				send_text_message(event.reply_token, "我不了解你在說什麼,請再試一次")

	return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
	#machine.get_graph().draw("fsm.png", prog="dot", format="png")
	return send_file("./fsm.png", mimetype="image/png")


if __name__ == "__main__":
	port = os.environ['PORT']
	app.run(host="0.0.0.0", port=port, debug=True)
