import wocabee
import datetime
import traceback
import threading
from time import sleep
from selenium.webdriver.common.by import By
users = [
    # insert users here 
    # (username, password),...
]
def vsetky_baliky():
    while woca.get_packages(woca.DOPACKAGE):
        woca.pick_package(0,woca.get_packages(woca.DOPACKAGE))
        while True:
            try:
                woca.do_package()
            except Exception as e:
                print(traceback.format_exception(e))
            else:
                break
        sleep(2)
        if woca.exists_element(woca.driver,By.ID,"continueBtn"):
            woca.get_element(By.ID,"continueBtn").click()
        try:
            woca.wait_for_element(5,By.ID,"backBtn")
            if woca.get_element_text(By.ID,"backBtn") == "Uložiť a odísť":
                woca.get_element(By.ID,"backBtn").click()
        except:
            exit(0)

def do_wocabee(user):
    woca = wocabee.wocabee(user)
    woca.init()
    for x in range(len(woca.get_classes())):
        woca.pick_class(x,woca.get_classes())
        vsetky_baliky()
        woca.leave_class()
    woca.quit()

while True:
    if datetime.datetime.now().weekday() == 0 or 6: # if today is monday or sunday
        for x in users:
            thread = threading.Thread(do_wocabee,args=(x,))
            thread.start()
    
