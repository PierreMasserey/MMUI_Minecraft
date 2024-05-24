import cv2
import mediapipe as mp
import pyautogui
import speech_recognition as sr
import threading

pyautogui.FAILSAFE = False

# Définition des constantes pour le seuil et la taille de l'écran
THRESHOLD = 0.25  
screen_w, screen_h = pyautogui.size()

last_input = []
recognizer = sr.Recognizer()

def stop():
    # Relâcher toutes les touches
    pyautogui.keyUp('w')
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')
    pyautogui.keyUp('d')
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

def slot_3():
    pyautogui.keyDown('3')

def jump():
    pyautogui.keyDown('space')

def jump_forward():
    pyautogui.keyDown('w')
    pyautogui.keyDown('space')
    last_input.append('w')
    last_input.append('space')

def destroy():
    pyautogui.mouseDown(button='left')
def place():
    pyautogui.mouseDown(button='right')

def detect_head_movements():
    print("Head tracking thread started")
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        
        if landmark_points:
            landmarks = landmark_points[0].landmark
            head_center_x = (landmarks[10].x + landmarks[234].x) / 2
            head_center_y = (landmarks[10].y + landmarks[234].y) / 2
            
            # Déplacer la souris si la tête dépasse le seuil
            if head_center_x < THRESHOLD:
                pyautogui.move(-40, 0)  # Déplacer la souris vers la gauche
            elif head_center_x > 1 - THRESHOLD:
                pyautogui.move(40, 0)  # Déplacer la souris vers la droite
    
            if head_center_y < THRESHOLD:
                pyautogui.move(0, -40)  # Déplacer la souris vers le haut
            elif head_center_y > 0.75 - THRESHOLD:
                pyautogui.move(0, 40)  # Déplacer la souris vers le bas
    
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)


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
        elif "backward" in command:  
            go_backward()
        elif "left" in command:
            go_left()
        elif "right" in command:
            go_right()
        elif "slot three" in command:
            slot_3()
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
        else:
            print('Please say the command again.')

# Création des threads
mic_thread = threading.Thread(target=run_microphone)
head_movement_thread = threading.Thread(target=detect_head_movements)

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
