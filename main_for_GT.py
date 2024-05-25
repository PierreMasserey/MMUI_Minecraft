import pyautogui
import speech_recognition as sr
import threading
from GazeTracking.gaze_tracking.gaze_tracking import GazeTracking
import cv2

pyautogui.FAILSAFE = False

last_input = []
recognizer = sr.Recognizer()
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

def stop():
    # Relâcher toutes les touches
    pyautogui.keyUp('w')
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')
    pyautogui.keyUp('d')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('1')
    pyautogui.keyUp('2')
    pyautogui.keyUp('3')
    pyautogui.keyUp('space')
    
    # Relâcher tous les boutons de la souris
    pyautogui.mouseUp(button='left')
    pyautogui.mouseUp(button='right')

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
def slot_2():
    pyautogui.keyDown('2')
def slot_3():
    pyautogui.keyDown('3')

def jump():
    pyautogui.keyDown('space')

def jump_forward():
    pyautogui.keyDown('w')
    pyautogui.keyDown('space')
    last_input.append('w')
    last_input.append('space')

def go_ten_step():
    for _ in range(20):
        pyautogui.keyDown('w')
        last_input.append('w')
        pyautogui.keyUp('w')
        time.sleep(0.1)

def shift():
    pyautogui.keyDown('shift')
    last_input.append('space')


def destroy():
    pyautogui.mouseDown(button='left')
def place():
    pyautogui.mouseDown(button='right')

def detect_gaze_movements():


    while True:
            # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        if gaze.is_right() :
            pyautogui.move(40, 0)
        
        elif gaze.is_left() : 
            pyautogui.move(-40, 0)
        
        elif gaze.is_top() :
            pyautogui.move(0, -40)
        
        elif gaze.is_bottom() :
            pyautogui.move(0, 40)


def take_command():
    print("Entering take_command")
    with sr.Microphone() as source:
        print('Microphone is open...')
        recognizer.adjust_for_ambient_noise(source)
        print('Listening...')
        try:
            voice = recognizer.listen(source)
            print('Processing voice...')
            command = recognizer.recognize_google(voice)
            command = command.lower()
            if 'command' in command:
                command = command.replace('ok', '')
                print(f"Recognized command: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return ""

def run_microphone():
    print("Microphone thread started")
    while True:
        command = take_command()
        print(f"Command received: {command}")
        if "forward" in command:
            go_forward()
        elif "go" in command:
            go_ten_step()
        elif "backward" in command:  
            go_backward()
        elif "left" in command:
            go_left()
        elif "right" in command:
            go_right()
        elif "use first" in command:
            slot_1()
        elif "use second" in command:
            slot_2()
        elif "use third" in command:
            slot_3()
        elif "jump" in command:
            jump()
        elif "break" in command:
            destroy()
        elif "put" in command:
            place()
        elif "up" in command:
            jump_forward()
        elif "shift" in command:
            shift()
        elif "stop" in command:
            stop()
        else:
            print('Please say the command again.')

# Création des threads
mic_thread = threading.Thread(target=run_microphone)
head_movement_thread = threading.Thread(target=detect_gaze_movements)

# Démarrage des threads
print("Starting threads")
mic_thread.start()
head_movement_thread.start()

# Ajout de pauses pour s'assurer que les threads démarrent correctement
import time
time.sleep(1)

# Attente de la fin des threads (ce blocage du programme permet de garder les threads actifs)
mic_thread.join()
head_movement_thread.join()

print("Threads have been started")
