pip install selenium pytest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo:
    @pytest.fixture(scope="class")
    def setup(self):
        # Configuração inicial
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        yield
        # Limpeza após os testes
        self.driver.quit()

    def test_login(self, setup):
        # Teste de login bem-sucedido
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_btn = self.driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_btn.click()

        # Verifica se o login foi bem-sucedido
        assert "inventory.html" in self.driver.current_url

    def test_add_to_cart(self, setup):
        # Teste de adicionar item ao carrinho
        add_to_cart_btn = self.driver.find_element(By.XPATH, "//button[contains(@id,'add-to-cart')]")
        add_to_cart_btn.click()

        # Verifica se o ícone do carrinho mostra 1 item
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"

    def test_checkout_process(self, setup):
        # Teste do processo de checkout
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()

        # Preenche informações de checkout
        first_name = self.driver.find_element(By.ID, "first-name")
        last_name = self.driver.find_element(By.ID, "last-name")
        postal_code = self.driver.find_element(By.ID, "postal-code")
        continue_btn = self.driver.find_element(By.ID, "continue")

        first_name.send_keys("Test")
        last_name.send_keys("User")
        postal_code.send_keys("12345")
        continue_btn.click()

        # Finaliza a compra
        finish_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_btn.click()

        # Verifica mensagem de confirmação
        confirmation = self.driver.find_element(By.CLASS_NAME, "complete-header")
        assert "Thank you for your order!" in confirmation.text
