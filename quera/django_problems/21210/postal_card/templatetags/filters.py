import re

from django import template

register = template.Library()

english_numbers_to_farsi_numbers = {
    '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵',
    '6': '۶', '7': '۷', '8': '۸', '9': '۹', '0': '۰'
}

@register.filter
def translate_numbers(text: str) -> str:
    for english_number, farsi_number in \
            english_numbers_to_farsi_numbers.items():
        text = re.sub(english_number, farsi_number, text)
    return text
