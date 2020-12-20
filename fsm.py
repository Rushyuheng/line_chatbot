from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message

# golbal variable
totallist = []
tobuylist = []
newitem = ['','','','']
name = ''
unit = ''
number = 0
budget = 0
price = 0


class TocMachine(GraphMachine):
	def __init__(self, **machine_configs):
		self.machine = GraphMachine(model=self, **machine_configs)
	#user input anything to start
	def is_going_to_start(self,event):
		return True

	def on_enter_start(self,event):
		send_text_message(event.reply_token, '歡迎使用買菜助手,輸入『start』即可開始使用買菜助手。\n隨時輸入『restart』可以重新開始。\n隨時輸入『fsm』可以得到當下的狀態圖。')

	def is_going_to_makelist(self,event):
		text = event.message.text
		if text == 'start':
			return True
		else:
			return False

	def on_enter_makelist(self,event):
		#restart and clear list
		global totallist
		global tobuylist
		totalist.clear()
		tobuylist.clear()

		title = '請選擇新增購物清單或去購物'
		text = '新增項目至購物清單,若已新增完畢則選擇『去購物』'
		btn = [
			MessageTemplateAction(
				label = '新增項目',
				text ='新增項目'
			),
			MessageTemplateAction(
				label = '去購物',
				text = '去購物'
			),
		]
		url = 'https://i.imgur.com/d23V3Oy.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def is_going_to_shopping(self,event):
		text = event.message.text
		if text == '去購物':
			return True
		else:
			return False

	def on_enter_shopping(self,event):
		##TODO

	def is_going_to_newitemtolist(self,event):
		text = event.message.text
		if text == '新增項目':
			return True
		else:
			return False

	def on_enter_newitemtolist(self,event):
		send_text_message(event.reply_token, '請輸入要購買的項目名稱：')

	def is_going_to_inputitemname(self,event):
		text = event.message.text
		if not text: # not empty string
			name = text
			return True
		else:
			return False

	def on_enter_inputitemname(self,event):	
		title = '請選擇單位'
		text = '選擇物品單位'
		btn = [
			MessageTemplateAction(
				label = '公斤',
				text ='公斤'
			),
			MessageTemplateAction(
				label = '台斤',
				text = '台斤'
			),
			MessageTemplateAction(
				label = '公克',
				text = '公克'
			),
			MessageTemplateAction(
				label = '條',
				text = '條'
			),
			MessageTemplateAction(
				label = '顆',
				text = '顆'
			),

		]
		url = 'https://i.imgur.com/m51E7P5.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def is_going_to_chooseunit(self,event):
		text = event.message.text
		if text == '公斤' or text == '台斤' or text == '公克' or text == '條' or text == '顆': 
			unit = text
			return True
		else:
			return False

	def on_enter_chooseunit(self,event):
		send_text_message(event.reply_token, '請輸入數量（整數限定）：')

	def is_going_to_inputnumber(self,event):
		global number
		text = event.message.text
		if text.lower().isnumeric():
			number = int(text)
			return True
		return False
	def on_enter_inputnumber(self,event):
		send_text_message(event.reply_token, '請輸入預算（整數限定）：')

	def is_going_to_inputbudget(self,event):
		global budget
		text = event.message.text
		if text.lower().isnumeric():
			budget = int(text)
			return True
		return False

	def on_enter_inputbudget(self,event):
		global name
		global unit
		global number
		global budget
		global newitem
		newitem[0] = name
		newitem[1] = unit
		newitem[2] = number
		newitem[3] = budget

		title = '即將新增項目,請確認是否正確'
		text = '新增項目：' + name + '\n' + '數量：' + str(number) + unit + '\n' + '預算：' + str(budget) + '元'
		btn = [
			MessageTemplateAction(
				label = '確認新增',
				text ='確認新增'
			),
			MessageTemplateAction(
				label = '取消新增',
				text = '取消新增'
			),
		]
		url = 'https://i.imgur.com/fb1fQKX.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def confirm_add_item(self,event):
		global tobuylist
		global newitem
		if text == '確認新增': 
			tobuylist.append(newitem)
			return True
		elif text == '取消新增'
			#don't add item to list wait for next override
			return True
		else:
			return False

	def is_going_to_showlist(self,event):

	def on_enter_showlist(self,event):

	def back_to_shopping(self,event):

	def is_going_to_addnewbuyitem(self,event):

	def on_enter_addnewbuyitem(self,event):

	def is_going_to_buyitemname(self,event):

	def on_enter_buyitemname(self,event):

	def is_going_to_realexpense(self,event):

	def on_enter_realexpense(self,event):
	
	def check_and_goto_shopping(self,event):

	def is_going_to_endshopping(self,event):

	def on_enter_endshopping(self,event):

	def is_going_to_finishremind(self,event):

	def on_enter_finishremind(self,event):

	def overbudget(self,event):

	def on_enter_dangerous(self,event):

	def warning(self,event):

	def is_going_to_callNcheck(self,event):

	def on_enter_callNcheck(self,event):

	def is_going_to_goodend(self,event):

	def on_enter_goodend(self,event):


		

		

		

