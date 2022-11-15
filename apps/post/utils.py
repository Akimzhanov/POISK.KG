from datetime import datetime
import re

def get_time():
    format = '%Y_%m_%d_%M_%s'
    return datetime.now().strftime(format)

def normalize_phone(phone):
    phone = re.sub('[^0-9]','',phone)  # шаблон, строки которые начинаются с 0-9
    if phone.startswith('0'):
        phone = f'996{phone[1:]}'
    if not phone.startswith('996'):
        phone = f'996{phone}'  #997121714
    phone = f'+{phone}'
    return phone