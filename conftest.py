import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function") 
def driver():
    """Fixture para inicializar y finalizar el WebDriver de Chrome automáticamente."""
    
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    driver.implicitly_wait(10) 
    
    yield driver
    
    print("\nCerrando navegador...")
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """Fixture para crear una instancia de LoginPage.
    
    Este fixture es muy útil para inyectar la página en tus tests sin
    tener que instanciarla en cada función.
    """
    from pages.LoginPage import LoginPage
    return LoginPage(driver)


@pytest.fixture(scope="module")
def api_base_url():
    """Fixture para devolver la URL base de la API JSONPlaceholder"""
    # ¡Cambiamos a JSONPlaceholder, que es más estable!
    return "https://jsonplaceholder.typicode.com"