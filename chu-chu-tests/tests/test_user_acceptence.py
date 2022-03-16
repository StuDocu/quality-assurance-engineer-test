import pytest
from selenium import webdriver
from constants import *
from functions import add_question_with_answer, generate_some_string, get_questions_counter, check_element_not_present
from locators import *


def test_show_headers(driver):
    """
    Checks three main headers of the page

    :param driver:
    :return:
    """
    main_header = driver.find_element(MAIN_HEADER['by'], MAIN_HEADER['value']).get_attribute("innerHTML")
    assert MAIN_HEADER_TEXT == main_header
    created_questions_header = driver.find_element(CREATED_QUESTIONS_HEADER['by'],
                                                   CREATED_QUESTIONS_HEADER['value']).get_attribute("innerHTML")
    assert CREATED_QUESTIONS_HEADER_TEXT == created_questions_header
    create_a_new_question_header = driver.find_element(CREATE_A_NEW_QUESTION_HEADER['by'],
                                                       CREATE_A_NEW_QUESTION_HEADER['value']).get_attribute("innerHTML")
    assert CREATE_A_NEW_QUESTION_HEADER_TEXT == create_a_new_question_header


@pytest.mark.parametrize("header,tip_element,tip_text",
                         [(CREATED_QUESTIONS_HEADER, CREATED_QUESTIONS_TIP, CREATED_QUESTIONS_TIP_TEXT),
                          (CREATE_A_NEW_QUESTION_HEADER, CREATE_A_NEW_QUESTION_TIP, CREATE_A_NEW_QUESTION_TIP_TEXT)])
def test_show_tips(driver, header, tip_element, tip_text):
    """
    Parametrized test of tips of the page

    :param driver:
    :param header:
    :param tip_element:
    :param tip_text:
    :return:
    """
    driver.refresh()
    title = driver.find_element(header['by'], header['value'])
    action = webdriver.ActionChains(driver)
    action.move_to_element(title).perform()
    tip_text = driver.find_element(tip_element['by'], tip_element['value']).get_attribute("innerHTML")
    assert tip_text == tip_text


def test_delete_question(driver):
    """
    Checks question deleting

    :param driver:
    :return:
    """
    driver.refresh()
    remove_button = driver.find_element(REMOVE_BUTTON['by'], REMOVE_BUTTON['value'])
    remove_button.click()
    text = driver.find_element(NO_QUESTIONS_LABEL['by'], NO_QUESTIONS_LABEL['value']).get_attribute("innerHTML")
    assert NO_QUESTIONS_YET_TEXT == text
    assert NO_QUESTIONS_TEXT == get_questions_counter(driver)
    assert not check_element_not_present(driver, SORT_BUTTON['by'], SORT_BUTTON['value'])


def test_create_a_new_question(driver):
    """
    Checks question creating

    :param driver:
    :return:
    """
    driver.refresh()
    generated_question = generate_some_string()
    generated_answer = generate_some_string()
    add_question_with_answer(driver, generated_question, generated_answer)
    questions_list = driver.find_elements(CREATED_QUESTION['by'], CREATED_QUESTION['value'])
    assert HOW_TO_ADD_A_QUESTION_TEXT == questions_list[0].get_attribute("innerHTML"), "Default question not present"
    questions_list[1].click()
    question_question = questions_list[1].get_attribute("innerHTML")
    answers_list = driver.find_elements(CREATED_ANSWER['by'], CREATED_ANSWER['value'])
    question_answer = answers_list[0].get_attribute("innerHTML")
    assert generated_question == question_question
    assert generated_answer == question_answer


def test_counting_questions(driver):
    """
    Checks counter values and last S with question word

    :param driver:
    :return:
    """
    driver.refresh()
    assert ONE_QUESTION_TEXT == get_questions_counter(driver)
    add_question_with_answer(driver,
                             question=generate_some_string(),
                             answer=generate_some_string())
    assert TWO_QUESTIONS_TEXT == get_questions_counter(driver)


def test_sort_questions(driver):
    """
    Checks sorting

    :param driver:
    :return:
    """
    driver.refresh()
    expected_question_list = [HOW_TO_ADD_A_QUESTION_TEXT]
    question_list = []

    for i in range(5):
        generated_question = generate_some_string()
        expected_question_list.append(generated_question)
        add_question_with_answer(driver,
                                 question=generated_question,
                                 answer=generate_some_string())
    sort_button = driver.find_element(SORT_BUTTON['by'], SORT_BUTTON['value'])
    sort_button.click()

    questions_list_elements = driver.find_elements(CREATED_QUESTION['by'], CREATED_QUESTION['value'])
    for i in range(6):  # +1 because of HOW_TO_ADD_A_QUESTION_TEXT
        question_list.append(questions_list_elements[i].get_attribute("innerHTML"))

    expected_question_list.sort(key=str.casefold)
    assert expected_question_list == question_list


@pytest.mark.parametrize("question,answer", [('', 'some answer'), ('some question', '')])
def test_decline_adding_empty_fields(driver, question, answer):
    """
    Checks filter for adding empty question or answer

    :param driver:
    :param question:
    :param answer:
    :return:
    """
    driver.refresh()
    add_question_with_answer(driver, question, answer)
    questions_list = driver.find_elements(CREATED_QUESTION['by'], CREATED_QUESTION['value'])
    assert HOW_TO_ADD_A_QUESTION_TEXT == questions_list[0].get_attribute("innerHTML"), "Default question not present"
    assert len(questions_list) < 2
