#!/usr/bin/python3
# automaus.py
# Programm zum erfassen von Mauskoordinaten und deren automatische Abarbeitung.

# importieren der Module: pyautogui, time
import pyautogui, time
from pynput import mouse

# Variablen 
t_klick = 0.2   # Wartezeit nach 1xKlick in Sekunden
t_schritt = 4.4   # Wartezeit nach 6xKlick in Sekunden
t_zyklus = 5    # Wartezeit nach Durchlauf in Sekunden
oftmal = 0      # Durchlaufzähler
kordlist = []   # Liste mit Koordinaten-Tupel


# Funktionen
def on_click(x, y, button, pressed):
    # x,y = type 'int'
    global kordlist 
    if pressed == True:
        if button == mouse.Button.left:
            kordlist.append((x,y)) # x,y in Liste 
        if button == mouse.Button.right:
            return False # Stop listener
  
# das Programm
print('Maus-Links = Koordinaten / Maus-Rechts = Start')
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

time.sleep(0.5)
pyautogui.moveTo(kordlist[0],duration=0.5)

print('Ctrl+C zum beenden. es sind ' + str(len(kordlist)) + ' Punkte')

try:
   while True:
      for mpkt in kordlist:
         for anz in range(6):
            pyautogui.click(mpkt,duration=t_klick)
         time.sleep(t_schritt)
      oftmal = oftmal + 1 
      print('\b' * 15, end='', flush=True)
      print( 'Durchlauf: ' + str(oftmal).rjust(3) + '  ' + ('\b'), end='', flush=True)
      time.sleep(t_zyklus)   
except KeyboardInterrupt:
      print("\nfertig")  

    
