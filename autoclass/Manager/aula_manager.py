from threading import Thread, Timer
import socket
import sqlite3
from selenium import webdriver
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
from msedge.selenium_tools import Edge, EdgeOptions
from win10toast import ToastNotifier

options= EdgeOptions()
options.use_chromium= True
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2, 
    "create_all_shortcuts":False,
    "do_not_create_any_shortcuts":True,
    "do_not_create_desktop_shortcut": True,
    "do_not_create_quick_launch_shortcut": True,
    "do_not_create_taskbar_shortcut":True 
  })

WEEK_DAY_TUPLE=('Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Domingo')

driver=1

DATABASE='./autoclass/db.sqlite3'

def open_teams(aula: dict):
    print(aula)

    global options

    driver = webdriver.Edge('./msedgedriver.exe',options.to_capabilities())
    driver.get(aula['link'])
    
    Timer(aula['duracao_da_aula_minutos'],driver.close)

    time.sleep(3)
    login = driver.find_element_by_class_name('input')
    login.send_keys(aula['login'])
    login.send_keys(Keys.ENTER)
    time.sleep(4)

    senha= driver.find_element_by_class_name('input')
    senha.send_keys(aula['senha'])
    senha.send_keys(Keys.ENTER)
    time.sleep(4)    

    sim=driver.find_element_by_id("idSIButton9")
    sim.click()
    time.sleep(5)

    driver.get(aula['link'])

    time.sleep(10)
    
    entrar = driver.find_element_by_xpath('//calling-join-button/button')
    entrar.click()
    time.sleep(4)

    ingressar = driver.find_element_by_class_name("button-col")
    ingressar.click()

def open_blackboard():
    pass

def open_classroom():
    pass

def open_zoom():
    pass

def get_classes():
    try:
        with sqlite3.connect(DATABASE) as db:
            db.row_factory = sqlite3.Row
            cursor= db.execute('''SELECT * FROM crud_aula''')
            response=[dict(row) for row in cursor]
        return(response)
    except sqlite3.OperationalError:
        pass

def close_tab():
    global driver
    driver.quit()

aula_method_dict={
    "Teams": open_teams,
    "Zoom": open_zoom,
    "Classroom":open_classroom,
    "BlackBoard":open_blackboard,
}

all_times=[]

def start_timers():

    print('starting timers')
    #Sets tiny little things
    aulas= get_classes()
    now = datetime.today()
    
    #atualiza  o Timer toda meia noite
    global all_times
    dayly=Timer((datetime.today().replace(hour=23,minute=59)-datetime.today()).seconds,start_timers)
    dayly.start()
    all_times.append(dayly)

    #Método weekday retorna um inteiro  enumeranda de [Segunda, Domingo]
    
    for aula in aulas:
        if aula['dia_da_aula'] == WEEK_DAY_TUPLE[now.weekday()]:
            inicio = [int(a) for a in aula['horario_de_inicio'].split(':')]
            classtime = datetime.today().replace(hour=inicio[0] ,minute=inicio[1])
            if now < classtime:
                #Timer para abrir a aula
                open_class= Timer((classtime-now).seconds,aula_method_dict[aula['plataforma']],(aula,))
                open_class.start()
                #Timer para fechar a aul
                all_times.append(open_class)
                #Timer da notificação
                if (classtime-now).seconds>0:
                    notfy = Timer((classtime-now).seconds-300,toast_notfy,(aula,))
                    notfy.start()
                    all_times.append(notfy)
                else:
                    toast_notfy(aula)
    print(all_times)
    return(all_times)
        

def stop_timers():
    try:
        print('stopping timers')
        global all_times
        for timer in reversed(all_times):
            timer.cancel()
            all_times.pop()
    except: pass

def reload_timers():
    try:
        print('reloading timers')
        stop_timers()
        start_timers()
    except:pass

def signal_handler(data):
    print('handling signals')
    if data=="reload":
        reload_timers()
    if data =="end":
        close_tab()
        stop_timers()


def toast_notfy(aula):

    toaster = ToastNotifier()
    toaster.show_toast("Autoclass 2000",
                    f"Sua aula '{aula['nome']}' vai começar em 5 minutos",
                    icon_path=None,
                    duration=5,
                    threaded=True)





if __name__ =="__main__":
    start_timers()