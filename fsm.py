from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message
from linebot.models import MessageTemplateAction
# golbal variable
extralist = []
tobuylist = []
newitem = ['','',0,0]
newbuyitem = ['',0]
name = ''
unit = ''
number = 0
budget = 0
price = 0
buyextra = False

class TocMachine(GraphMachine):
	def __init__(self, **machine_configs):
		self.machine = GraphMachine(model=self, **machine_configs)
	#user input anything to start
	def is_going_to_start(self,event):
		return True

	def on_enter_start(self,event):
		#restart and clear list
		global extralist
		global tobuylist
		extralist.clear()
		tobuylist.clear()
		send_text_message(event.reply_token, '歡迎使用採購小幫手,輸入『start』即可開始。\n隨時輸入『restart』可以重新開始。\n隨時輸入『fsm』可以得到狀態圖。')

	def is_going_to_makelist(self,event):
		text = event.message.text
		if text == 'start' or text == 'back':
			return True
		else:
			return False

	def is_going_to_preparelist(self,event):
		text = event.message.text
		if text == 'gogo':
			return True
		else:
			return False

	def on_enter_preparelist(self,event):
 		send_text_message(event.reply_token, 'welcome enter \'start\' to continue')
	   
	def on_enter_makelist(self,event):
		title = '請選擇新增購物清單、檢視清單或去購物'
		text = '新增項目至購物清單,若已新增完畢則選擇『去購物』'
		btn = [
			MessageTemplateAction(
				label = '新增項目',
				text ='新增項目'
			),
			MessageTemplateAction(
				label = '檢視清單',
				text = '檢視清單'
			),
			MessageTemplateAction(
				label = '去購物',
				text = '去購物'
			),
		]
		url = 'https://i.imgur.com/m7S2P3t.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def is_going_to_showmakelist(self,event):
		text = event.message.text
		if text == '檢視清單':
			return True
		else:
			return False

	def on_enter_showmakelist(self,event):
		global tobuylist
		replytext = '清單內容：\n名稱  數量  預算  \n'
		for item in tobuylist:
			replytext += item[0] + ' ' + str(item[2]) + ' ' + item[1] + ' ' + str(item[3]) + '元\n'
		replytext +='輸入『back』以結束檢視清單'
		send_text_message(event.reply_token, replytext)

	def is_going_to_shopping(self,event):
		text = event.message.text
		if text == '去購物':
			return True
		else:
			return False

	def on_enter_shopping(self,event):
		title = '請選擇新增已買物品、檢視清單或結束購物'
		text = '新增項目至已買清單,若購物完畢則選擇『結束購物』'
		btn = [
			MessageTemplateAction(
				label = '新增已買項目',
				text ='新增已買項目'
			),
			MessageTemplateAction(
				label = '檢視清單',
				text = '檢視清單'
			),
			MessageTemplateAction(
				label = '結束購物',
				text = '結束購物'
			),
		]
		url = 'https://i.imgur.com/a0FOukY.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def is_going_to_newitemtolist(self,event):
		text = event.message.text
		if text == '新增項目':
			return True
		else:
			return False

	def on_enter_newitemtolist(self,event):
		send_text_message(event.reply_token, '請輸入要購買的項目名稱：')

	def is_going_to_inputitemname(self,event):
		global name
		text = event.message.text
		if text != '': # not empty string
			text = text.replace(' ','')# remove blank
			name = text
			return True
		else:
			return False

	def on_enter_inputitemname(self,event):	
		title = '請選擇單位'
		text = '選擇物品單位'
		btn = [
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
		url = 'https://i.imgur.com/yj8WSSL.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def is_going_to_chooseunit(self,event):
		global unit
		text = event.message.text
		if text == '台斤' or text == '公克' or text == '條' or text == '顆': 
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
		url = 'https://i.imgur.com/6IRRt2s.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def confirm_add_item(self,event):
		global tobuylist
		global newitem
		text = event.message.text
		if text == '確認新增':
			tobuylist.append(newitem[:]) #pass by value not reference
			return True
		elif text == '取消新增':
			#don't add item to list wait for next override
			return True
		else:
			return False
		
	def is_going_to_showlist(self,event):
		text = event.message.text
		if text == '檢視清單': 
			return True
		else:
			return False

	def on_enter_showlist(self,event):
		global tobuylist
		global extralist
		replytext = ''
		if tobuylist:
			replytext += '清單尚餘：\n名稱  數量  預算  \n'
			for item in tobuylist:
				replytext += item[0] + ' ' + str(item[2]) + ' ' + item[1] + ' ' + str(item[3]) + '元\n'

		if extralist:
			replytext += '額外購買：\n名稱  金額  \n'
			for item in extralist:
				replytext += item[0] + ' ' + str(item[1]) + '元\n'

		if not extralist and not tobuylist:
			replytext += '清單已空\n請輸入『back』後選擇結束購物\n'
		replytext +='輸入『back』以結束檢視清單'
		send_text_message(event.reply_token, replytext)

	def back_to_shopping(self,event):
		text = event.message.text
		if text == '繼續購物' or text == 'back': 
			return True
		else:
			return False

	def is_going_to_addnewbuyitem(self,event):
		text = event.message.text
		if text == '新增已買項目': 
			return True
		else:
			return False
	
	def on_enter_addnewbuyitem(self,event):
		send_text_message(event.reply_token, '請輸入已購買的項目名稱：')

	def is_going_to_buyitemname(self,event):
		global name
		text = event.message.text
		if text != '': # not empty string
			text = text.replace(' ','')# remove blank
			name = text
			return True
		else:
			return False

	def on_enter_buyitemname(self,event):
		send_text_message(event.reply_token, '請輸入實際花費（整數限定）：')
	def is_going_to_realexpense(self,event):
		global price
		text = event.message.text
		if text.lower().isnumeric():
			price = int(text)
			return True
		return False

	def on_enter_realexpense(self,event):
		global name
		global price
		global newbuyitem
		newbuyitem[0] = name
		newbuyitem[1] = price

		title = '即將新增已購買項目,請確認是否正確'
		text = '已購買項目：' + name + '\n' + '實際金額：' + str(price) + '元'
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
		url = 'https://i.imgur.com/6IRRt2s.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def is_going_to_check(self,event):
		global tobuylist
		global extralist
		global newbuyitem
		global newitem
		global buyextra

		text = event.message.text
		flag = False
		i = 0

		if text == '確認新增':
			i = 0
			for item in tobuylist:
				if item[0] == newbuyitem[0]:#find match in tobuylist
					newitem = item # copy it before pop for later use
					flag = True
					break
				i += 1
			if flag:
				tobuylist.pop(i) # pop item in list
				buyextra = False
			else:
				extralist.append(newbuyitem[:]) #add item to extra list
				buyextra = True
			return True
		elif text == '取消新增':
			#do nothing
			buyextra = False
			return True
		else:
			return False
	def on_enter_check(self,event):
		title = '選擇檢查以確認是否仍有項目需購賣'
		text = '如果購物清單尚未完成會自動進入購物模式，請選擇查看清單以確認尚缺哪些項目'
		btn = [
			MessageTemplateAction(
				label = '檢查',
				text ='檢查'
			),
		]
		url = 'https://i.imgur.com/VWYK4JJ.png'
		send_button_message(event.reply_token, title, text, btn, url)
	def check_and_goto_shopping(self,event):
		global tobuylist
		global buyextra

		text = event.message.text
		if text == '檢查' and tobuylist and not buyextra and newbuyitem[1] <= newitem[3] * 1.5: 
			return True
		else:
			return False

	def is_going_to_endshopping(self,event):
		text = event.message.text
		if text == '結束購物': 
			return True
		else:
			return False

	def on_enter_endshopping(self,event):
		title = '選擇結算以確認清單是否完全符合'
		text = '超買或缺買都有被念的風險喔！'
		btn = [
			MessageTemplateAction(
				label = '結算',
				text = '結算'
			),
		]
		url = 'https://i.imgur.com/VWYK4JJ.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def is_going_to_finishremind(self,event):
		global tobuylist
		global buyextra

		text = event.message.text
		if text == '檢查' and not tobuylist and not buyextra and newbuyitem[1] <= newitem[3] * 1.5: 
			return True
		else:
			return False
	def on_enter_finishremind(self,event):
		title = '完成採購購物清單內容，選擇繼續購物或是結束購物'
		text = '注意繼續購物小心不要超買太多以免回去挨念喔'
		btn = [
			MessageTemplateAction(
				label = '結束購物',
				text ='結束購物'
			),
			MessageTemplateAction(
				label = '繼續購物',
				text ='繼續購物'
			),
		]
		url = 'https://i.imgur.com/nKh2NYg.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def overbudget(self,event):
		global tobuylist
		global buyextra
		text = event.message.text
		if text == '檢查' and not buyextra and newbuyitem[1] >= newitem[3] * 1.5: 
			return True
		else:
			return False

	def on_enter_dangerous(self,event):
		send_text_message(event.reply_token, '購物內容與購物清單不吻合\n可能有超買或缺買的情形\n建議致電皇太后詢問指示以免挨念\n閱讀後請輸入『我知道了』代表您已了解風險')

	def warning(self,event):
		global tobuylist
		global extralist
		text = event.message.text
		if text == '結算' and (extralist or tobuylist): 
			return True
		else:
			return False

	def on_enter_dangerousprice(self,event):
		global newbuyitem
		global newitem
		sendtext = '實際消費已超過預算的1.5倍\n' + '物品內容：' + newbuyitem[0] + '\n' + '預算：' + str(newitem[3]) + '\n' +'實際金額：' + str(newbuyitem[1]) + '\n' +'建議致電皇太后詢問指示以免挨念\n閱讀後請輸入『我知道了』代表您已了解風險'
		send_text_message(event.reply_token,sendtext) 

	def listunmatch(self,event):
		text = event.message.text
		if text == '檢查' and buyextra: #add a extra item  
			return True
		else:
			return False

	def is_going_to_callNcheck(self,event):
		text = event.message.text
		if text == '我知道了':  
			return True
		else:
			return False

	def on_enter_callNcheck(self,event):
		title = '致電皇太后尋求指示後選擇繼續購物'
		text = '強烈建議致電詢問，自作主張有高機率回去挨念喔'
		btn = [
			MessageTemplateAction(
				label = '繼續購物',
				text ='繼續購物'
			),
		]
		url = 'https://i.imgur.com/JIwdwBR.png'
		send_button_message(event.reply_token, title, text, btn, url)

	def is_going_to_goodend(self,event):
		text = event.message.text
		if text == '結算' and not extralist and not tobuylist : #no extra item and tobuylist is empty
			return True
		else:
			return False

	def on_enter_goodend(self,event):
		send_text_message(event.reply_token, '已採購完成清單項目，感謝您使用採購小幫手，希望您今日有個不挨念美好的一天\n輸入『restart』以重新開始')	
	def restart(self,event):
		text = event.message.text
		if text == 'restart':
			return True
		else:
			return False
