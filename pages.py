import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        # Localizadores dos campos, encapsulados dentro do construtor
        self.from_field = (By.ID, 'from')
        self.to_field = (By.ID, 'to')
        self.taxi_option_locator = (By.XPATH, '//button[contains(text(), "Chamar")]')
        self.comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
        self.comfort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
        self.number_text_locator = (By.CSS_SELECTOR, '.np-button')
        self.number_enter = (By.ID, 'phone')
        self.number_confirm = (By.CSS_SELECTOR, '.button.full')
        self.number_code = (By.ID, 'code')
        self.code_confirm = (By.XPATH, '//button[contains(text(), "Confirmar")]')
        self.number_finish = (By.CSS_SELECTOR, '.np-text')
        self.add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
        self.add_card = (By.CSS_SELECTOR, '.pp-plus')
        self.number_card = (By.ID, 'number')
        self.code_card = (By.CSS_SELECTOR, 'input.card-input#code')
        self.add_finish_card = (By.XPATH, '//button[contains(text(), "Adicionar")]')
        self.close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
        self.confirm_card = (By.CSS_SELECTOR, '.pp-value-text')
        self.add_comment = (By.ID, 'comment')
        self.switch_blanket = (By.CSS_SELECTOR, '.switch')
        self.switch_blanket_active = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')
        self.add_icecream = (By.CSS_SELECTOR, '.counter-plus')
        self.qnt_icecream = (By.CSS_SELECTOR, '.counter-value')
        self.call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
        self.pop_up = (By.CSS_SELECTOR, '.order-header-title')
        self.wait = WebDriverWait(self.driver, 30) # Instância de espera explícita

    def enter_from_location(self, from_text):
        # Usa a espera para garantir que o campo esteja presente antes de interagir
        from_input = self.wait.until(EC.element_to_be_clickable(self.from_field))
        from_input.send_keys(from_text)
        from_input.send_keys(Keys.ENTER) # Adicionado para simular a seleção da sugestão

    def enter_to_location(self, to_text):
        # Usa a espera para garantir que o campo esteja presente antes de interagir
        to_input = self.wait.until(EC.element_to_be_clickable(self.to_field))
        to_input.send_keys(to_text)
        to_input.send_keys(Keys.ENTER) # Adicionado para simular a seleção da sugestão

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        # A espera já está definida, agora apenas a usamos
        return self.wait.until(EC.visibility_of_element_located(self.from_field)).get_attribute('value')

    def get_to_location_value(self):
        # A espera já está definida, agora apenas a usamos
        return self.wait.until(EC.visibility_of_element_located(self.to_field)).get_attribute('value')

    def click_taxi_option(self):
        taxi_button = self.wait.until(
            EC.element_to_be_clickable(self.taxi_option_locator)
        )
        taxi_button.click()

    def click_comfort_icon(self):
        self.driver.find_element(*self.comfort_icon_locator).click()

    def click_comfort_active(self):
        try:
            active_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.comfort_active))
            return "active" in active_button.get_attribute('class')
        except:
            return False

    def click_number_text(self, telefone):
        self.driver.find_element(*self.number_text_locator).click()

        self.driver.find_element(*self.number_enter).send_keys(telefone)

        self.driver.find_element(*self.number_confirm).click()

        code = retrieve_phone_code(self.driver)
        code_input = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.number_code))
        code_input.clear()
        code_input.send_keys(code)

        self.driver.find_element(*self.code_confirm).click()

    def numero_confirmado(self):
        numero = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.number_finish))
        return numero.text

    def click_add_cartao(self,cartao,code):
        self.driver.find_element(*self.add_metodo_pagamento).click()
        self.driver.find_element(*self.add_card).click()
        time.sleep(1)
        self.driver.find_element(*self.number_card).send_keys(cartao)
        time.sleep(1)
        self.driver.find_element(*self.code_card).send_keys(code)
        time.sleep(1)
        self.driver.find_element(*self.add_finish_card).click()
        self.driver.find_element(*self.close_button_card).click()

    def confirm_cartao(self):
        return self.driver.find_element(*self.confirm_card).text

    def add_comentario(self, comentario):
        return self.driver.find_element(*self.add_comment).send_keys(comentario)

    def comment_confirm(self):
        return self.driver.find_element(*self.add_comment).get_attribute('value')

    def switch_cobertor(self):
        switch_ativo = self.driver.find_element(*self.switch_blanket)
        switch_ativo.click()

    def switch_cobertor_active(self):
        switch = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.switch_blanket_active))
        return switch.is_selected()

    def add_ice(self):
        self.driver.find_element(*self.add_icecream).click()

    def qnt_sorvete(self):
        return self.driver.find_element(*self.qnt_icecream).text

    def call_taxi(self):
        call_button = self.wait.until(
            EC.element_to_be_clickable(self.call_taxi_button)
        )
        call_button.click()

    def pop_up_show(self):
        pop_up = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.pop_up))
        return pop_up.text

