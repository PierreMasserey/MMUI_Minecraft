import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Seuil pour déplacer la souris
THRESHOLD = 0.25  

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
            pyautogui.move(-10, 0)  # Déplacer la souris vers la gauche
        elif head_center_x > 1 - THRESHOLD:
            pyautogui.move(10, 0)  # Déplacer la souris vers la droite


        # Déplacer la souris si la tête dépasse le seuil
        if head_center_y < THRESHOLD:
            pyautogui.move(0, -10)  # Déplacer la souris vers le haut
        elif head_center_y > 0.75 - THRESHOLD:
            pyautogui.move(0, 10)  # Déplacer la souris vers le bas
        
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
        
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
    
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
