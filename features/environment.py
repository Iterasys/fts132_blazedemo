from selenium import webdriver

# Início
def before_all(context):    # Antes de Tudo

    # Declarar o Selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('drivers/chrome/96/chromedriver.exe')

    # Maximizar a janela do navegador
    context.driver.maximize_window()

    print('Passo A - Antes de Tudo')

# Fim
def after_all(context):     # Depois de Tudo

    # Desligar / Detruir o objeto do Selenium
    context.driver.quit()

    print('Passo Z - Depois de Tudo')