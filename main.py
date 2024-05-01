import pyautogui
import speech_recognition as sr
import time

def stop():
    for i in last_input:
        pyautogui.keyUp(i)
    last_input.clear()

def go_forward():
    pyautogui.keyDown('w')
    last_input.append('w')

def go_backward():
    pyautogui.keyDown('s')
    last_input.append('s')

def go_left():
    pyautogui.keyDown('a')
    last_input.append('a')

def go_right():
    pyautogui.keyDown('d')
    last_input.append('d')

def slot_1():
    pyautogui.keyDown('1')

def jump():
    pyautogui.keyDown('space')

def jump_forward():
    pyautogui.keyDown('w')
    pyautogui.keyDown('space')
    last_input.append('w')
    last_input.append('space')

def destroy():
    pyautogui.click(button='left')

def place():
    pyautogui.click(button='right')

def use_microphone(recognizer, source, timeout):
    print("Listening...")
    audio = recognizer.listen(source, timeout=timeout)
    return audio

last_input = []
recognizer = sr.Recognizer()

print("hello")

timeout_counter = 0
listening = False

with sr.Microphone() as source:
    while True:
        try:
            if not listening:
                audio = use_microphone(recognizer, source, timeout=500)  # Timeout initial de 500ms
                print("Start of listening...")
                listening = True

            if audio and timeout_counter < 20:  # 50 * 0.1s = 5s
                command = recognizer.recognize_google(audio)
                print("You said:", command)

                if "forward" in command:
                    go_forward()
                elif "backward" in command:  
                    go_backward()
                elif "left" in command:
                    go_left()
                elif "right" in command:
                    go_right()
                elif "slot one" in command:
                    slot_1()
                elif "jump" in command:
                    jump()
                elif "break" in command:
                    destroy()
                elif "put" in command:
                    place()
                elif "up" in command:
                    jump_forward()
                elif "stop" in command:
                    stop()

                listening = False  # Réinitialiser le drapeau de l'écoute
                timeout_counter = 0  # Réinitialiser le compteur de timeout

            elif timeout_counter >= 20:
                print("Timeout reached. Restarting listening...")
                listening = False
                timeout_counter = 0

            else:
                timeout_counter += 1
                time.sleep(0.1)  # Attendre 0.1 seconde
        except sr.UnknownValueError:
            print("Error: I did not recognize any words.")
            listening = False
        except sr.RequestError:
            print("Sorry, I couldn't request results. Please check your internet connection.")
            listening = False
        except KeyboardInterrupt:
            break
        finally:
            print(last_input)
