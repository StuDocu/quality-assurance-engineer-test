from selenium.webdriver.common.by import By

MAIN_HEADER = {'by': By.XPATH, 'value': "//*[@class='header']/h1"}
CREATED_QUESTIONS_HEADER = {'by': By.XPATH, 'value': "//*[@class='questions']//*[@class='tooltipped-title__title']"}
CREATE_A_NEW_QUESTION_HEADER = {'by': By.XPATH,
                                'value': "//*[@class='question-maker']//*[@class='tooltipped-title__title']"}

CREATED_QUESTIONS_TIP = {'by': By.XPATH, 'value': "//*[@class='questions']//*[@class='tooltipped-title__tooltip ']"}
CREATE_A_NEW_QUESTION_TIP = {'by': By.XPATH,
                             'value': "//*[@class='question-maker']//*[@class='tooltipped-title__tooltip ']"}

NO_QUESTIONS_LABEL = {'by': By.XPATH, 'value': "//*[@class='alert alert-danger']"}
QUESTION_COUNTER_LABEL = {'by': By.XPATH, 'value': "//*[@class='sidebar']"}

CREATED_QUESTION = {'by': By.XPATH, 'value': "//*[@class='question__question']"}
CREATED_ANSWER = {'by': By.XPATH, 'value': "//*[@class='question__answer ']"}

ENTER_QUESTION_FIELD = {'by': By.ID, 'value': "question"}
ENTER_ANSWER_FIELD = {'by': By.ID, 'value': "answer"}

SORT_BUTTON = {'by': By.XPATH, 'value': "//*[@class='btn btn-primary']"}
REMOVE_BUTTON = {'by': By.XPATH, 'value': "//*[@class='btn btn-danger']"}
CREATE_BUTTON = {'by': By.XPATH, 'value': "//*[@class='btn btn-success']"}
