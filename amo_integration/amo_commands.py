"""
Модуль команд работы с AMO CRM
"""
from amocrm.v2 import Lead as _Lead, custom_field
from amo_integration.connect_api_amo import connect_amo
from asgiref.sync import sync_to_async
from datetime import datetime

# from api_amo.decorator_launch import delayed_launch
from media_bot.texts import text_story_recording

"""
Класс определения полей с данными АМО
"""


class Lead(_Lead):
    source_phone = custom_field.TextCustomField("Source_phone")
    rec_date = custom_field.TextCustomField("Дата записи")
    rec_time = custom_field.TextCustomField("Время записи")
    doctor = custom_field.TextCustomField("ФИО врача")


"""
Функция добавления записи пользователя в АМО
"""


@sync_to_async()
def add_contact(name: str, phone: str):
    name = f"{name} {phone}"
    connect_amo()
    create_contact = Lead.objects.create(name=name)
    create_contact.source_phone = phone
    create_contact.tags.append("Телеграм бот")
    create_contact.save()


"""
Функция извлечения информации о записи пользователя из АМО
"""


def info(phone):
    connect_amo()
    try:
        lead = Lead.objects.get(query=phone)
        date = datetime.fromtimestamp(lead.rec_date).strftime("%d.%m.%Y")
        time_ = lead.rec_time
        doctor = lead.doctor
        return f"Вы записаны {date} на {time_} к доктору {doctor}"
    except Exception:
        return text_story_recording
