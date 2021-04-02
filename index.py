import time
import random
verision = "Aplha 0.0.5"
print("©AfterDoor 2021.")
time.sleep(3)
print("After Door Inc. Представляет")
time.sleep(3)
print("Симулятор Разработчика Игр")
time.sleep(3)
print(verision)
time.sleep(2)

start = 0
i = 1
options = "0"
codes = "0"
code = 0
lvl = ["Япония","Россия","Украина","Америка"]
Genre = ["Мморпг","2дплаформер","Шутер","Гонки","Симулятор","Рпг","Стратегия","Хоррор","Бродилка"]
daydownloadrand01 = [1,2,3,4,5,6,7,8,9,10]
daydownloadrand02 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
Gamestatrand01 = random.randint(55, 80)
daydownload001 = 1
money = 0
moneyday = 0
day = 0
Gamestat01 = 1
Gamedownload01 = 0
daydownload01 = 0
Games = 0
Exit01 = 0
nextday = str(0)
entershop = "0"
daydownload01 = 0
moneyday = daydownload01
reklama01 = "0"
reklama1lvl01 = 0
reklamalvl01 = 0
reklamalvl01limit = 0
reklama2lvl02 = 0
reklamalvl02 = 0
reklamalvl02limit = 0
reklama3lvl03 = 0
reklamalvl03 = 0
reklamalvl03limit = 0
moneyday = 1
z = daydownloadrand01
a = 0
bossesplatf01 = 0
bossesshoot01 = 0
bossesMmorpg01 = 0
bossesRpg01 = 0
bossesBrodil01 = 0
graphic01 = 0
graphic1lvl01 = 0
graphiclvl01 = 0
graphiclvl01limit = 0
graphic2lvl02 = 0
graphiclvl02 = 0
graphiclvl02limit = 0
graphic3lvl03 = 0
graphiclvl03 = 0
graphiclvl03limit = 0
learnt01 = 0
lerntvideographic001 = 0
learntvideograph01 = 0
lerntvideographic01 = 0
lerntvideographic01limit = 0
timerlerntgraph01 = -1
timercredit01 = 1
timercreaditlimit01 = 0

while start != "Да":
	start = input("Начать игру?")
	if start == "Да":
		print("Тогда поехали!")
	elif start == 0:
		options = input("Настройки?")
	else :
		options = input("Настройки?")
	if options == "Да":
		print("Настройки")
		codes = input("Секретные коды?")
		if codes == "Да":
			print("Вводите код с первого раза иначе код не защитаеться а игра продолжиться!")
			code = int(input("Введите секретный код: "))
		if code == 3301:
			money += 10000
			Gamedownload01 += 1000
			print("Код активирован и за тобой уже выехали!")

Nickname = input("Введите свой никнейм: ")
if Nickname == "BESTWOOD":
	print("Этот ник настолько гениален что он сломал игру!")
	while i != float(3300.0):
		i += random.randint(1,2)
		print(i)
	print("3301?")
print("Привет, " + Nickname + "!" + "Это Симулятор разработчика игр!Здесь ты будеш делать свои игры и сотрудничать с такими же разработчиками!")

print("А теперь тебе надо зделать свою первую игру для начала придумай имя!")

Namegame01 = input("Введите название!: ")
print("Отличное название, " + Nickname + " .Теперь тебе нужно выбрать жанр игры!")

print("Жанров очень много но пока этот Симулятор добавлено несколько из многих:" + "Мморпг," + "2дплаформер," + "Шутер," + "Гонки," + "Симулятор," + "Рпг," + "Стратегия," + "Хоррор," + "Бродилка")
Genre01 = input("Введи жанр своей игры!: ")
print("Жанр " + Genre01 + " отлично подходит!")

if Genre01 == "2дплатформер":
	bossesplatf01 = input("Будут ли босы в вашей игре?")
if Genre01 == "Шутер":
	bossesshoot01 = input("Будут ли босы в вашей игре?")
if Genre01 == "Мморпг":
	bossesMmorpg01 = input("Будут ли босы в вашей игре?")
if Genre01 == "Рпг":
	bossesRpg01 = input("Будут ли босы в вашей игре?")
if Genre01 == "Бродилка":
	bossesBrodil01 = input("Будут ли босы в вашей игре?")

print("Отлично теперь надо добавить описание для игры!")
Description01 = input("Напиши описание для своей игры: ")

print("Получяеться так!")
print("Название: " + Namegame01)
print("Жанр: " + Genre01)
print("Описание: " + Description01)

creategame01 = input("Создать игру?")
if creategame01 == "Нет":
	print("Ну ладно)")
else :
	print("Окей, ты создал свою игру!")
	Games += 1

print("Теперь когда твоя игра " + Namegame01 + " выложена в сеть ты будеш получать первые деньги для твоего уровня тоесть " + lvl[0])
print("А имено ты будеш получать 1 валюту за 1 скачивание!С колчиеством скачиваний ты будеш увеличивать колчиество денег за скачивание!")
print("Данное колчиество скачиваний твоей игры: " + str(Gamedownload01))
print("Данное количество денег у тебя: " + str(money))
moneyday = 1
z = daydownloadrand01
commentspatfbosesposit01 = ["Отличное название " + Namegame01 + "!","Отличная графика!","Хорошая работа " + Nickname + "!","Боссы как раз в тему сюда!","Продолжай в том же духе " + Nickname + "!"]
commentspatfposit01 = []
commentsmmprgbosesposit01 = []
commentsmmorpgposit01 = []
commentsshootbosesposit01 = []
commentsshootposit01 = []
commentsracebosesposit01 = []
commentsraceposit01 = []
commentssimulbosesposit01 = []
commentssimulposit01 = []
commentsrpgbosesposit01 = []
commentsrpgposit01 = []
commentsstratbosesposit01 = []
commentsstrarposit01 = []
commentsbrodibosesposit01 = []
commentsbrodiposit01 = []
print(commentspatfbosesposit01[0])
while Exit01 != "Да":
	daydownload01 = 0
	print(Namegame01 + ": " + str(Gamedownload01))
	print("Описание: " + Description01)
	print("День: " + str(day))
	print("Деньги:" + str(money))
	if timerlerntgraph01 >= 1:
		print("Обучение создание графики")
		print("Осталось: " + str(timerlerntgraph01) + " до окночания обученния")
	if timerlerntgraph01 == 0:
		print("Обучение созданию графики закончено!")
		lerntvideographic01 = 1
	if money <= 0:
		if timercreaditlimit01 <= 0:
			timercredit01 += 6
			timercreaditlimit01 += 1
		print("У тебя кредит!Если ты не вернеш денги в прежнее состояние за" + str(timercredit01) + " то твоя игра закончиться!")
	if timercredit01 <= 0:
		print("Твое время истекло!Ты не смог погасить кредит игра закрываеться!")
		Exit01 = "Да"
	entershop01 = input("Войти в Магазин?")
	if entershop01 == "Да":
		reklama01 = input("Покупка рекламы?")
		if reklama01 == "Да":
			reklama1lvl01 = input("Реклама Первого уровня?")
			if reklamalvl01limit <= 2:
				if reklama1lvl01 == "Да":
					print("Успешная покупка!")
					print("Деньги -100")
					money -= 100
					reklamalvl01 += 10
					reklamalvl01limit += 1
			reklama2lvl02 = input("Реклама Второго Уровня?")
			if reklamalvl02limit <= 2:
				if reklama2lvl02 == "Да":
					print("Успешная покупка!")
					print("Деньги -500")
					money -= 500
					reklamalvl02 += 25
					reklamalvl02limit += 1
			reklama3lvl03 = input("Реклама Третего Уровня?")
			if reklamalvl03limit <= 2:
				if reklama3lvl03 == "Да":
					print("Успешная покупка!")
					print("Деньги -1000")
					money -= 1000
					reklamalvl03 += 50
					reklamalvl03limit += 1
		if lerntvideographic01 == 1:
			graphic01 = input("Улучшение графики?")
		else :
			print("Ты должен выучить сначала как создавать графику а потом начинать ее делать!")
		if graphic01 == "Да":
			graphic1lvl01 = input("Улучшение графики первого уровня?")
			if graphiclvl01limit == 0:
				if graphic1lvl01 == "Да":
					print("Успешная покупка!")
					print("Деньги -500")
					money -= 500
					graphiclvl01 += 20
					graphiclvl01limit += 1
			else :
				print("Не корректно введено!")
			graphic2lvl02 = input("Улучшение графики второго уровня?")
			if graphiclvl02limit == 0:
				if graphic2lvl02 == "Да":
					print("Успешная покупка!")
					print("Деньги -1000")
					money -= 1000
					graphiclvl02 += 45
					graphiclvl02limit += 1
			else :
				print("Не корректно введено!")
			graphic3lvl03 = input("Улучшение графики третего уровня?")
			if graphiclvl03limit == 0:
				if graphic3lvl03 == "Да":
					print("Успешная покупка!")
					print("Деньги -2500")
					money -= 2500
					graphiclvl03 += 20
					graphiclvl03limit += 1
			else :
				print("Не корректно введено!")
		learnt01 = input("Обучение?")
		if learnt01 == "Да":
			learntvideograph01 = input("Обучение созданию графики?")
			print('Стоимость 500')
			if lerntvideographic01limit <= 1:
				if learntvideograph01 == "Да":
					print("Деньги -500")
					money -= 500
					print("Отлично ты начал учиться созданию графики!Через пять дней закончиш!")
					timerlerntgraph01 += 6
			else :
				print("Ты не можеш выучить это еще раз!")
	nextday = input("Следуйший день?")
	if Gamedownload01 >= 50:
		z = daydownloadrand02
	if Gamedownload01 >= 100:
		a = 2
	if Gamedownload01 >= 500:
		a = 5
	if Gamedownload01 >= 1000:
		a = 10
	if nextday == "Да":
		timerlerntgraph01 -= 1
		timercredit01 -= 1
		daydownload01 += random.choice(z)
		Gamedownload01 += reklamalvl01
		Gamedownload01 += reklamalvl02
		Gamedownload01 += reklamalvl03
		Gamedownload01 += graphiclvl01
		Gamedownload01 += graphiclvl02
		Gamedownload01 += graphiclvl03
		Gamedownload01 += daydownload01
		money += daydownload01
		money += reklamalvl01
		money += a
		day += 1
		Exit = "0"
		nextday = "0"
		print("Следуший день!")
	if nextday == "да":
		timerlerntgraph01 -= 1
		timercredit01 -= 1
		daydownload01 += random.choice(z)
		Gamedownload01 += reklamalvl01
		Gamedownload01 += reklamalvl02
		Gamedownload01 += reklamalvl03
		Gamedownload01 += graphiclvl01
		Gamedownload01 += graphiclvl02
		Gamedownload01 += graphiclvl03
		Gamedownload01 += daydownload01
		money += daydownload01
		money += reklamalvl01
		money += a
		day += 1
		Exit = "0"
		nextday = "0"
		print("Следуший день!")
	if nextday == "ДА":
		timerlerntgraph01 -= 1
		timercredit01 -= 1
		daydownload01 += random.choice(z)
		Gamedownload01 += reklamalvl01
		Gamedownload01 += reklamalvl02
		Gamedownload01 += reklamalvl03
		Gamedownload01 += daydownload01
		Gamedownload01 += graphiclvl01
		Gamedownload01 += graphiclvl02
		Gamedownload01 += graphiclvl03
		money += daydownload01
		money += reklamalvl01
		money += a
		day += 1
		Exit = "0"
		nextday = "0"
		print("Следуший день!")
	if nextday == "Нет":
		Exit = "0"
		nextday = "0"
		print(Namegame01 + ":" + str(Gamedownload01))
		print("День: " + str(day))
		print("Деньги:" + str(money))
		Exit01 = input("Выйти из игры?")
	if nextday == "нет":
		Exit = "0"
		nextday = "0"
		print(Namegame01 + ":" + str(Gamedownload01))
		print("День: " + str(day))
		print("Деньги:" + str(money))
		Exit01 = input("Выйти из игры?")
