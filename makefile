#infinite chill / 2017
all: emoji-bot

emoji-bot: emoji-bot.py
	cp emoji-bot.py emoji-bot
	chmod u+x emoji-bot

run:
	./emoji-bot

clean:
	rm -f emoji-bot
