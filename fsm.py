from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

	def is_going_to_start(self,event):

	def on_enter_start(self,event):
		
	def is_going_to_makelist(self,event):

	def on_enter_makelist(self,event):

	def is_going_to_shopping(self,event):

	def on_enter_shopping(self,event):

	def is_going_to_newitemtolist(self,event):

	def on_enter_newitemtolist(self,event):

	def is_going_to_inputitemname(self,event):

	def on_enter_inputitemname(self,event):

	def is_going_to_chooseunit(self,event):

	def on_enter_chooseunit(self,event):

	def is_going_to_inputnumber(self,event):

	def on_enter_inputnumber(self,event):

	def is_going_to_inputbudget(self,event):

	def on_enter_inputbudget(self,event):

	def confirm_add_item(self,event):

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


		

		

		

