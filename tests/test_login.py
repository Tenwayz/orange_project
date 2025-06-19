import pytest
import allure
from playwright.sync_api import expect

@allure.feature('Авторизация')
@allure.story('Авторизация с невалидными учетными данными')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с недействительными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('wrong_name', 'wrong_password'),
    ('wrong_name', 'admin123'),
    ('Admin', 'wrong_password')
])
def test_login_failure(login_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login(username, password)
    with allure.step('Отображается ошибка о неправильно заполненных полях'):
        expect(login_page.error_message).to_be_visible()
    with allure.step('Текст ошибки - Invalid credentials'):
        assert login_page.get_error_message() == 'Invalid credentials'


@allure.feature('Авторизация')
@allure.story('Авторизация с незаполненными полями логин/пароль')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с незаполненными полями логин ИЛИ пароль')
@pytest.mark.parametrize('username, password', [
    ('', 'admin123'),
    ('Admin', '')
])
def test_empty_name_field(login_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Не заполнять поле Логин или Пароль'):
        login_page.login(username, password)
    with allure.step('Отображается ошибка о незаполненных полях'):
        expect(login_page.empty_field_1_message).to_be_visible()
    with allure.step('Текст ошибки - Required'):
        assert login_page.get_empty_field_message() == 'Required'


@allure.feature('Авторизация')
@allure.story('Авторизация с незаполненными полями логин/пароль')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с незаполненным полем логин И пароль')
def test_empty_both_fields(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Не заполнять поля Логин и Пароль'):
        login_page.login('', '')
    with allure.step('Отображается ошибка о незаполненном поле Логин'):
        expect(login_page.empty_field_1_message).to_be_visible()
    with allure.step('Отображается ошибка о незаполненных поле Пароль'):
        expect(login_page.empty_field_2_message).to_be_visible()