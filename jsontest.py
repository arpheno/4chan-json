import json
import urllib2
import re
import sys

menu = {1: 'GRAB TOP THREAD FROM BOARD', 2: 'GET THREAD BY BOARD/INDEX'}

boards = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'gif', 'h', 'hr', 'k', 'm', 'o', 'p', 'r', 's',
		  't', 'u', 'v', 'vg', 'w', 'wg', 'i', 'ic', 'r9k', 'cm', 'hm', 'y', '3', 'adv', 'an',
		  'cgl', 'ck', 'co', 'diy', 'fa', 'fit', 'hc', 'int', 'jp', 'lit', 'mlp', 'mu', 'n',
		  'po', 'pol', 'sci', 'soc', 'sp', 'tg', 'toy', 'trv', 'tv', 'vp', 'wsg', 'x', 'rs']

htmlpattern = r'<.*?>'
urlpattern = r'\d{8}'

def select():
	return input("make a selection  ")

def get_input(subs):
	return input("enter %s: " % subs)

def validate_board(board):
	while board not in boards:
		print 'invalid selection'
		board = get_input("board")

def remove_html_tags(data):
	p = re.compile(htmlpattern)
	return p.sub('', data)

def remove_url_jumble(data):
	p = re.compile(urlpattern)
	threadnumber = re.match(p, data)
	print threadnumber
	return threadnumber

def replace_quote(data):
	return data.replace('&gt;', '>')

def replace_comma(data):
	return data.replace('&#44;', ',')

def grab_top_thread():
	board = get_input("board")

def get_thread():
	board = get_input("board")
	print "board is: /%s/" % board
	validate_board(board)
	thread = get_input("thread")
	threadToOpen = 'https://api.4chan.org/%s/res/%s.json' % (board, thread)

	print "trying to open " + threadToOpen
	jason = json.loads(urllib2.urlopen(threadToOpen).read())

	for i in range(len(jason['posts'])):
		currContent =  jason['posts'][i]['com'].replace('<br>', '\n')
		currContent = remove_html_tags(currContent)
		currContent = replace_comma(currContent)
		currContent = replace_quote(currContent)
		print currContent + '\n'

def get_board():
	board = get_input("board")
	print "board is: /%s/" % board
	validate_board(board)
	url = "http://boards.4chan.org/%s/" % board
	boardurl = urllib2.urlopen(url).read()
	threadnumber = remove_url_jumble(boardurl)

process = True

print menu.items()
selection = select()

while (selection not in menu):
	print 'invalid selection'
	print menu.items()
	selection = select()

if(selection == 1):
	get_board()
else:
	get_thread() 
st = wordList.replace('u\'', '')






