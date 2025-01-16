import smtplib
import os
from dotenv import load_dotenv

friend_name = 'мой друг'
my_name = 'Jana'
website = 'https://dvmn.org/profession-ref-program/yanix2x2/ya6Ge/'
my_email = 'YanixAvatar@yandex.ru'
friend_email = 'YanixAvatar@yandex.ru'

letter = """\
From: {my_email}
To: {friend_email}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""\
	.format(friend_name=friend_name, my_name=my_name, website=website, my_email=my_email, friend_email=friend_email)\
	.encode()

load_dotenv(override=True)
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')	
server.login(login, password)
server.sendmail(my_email, friend_email, letter)
server.quit()