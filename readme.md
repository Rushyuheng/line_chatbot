# Shopping-helper-toc

## Motivation
In my family, my Dad is ususally the one who go to traditional market and do the shopping while, My Mom will give him some instruction, wait for all ingredients brought back by my Dad and she will do the cooking.  
It seems like a reasonable way to share houseworks, however, my Dad and Mom sometimes start a argument due to the mismatch of my Mom's expectation and the ingredients brought back by my Dad.
They are several reason:  
* My Dad forget to buy somthing
* My Dad spent too much or buy too much on certain item
* My Mom thinks that she did ask my Dad to buy something but actually not
* My Dad buy some extra items which he think my Mom needed but actually not  

To deal with the problems mentioned above, I made a shopping helper chatbot, it can be used as a shopping list but with extra reminding mechanisim and auto comparsion with the shopping list and what is actually bought.

## Quick start
1. download Line in Google Play or Apple Store
2. Scan this QR code!  
![](https://i.imgur.com/aU2fCYc.png)
3. Add bot as friend
4. start playing with it

## Function and User Guides
1. Enter anything to wakeup the bot  
2. Make your own shopping list
3. Enter food name, unit, number and your budget
4. Start shopping
5. Check the list whenever you want during shopping
7. If you buy some stuff,enter it to your list
8. Bot will check if the item match with the list or over 1.5 times than your budget
9. Bot send you warning if overbudget or buy extra item which is not on the list
10. Bot remind you to call and check helping you to get away for possible blaming
11. Bot auto delete the item you already bought ont the list and record the extra you bought
12. If the shopping list is completed, bot will remind you and you can go home happily
13. Enter "restart" to restart anytime and "fsm" to get currrent state diagram 

## FSM
![](https://i.imgur.com/fWK85Ap.png)

## About development
### Prerequisite
* Python 3.6
* Pipenv
* Line developer
* HTTPS Server

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)


**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py

## Deploy
Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku
1. Register Heroku: https://signup.heroku.com
2. Create Heroku project from website
3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

	refference: https://hackmd.io/@ccw/B1Xw7E8kN?type=view#Q2-如何在-Heroku-使用-pygraphviz

## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)  
[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)  
Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)  
[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)  
[transition](https://github.com/pytransitions/transitions)  
[line message API](https://developers.line.biz/en/docs/messaging-api/)  
[code tracing](https://github.com/aqwefghnm/LineChatBot)  
[requirement](https://docs.google.com/presentation/d/e/2PACX-1vThBHTe2iRVzvead5tBeqnshkhmE61j13rMOs8iwzGgodWheJNlOntg7hXuSlMEY-Ek1l7XA1rzM-xK/pub?start=false&loop=false&delayms=3000&slide=id.p1)