import pyautogui
import time
import threading
from pynput import keyboard

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

macro_active = False
macro_thread = None

def toggle_macro():
    global macro_active, macro_thread
    macro_active = not macro_active
    status = "ВКЛЮЧЕН" if macro_active else "ВЫКЛЮЧЕН"
    print(f"Макрос {status}")
    
    if macro_active:
        if macro_thread is None or not macro_thread.is_alive():
            macro_thread = threading.Thread(target=run_macro, daemon=True)
            macro_thread.start()
    else:
        macro_active = False
        print("Остановка макроса...")

def run_macro():
    global macro_active
    
    while macro_active:
        try:
            screen_width, screen_height = pyautogui.size()
            click1_x = (screen_width // 2) + 25
            click1_y = (screen_height // 2) - 50
            pyautogui.click(click1_x, click1_y)
            print(f"Клик 1 правее ({click1_x}, {click1_y})")
            
            click2_x = (screen_width // 2) - 25
            click2_y = (screen_height // 2) - 50
            pyautogui.click(click2_x, click2_y)
            print(f"Клик 2 левее ({click2_x}, {click2_y})")
            
            time.sleep(1)
            
            pyautogui.keyDown('ctrl')
            pyautogui.moveTo(450, 330, duration=0.2)
            time.sleep(1)
            pyautogui.click(450, 330, button='left')
            pyautogui.keyUp('ctrl')
            print("Ctrl+Наведение+1с+Клик (450, 330)")
            
            time.sleep(2)
            
            pyautogui.moveTo(430, 300, duration=0.2)
            time.sleep(1)
            pyautogui.click(430, 300)
            print("Наведение+1с+Клик (430, 300)")
            
            time.sleep(13)
            
        except pyautogui.FailSafeException:
            print("Экстренная остановка (мышь в углу экрана)")
            macro_active = False
            break
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(1)

def on_press(key):
    try:
        if key == keyboard.Key.f7:
            toggle_macro()
    except AttributeError:
        pass

def main():
    print("=== МАКРОС F7 ===")
    print("F7 - включить/выключить макрос")
    print("Двигайте мышь в угол экрана для экстренной остановки")
    print("Ctrl+C для выхода из программы")
    print()
    
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nПрограмма завершена")
            macro_active = False

if __name__ == "__main__":
    main()
