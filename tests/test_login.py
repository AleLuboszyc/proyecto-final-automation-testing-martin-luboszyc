import pytest
from pages.LoginPage import LoginPage
from utils.data_reader import get_login_data

CASOS_LOGIN = get_login_data()

@pytest.mark.parametrize("username, password, expected_result", CASOS_LOGIN)
def test_login_data_driven(driver, username, password, expected_result):
    
    login_page = LoginPage(driver)
    
    login_page.go_to_login_page()\
              .enter_credentials(username, password)\
              .click_sign_in()

    if expected_result == "success":
        
        assert login_page.is_login_successful(), \
               f"FALLO: Esperado éxito para {username}, pero falló el login."
               
        
        
    elif expected_result == "failure":
        
        actual_error = login_page.get_error_message()
        
        if username == "locked_out_user":
            expected_error = "Epic sadface: Sorry, this user has been locked out."
        else:
            expected_error = "Epic sadface: Username and password do not match any user in this service"
            
        assert expected_error in actual_error, \
               f"FALLO: Esperado mensaje '{expected_error}' para {username}, pero se obtuvo '{actual_error}'."
    
    print(f"Test finalizado: {username} -> Resultado esperado: {expected_result}")