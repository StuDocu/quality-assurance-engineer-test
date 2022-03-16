import re
import selenium
import uuid
from constants import *
from locators import *


def generate_some_string():
    return f'{uuid.uuid4()} /$:;.?'


def add_question_with_answer(driver, question, answer):
    question_field = driver.find_element(ENTER_QUESTION_FIELD['by'], ENTER_QUESTION_FIELD['value'])
    question_field.send_keys(question)
    question_field = driver.find_element(ENTER_ANSWER_FIELD['by'], ENTER_ANSWER_FIELD['value'])
    question_field.send_keys(answer)
    create_question_button = driver.find_element(CREATE_BUTTON['by'], CREATE_BUTTON['value'])
    create_question_button.click()


def get_questions_counter(driver):
    question_counter = driver.find_element(QUESTION_COUNTER_LABEL['by'],
                                           QUESTION_COUNTER_LABEL['value']).get_attribute("innerHTML")
    return re.search(QUESTION_COUNTER_TEXT_TEMPLATE, question_counter).group(1)


def check_element_not_present(driver, by, value):
    try:
        driver.find_element(by, value)
        return True
    except selenium.common.exceptions.NoSuchElementException:
        return False
