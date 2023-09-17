from botcity.core import DesktopBot, Backend

"""
backend=Backend.UIA
backend=Backend.WIN32

 POR QUE E COMO ESCOLHER CADA UMA DAS DUAS FORMAS DE CONEXÃO
 > https://pywinauto.readthedocs.io/en/latest/getting_started.html

 UTILIZA PYWINAUTO NOS BASTIDORES
 > https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html

"""


def main():

    bot = DesktopBot()
    path_app =  fr'C:\Program Files\MyCRM.exe'
    bot.execute(path_app)
    bot.wait(2000)


    #                (forma de acesso, caminho de conexão)
    bot.connect_to_app(backend=Backend.UIA, path=path_app)

    # ValuePattern.Value	My CRM (Sample App)
    main_window = bot.find_app_window(title="My CRM (Sample App)")
    main_window.menu_select('File -> Clear Fields')

    # é do pywinauto
    main_window.type_keys('%{t} Camilo')
    main_window.Edit.type_keys('Costa')
    main_window.Edit10.type_keys('Fortaleza')
    main_window.Male.click()
    main_window.Company.select()
    main_window.People.select()
    main_window.menu_select('File -> Open')

    #ValuePattern.Value	Customer Lookup
    main_window.CostumerLookup.print_control_identifiers()
    main_window.CostumerLookup.Edit2.type_keys('Camilo')
    main_window.CostumerLookup.Edite3.type_keys('Costa')
    main_window.CostumerLookup.OK.click()

    # END



if __name__ == '__main__':
    main()