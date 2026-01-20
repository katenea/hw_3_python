import datetime


# 1. Создайте словарь email, содержащий следующие поля:
# subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).
email = {
    'subject': 'kate',
    'from': 'Kaliningrad@mail.ru ',
    'to': ' Moscow@mail.ru',
    'body': ' Hello \nfriend \t '
    }


# 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD
# и запишите её в email["date"].
send_date = datetime.datetime.now()
email['date'] = send_date.strftime('%Y-%m-%d')


# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].

email['from'] = email['from'].lower().strip()
email['to'] = email['to'].lower().strip()


# 4. Извлеките логин и домен отправителя в две переменные login и domain.
login = email['from'].split('@')[0]
domain = email['from'].split('@')[1]


# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].

email['short_body'] = email['body'][0:10] + '...'


# 6. Списки доменов: создайте список личных доменов и список корпоративных доменов с учетом того
# что там должны быть только уникальные значение
a = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
b = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
private = list(set(a))
corporate = list(set(b))


# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
# ни один домен не должен входить в оба списка одновременно.

intersection = set(private) & set(corporate)

# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate,
# # равную результату проверки вхождения домена отправителя в список корпоративных доменов.

is_corporate = domain in corporate

# 9. Соберите «чистый» текст сообщения

email['clean_body'] = email['body'].replace('\t', ' ').replace('\n',' ')


# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}

multi_text = f'''Кому: {email['to']}
от {email['from']}
Тема: {email['subject']}
дата {email['date']}
{email['clean_body']}'''
email['sent_text'] = multi_text

# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.

pages = (len(email['sent_text']) + 499) // 500


# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty,
# is_body_empty в котором будет хранится что тема письма содержит данные.

is_subject_empty = not email['subject']
is_body_empty = not email['body']


# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].

email['masked_from'] = login[:2] + '***@' + domain



# 14.  Удалите из списка личных доменов значения "list.ru" и "bk.ru".

private.remove('list.ru')
private.remove('bk.ru')



#print
print(email)
print(email['date'])
print(email['from'])
print(email['to'])
print(login)
print(domain)
print(email['short_body'])
print(private)
print(corporate)
print(intersection)
print(email['clean_body'])
print(email['sent_text'])
print(pages)
print(is_subject_empty)
print(is_body_empty)
print(email['masked_from'])



