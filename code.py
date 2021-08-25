import pygame
import random
import time

pygame.init()
pygame.font.init()
colour = [0,50,20]
screen = pygame.display.set_mode([900,700])
screen.fill([0,50,20])
pygame.display.flip()
clock_tick_rate = 20
dead = False
clock = pygame.time.Clock()
iterate = 0
lis=[8,10,8,8,8,8,8,8,8,8,8,8,13,20,25,32]
ch=random.choice(lis)

class button:
	def __init__(self,text):
		self.x = 750
		self.y = 550
		self.txt=text
		self.width=80
		self.height=30
	def displaybutton(self):
		butt = pygame.draw.rect(screen,(0,0,0),(self.x-2,self.y-2,self.width+4,self.height+4))
		but = pygame.draw.rect(screen,(245,245,245),(self.x,self.y,self.width,self.height))
		font = pygame.font.SysFont('Arial Black MS', 19)
		text = font.render(self.txt, True, [0,0,0],[245,245,245])
		d = text.get_rect()
		d.centerx = self.x+self.width/2
		d.centery=self.y+self.height/2
		d.width = self.width
		d.height = self.height-20
		screen.blit(text, d)
		pygame.display.update()
	def clickedbutton(self,pos_x,pos_y):
		if pos_x>self.x and pos_x<self.x+self.width and pos_y>self.y and pos_y<self.y+self.height:
			return 1
		else :
			return 0

u=[]
c=[]
count = 0
cardback = pygame.image.load('assets/peeche.png')
usercards=[]
compcards=[]
discardpile=[]
deck=[]
jugaad=[]
deckcoordinates=[[250,280],[252,280],[254,280],[256,280],[258,280],[260,280]]
cards = ['assets/AC.png','assets/AD.png','assets/AH.png','assets/AS.png','assets/2C.png','assets/2D.png','assets/2H.png','assets/2S.png','assets/3C.png','assets/3D.png','assets/3H.png','assets/3S.png','assets/4C.png','assets/4D.png','assets/4H.png','assets/4S.png','assets/5C.png','5D.png','assets/5H.png','assets/5S.png','assets/6C.png','assets/6D.png','assets/6H.png','assets/6S.png','assets/7C.png','assets/7D.png','assets/7H.png','assets/7S.png','assets/8C.png','assets/8D.png','assets/8H.png','assets/8S.png','assets/9C.png','assets/9D.png','assets/9H.png','assets/9S.png','assets/10C.png','assets/10D.png','assets/10H.png','assets/10S.png','assets/KC.png','assets/KD.png','assets/KH.png','assets/KS.png','assets/QC.png','assets/QD.png','assets/QH.png','assets/QS.png','assets/JC.png','assets/JD.png','assets/JH.png','assets/JS.png','assets/AC.png','assets/AD.png','assets/AH.png','assets/AS.png','assets/2C.png','assets/2D.png','assets/2H.png','assets/2S.png','assets/3C.png','assets/3D.png','assets/3H.png','assets/3S.png','assets/4C.png','assets/4D.png','assets/4H.png','assets/4S.png','assets/5C.png','assets/5D.png','assets/5H.png','assets/5S.png','assets/6C.png','assets/6D.png','assets/6H.png','assets/6S.png','assets/7C.png','assets/7D.png','assets/7H.png','assets/7S.png','assets/8C.png','assets/8D.png','assets/8H.png','assets/8S.png','assets/9C.png','assets/9D.png','assets/9H.png','assets/9S.png','assets/10C.png','assets/10D.png','assets/10H.png','assets/10S.png','assets/KC.png','assets/KD.png','assets/KH.png','assets/KS.png','assets/QC.png','assets/QD.png','assets/QH.png','assets/QS.png','assets/JC.png','assets/JD.png','assets/JH.png','assets/JS.png']
joker=cards[random.randint(0,83)]
 

def shuffle():
	global usercards
	global compcards
	global discardpile
	global deck
	while(len(usercards))<10:
		rn= random.randint(0,51)
		if usercards.count(cards[rn])+compcards.count(cards[rn]) <2:
			usercards.append(cards[rn])
	while(len(compcards))<10:
		rad = random.randint(0,51)
		if usercards.count(cards[rad])+compcards.count(cards[rad]) <2:
			compcards.append(cards[rad])
			jugaad.append(cards[rad][0:2])
	for i in range(104):
		if usercards.count(cards[i])+compcards.count(cards[i])+deck.count(cards[i])<2:
			deck.append(cards[i])
	print(usercards, compcards, deck, len(deck))

def coordinates():
	xu=100
	yu=500
	xc=100
	yc=70
	global u
	global c
	for i in range(len(usercards)):
		u.append([xu,yu])
		c.append([xc,yc])
		xu+=50
		xc+=50
	print(len(c))

def carduser():
	global usercards
	for i in range(len(u)):
		screen.blit(pygame.transform.scale(pygame.image.load(usercards[i]), (100,150)), u[i])
def cardcomp():
	global cardcomp
	for i in range(len(compcards)):
		screen.blit(pygame.transform.scale(cardback, (100,150)), c[i])
def deckmanip():
	global discardpile
	global deck
	for i in deckcoordinates:
		screen.blit(pygame.transform.scale(cardback, (100,150)),i)
	screen.blit(pygame.transform.scale(pygame.image.load(discardpile[-1]),(100,150)),[450,280])
def reset():
	global u
	u=[]
	screen.fill([0,50,20])
	coordinates()
	print(u)
def discardedcard(i,j=0):
	discardpile.append(usercards[i])
	usercards.remove(usercards[i])
	u.remove(u[i])
	reset()
	carduser()
	cardcomp()
	deckmanip()
	if j==1:
		discardpile.append('assets/peeche.png')
		screen.blit(pygame.transform.scale(pygame.image.load('assets/peeche.png'),(100,150)),[450,280])

def clickedimage(x,y):
	#groupedcards(meld,0)
	displaygroups(meld)
	pygame.display.update()
	for i in range(len(usercards)-1):
		if x>u[i][0] and x<u[i+1][0] and y>500 and y<700 and u[i][1]>460:
			groupedcards(meld,0)
			reset()
			u[i][1]-=40
			carduser()
			deckmanip()
			cardcomp()
			displaygroups(meld)
			pygame.display.update()
			return(1,i)
		elif x>u[-1][0] and x<100+u[-1][0] and y>500 and y<700 and u[-1][1]>460:
			groupedcards(meld,0)
			reset()
			u[-1][1]-=40
			carduser()
			deckmanip()
			cardcomp()
			displaygroups(meld)
			pygame.display.update()
			return(1,len(usercards)-1)
def selectcard(x,y):
	global count
	if (x>249 and x<358):
		k = random.randint(0,len(deck)-1)
		usercards.append(deck[k])
		u.append([u[-1][0]+50,u[-1][1]])
		deck.remove(deck[k])
		carduser()
		cardcomp()
		deckmanip()
		return 1
	if(x>452 and x<550) and len(discardpile)>1:
		print(discardpile)
		usercards.append(discardpile[-1])
		u.append([u[-1][0]+50,u[-1][1]])
		discardpile.pop()
		carduser()
		cardcomp()
		deckmanip()
		return 1
	else:
		count=0


four=0
meld=[]

def printonlyuser():
	reset()
	usercards()

def computersturntoselect():
	global c
	d=discardpile[-1]
	after=0
	before=0
	index=cards.index(d)  
	if index > 0 and index <102:
		after=cards[index+1] 
		before=cards[index-1]
		if (after in compcards and before in compcards and len(discardpile)>1) or discardpile[-1]==joker:
			compcards.append(discardpile[-1])
			c.append([c[-1][0]+50,c[-1][1]])
			discardpile.pop()
			c=c[0:len(compcards)]
			print("COMPS TURN", len(c))
			reset()
			carduser()
			cardcomp()
			deckmanip()
			return
		else:
			k = random.randint(0,len(deck)-1)
			compcards.append(deck[k])
			c.append([c[-1][0]+50,c[-1][1]])
			deck.remove(deck[k])
			c=c[0:len(compcards)]
			print("COMPS TURN", len(c))
			reset()
			carduser()
			cardcomp()
			deckmanip()
			return
def computersturntothrow():
	global c
	compcards.sort()
	discardpile.append(compcards[-1])
	compcards.pop()
	c=c[0:len(compcards)]
	reset()
	carduser()
	cardcomp()
	deckmanip()

def computersturntoshow():
	global iterate
	global ch
	if ch == iterate:
		return 1

def groupedcards(gp,k=1):
	if(k==1):
		reset()
		carduser()
		cardcomp()
		deckmanip()
	cx=600
	cy=500
	j=0
	for i in gp:
		j+=1
		screen.blit(pygame.transform.scale(pygame.image.load(i[-1]),(100,150)),[cx-(j*20),500])
	pygame.display.update()
def displaygroups(gp):
	cx=600
	cy=500
	j=0
	for i in gp:
		j+=1
		screen.blit(pygame.transform.scale(pygame.image.load(i[-1]),(100,150)),[cx-(j*20),500])
	pygame.display.update()

def sortswap(gp):
	print(usercards)
	for i in gp[-1]:
		ind = usercards.index(i)
		print(ind)
		usercards.remove(usercards[ind])
		u.remove(u[ind])
		carduser()
		cardcomp()
		deckmanip()
	groupedcards(gp)
def showwinlose():
	reset()
	font = pygame.font.SysFont('Arial Black MS', 40)
	text = font.render('CALCULATING SCORE', True, [245,245,245],[0,50,20])
	textRect = text.get_rect()
	textRect.centerx = 450
	textRect.centery= 350
	screen.blit(text,textRect)
	pygame.display.update()
	time.sleep(3)
	r = random.choice([0,1])
	if r == 0:
		reset()
		font = pygame.font.SysFont('Arial Black MS', 40)
		text = font.render('YOU WIN!', True, [245,245,245],[0,50,20])
		textRect = text.get_rect()
		textRect.centerx = 450
		textRect.centery= 350
		screen.blit(text,textRect)
		pygame.display.update()
		time.sleep(5)
		exit()
	if r == 1:
		reset()
		font = pygame.font.SysFont('Arial Black MS', 40)
		text = font.render('YOU LOSE!', True, [245,245,245],[0,50,20])
		textRect = text.get_rect()
		textRect.centerx = 450
		textRect.centery= 350
		screen.blit(text,textRect)
		pygame.display.update()	
		time.sleep(5)
		exit()	

def showtext(texts):
	font = pygame.font.SysFont('Arial Black MS', 20)
	text = font.render(texts, True, [245,245,245],[0,50,20])
	textRect = text.get_rect()
	textRect.centerx = 400
	textRect.centery= 680
	screen.blit(text,textRect)
	pygame.display.update()
def makerectangle():

	font = pygame.font.SysFont('Arial Black MS', 20)
	text = font.render('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', True, [0,50,20],[0,50,20])
	textRect = text.get_rect()
	textRect.centerx = 400
	textRect.centery= 680
	screen.blit(text,textRect)
	pygame.display.update()
def calculatescore():
	scl=[0,0,0,1]
	ch=random.choice(scl)
	reset()
	font = pygame.font.SysFont('Arial Black MS', 40)
	text = font.render('CALCULATING SCORE', True, [245,245,245],[0,50,20])
	textRect = text.get_rect()
	textRect.centerx = 450
	textRect.centery= 350
	screen.blit(text,textRect)
	pygame.display.update()
	time.sleep(3)
	if ch == 0:
		reset()
		font = pygame.font.SysFont('Arial Black MS', 40)
		text = font.render('YOU LOSE', True, [245,245,245],[0,50,20])
		textRect = text.get_rect()
		textRect.centerx = 450
		textRect.centery= 350
		screen.blit(text,textRect)
		pygame.display.update()
		time.sleep(5)
		exit()
	if ch==1:
		reset()
		font = pygame.font.SysFont('Arial Black MS', 40)
		text = font.render('YOU WIN!', True, [245,245,245],[0,50,20])
		textRect = text.get_rect()
		textRect.centerx = 450
		textRect.centery= 350
		screen.blit(text,textRect)
		pygame.display.update()
		time.sleep(5)
		exit()

shuffle()
coordinates()
carduser()
cardcomp()
discardpile.append(deck[random.randint(0,83)])
print(discardpile)
deck.remove(discardpile[0])
deckmanip()
z = 0
grouping=[]
counter =0
pygame.display.update()
start=0
while(dead==False):
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			dead = True
			break
		print(count)
		if count == 0:
			reset()
			carduser()
			cardcomp()
			deckmanip()
			makerectangle()
			if start==0:
				showtext('Choose a card from the deck')
			else:
				makerectangle()
				showtext('Choose a card from the deck or discard pile')
		if event.type == pygame.MOUSEBUTTONDOWN and count ==0:
			x,y = event.pos
			print(x,y)
			if (y>281 and y<432) and ((x>249 and x<358) or (x>452 and x<550)) and len(usercards)<11:
				k = selectcard(x,y)
				if k == 1:
					pygame.display.update()
					count+=1 
					start+=1
					iterate+=1
					showbutton = button('SHOW')
					showbutton.displaybutton()
					showtext('Click on a card from your deck to discard it or click on show to group and show your cards')
			else:
				count = 0
				
		if count == 1:
			makerectangle()
			showtext('Click on a card from your deck to discard it or make a show')
		if event.type == pygame.MOUSEBUTTONDOWN and count==1:
			
			x,y = event.pos
			print(event.pos)
			p=[2500,2500]
			showbutton = button('SHOW')
			showbutton.displaybutton()
			if not ((x<102 or x>646) or (y>648 or y<502)):
				print(x,y)
				p=clickedimage(x,y)
				crd=p[0]
				selected=p[1]
				pygame.display.update()
				time.sleep(0.5)
				discardedcard(selected)
				pygame.display.update()
				count+=1
				time.sleep(1)
			if showbutton.clickedbutton(x,y)==1:
				count = -1
		if count==2:
			makerectangle()
			showtext("Joe's turn")
		if count==-1 and counter==0:
			makerectangle()
			showtext("Select a card to show")
		if count==-1 and counter!=0:
			makerectangle()
			showtext("Select 3 cards to group. If you're left with only a single card, click on it to show results")
		if event.type == pygame.MOUSEBUTTONDOWN and count == -1:

			if counter == 0:
				x,y = event.pos
				print(event.pos)
				p=[2500,2500]

				if not ((x<102 or x>646) or (y>648 or y<502)):
					print(x,y)
					p=clickedimage(x,y)
					crd=p[0]
					selected=p[1]
					pygame.display.update()
					time.sleep(0.5)
					discardedcard(selected,1)
					coordinates()
					pygame.display.update()
					counter = 1

			else:
				x,y = event.pos
				print(event.pos)
				p=[2500,2500]
				if (len(usercards)==1):
					if counter==100:
						calculatescore()
					else:
						showwinlose()
				if not ((x<102 or x>646) or (y>648 or y<502)) and len(usercards)>1:
					print(x,y)
					groupedcards(meld)
					pygame.display.update()
					p=clickedimage(x,y)
					groupedcards(meld)
					pygame.display.update()	
					crd=p[0]
					selected=p[1]
					pygame.display.update()
					time.sleep(0.5)
					
					if len(grouping)<3:
						grouping.append(usercards[selected])
						print(grouping)
					if len (grouping)==3:
						print(grouping)
						count = -2
						meld.append(grouping)
					if len(grouping)>3:
						grouping=[]
						grouping.append(usercards[selected])
					pygame.display.update()
		if event.type == pygame.MOUSEBUTTONDOWN and count==-2:
			x,y = event.pos
			groupbutton = button('GROUP')
			groupbutton.displaybutton()
			g=groupbutton.clickedbutton(x,y) 
			print(g)
			if g == 1:
				print(grouping)
				sortswap(meld)
				print(meld)
				pygame.display.update()
				time.sleep(0.5)
				count=-1
				grouping=[]
		if count==2:
			computersturntoselect()
			c=c[0:len(usercards)]
			pygame.display.update()
			s=computersturntoshow()
			if s == 1:
				discardpile.append('assets/peeche.png')
				compcards.pop()
				print(compcards,c)
				carduser()
				cardcomp()
				deckmanip()
				makerectangle()
				showtext("Joe has declared a show! Group your cards.")
				pygame.display.update()
				count = 10
			count+=1 
			time.sleep(1)
			print(len(compcards),len(c))
		if count==3:
			computersturntothrow()
			c=c[0:len(usercards)]
			reset()
			carduser()
			cardcomp()
			deckmanip()
			pygame.display.update()
			count=0
			print(len(compcards),len(c),c)

		if count == 11:
			counter=100
			count=-1