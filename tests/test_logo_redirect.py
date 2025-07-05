import allure
import pytest
from conftest import driver
from page_objects.main_page import MainPage


class TestLogoRedirect:
    @allure.title('Проверяется, что клик по логотипу «Самокат» в верхней части страницы ведёт на главную страницу сервиса')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверяется, что при нажатии по логотипу «Яндекс» направляет пользователя на страницу «Дзен»')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert main_page.get_page_title() == 'Дзен'