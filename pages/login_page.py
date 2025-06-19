from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_text("Invalid credentials")
        self.empty_field_1_message = page.get_by_text("Required").nth(0)
        self.empty_field_2_message = page.get_by_text("Required").nth(1)


    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()

    def get_empty_field_message(self):
        return self.empty_field_1_message.inner_text()