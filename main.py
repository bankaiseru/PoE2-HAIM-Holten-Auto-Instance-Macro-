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
    status = "ON" if macro_active else "OFF"
    print(f"Macro {status}")
    
    if macro_active:
        if macro_thread is None or not macro_thread.is_alive():
            macro_thread = threading.Thread(target=run_macro, daemon=True)
            macro_thread.start()
    else:
        macro_active = False
        print("Stopping macro...")

def run_macro():
    global macro_active
    
    while macro_active:
        try:
            screen_width, screen_height = pyautogui.size()
            
            base_y = (screen_height // 2) - 50
            
            # Первая позиция: центр +25px вправо, 3 клика по высоте
            click1_x = (screen_width // 2) + 25
            click1_y_top = base_y - 25      # Выше на 25px
            click1_y_middle = base_y        # Средний
            click1_y_bottom = base_y + 25   # Ниже на 25px
            
            time.sleep(0.3)
            pyautogui.click(click1_x, click1_y_top)
            print(f"Click 1 RIGHT TOP ({click1_x}, {click1_y_top})")
            
            time.sleep(0.3)
            pyautogui.click(click1_x, click1_y_middle)
            print(f"Click 1 RIGHT MIDDLE ({click1_x}, {click1_y_middle})")
            
            time.sleep(0.3)
            pyautogui.click(click1_x, click1_y_bottom)
            print(f"Click 1 RIGHT BOTTOM ({click1_x}, {click1_y_bottom})")
            
            # Вторая позиция: центр -25px влево, 3 клика по высоте
            click2_x = (screen_width // 2) - 25
            click2_y_top = base_y - 25      # Выше на 25px
            click2_y_middle = base_y        # Средний
            click2_y_bottom = base_y + 25   # Ниже на 25px
            
            time.sleep(0.3)
            pyautogui.click(click2_x, click2_y_top)
            print(f"Click 2 LEFT TOP ({click2_x}, {click2_y_top})")
            
            time.sleep(0.3)
            pyautogui.click(click2_x, click2_y_middle)
            print(f"Click 2 LEFT MIDDLE ({click2_x}, {click2_y_middle})")
            
            time.sleep(0.3)
            pyautogui.click(click2_x, click2_y_bottom)
            print(f"Click 2 LEFT BOTTOM ({click2_x}, {click2_y_bottom})")
            
            time.sleep(1)
            
            # Ctrl + прицел + клик
            pyautogui.keyDown('ctrl')
            pyautogui.moveTo(450, 330, duration=0.2)
            time.sleep(1)
            pyautogui.click(450, 330, button='left')
            pyautogui.keyUp('ctrl')
            print("Ctrl+Aim+1s+Click (450, 330)")
            
            time.sleep(2)
            
            # Второй прицел + клик
            pyautogui.moveTo(430, 300, duration=0.2)
            time.sleep(1)
            pyautogui.click(430, 300)
            print("Aim+1s+Click (430, 300)")
            
            time.sleep(10)
            
        except pyautogui.FailSafeException:
            print("Emergency stop (mouse in screen corner)")
            macro_active = False
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

def on_press(key):
    try:
        if key == keyboard.Key.f7:
            toggle_macro()
    except AttributeError:
        pass

def main():
    print("=== MACRO F7 ===")
    print("F7 - включить/выключить макрос")
    print("Наведите мышь в угол экрана для экстренной остановки")
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
