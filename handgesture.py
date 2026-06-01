import cv2
import mediapipe as mp
import numpy as np

# Inisialisasi Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=4,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Variabel untuk gambar dan UI
drawing = np.zeros((720, 1280, 3), dtype=np.uint8)
color = (255, 0, 0)  # Default: Biru
drawing_mode = False
menu_selected = None

# Daftar menu pilihan
menu_options = {
    "Blue":  (255, 0, 0),
    "Green": (0, 255, 0),
    "Red":   (0, 0, 255),
    "Pink":  (255, 119, 130),
    "Clear": "clear",
    "Start": "draw",
    "Stop":  "stop"
}

# Posisi menu di layar
menu_positions = {
    "Blue":  (200, 650),
    "Green": (400, 650),
    "Red":   (600, 650),
    "Pink":  (800, 650),
    "Clear": (1050, 200),
    "Start": (1050, 300),
    "Stop":  (1050, 100),
}

# Fungsi menggambar UI di layar
def draw_menu(image):
    for text, pos in menu_positions.items():
        clr = (0, 255, 255) if text == menu_selected else (255, 255, 255)
        cv2.putText(image, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 1, clr, 2, cv2.LINE_AA)

# Fungsi untuk mengecek gesture menulis (hanya telunjuk naik)
def is_writing_gesture(hand_landmarks):
    lm = hand_landmarks.landmark
    index_y  = lm[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    thumb_y  = lm[mp_hands.HandLandmark.THUMB_TIP].y
    middle_y = lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_y   = lm[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_y  = lm[mp_hands.HandLandmark.PINKY_TIP].y
    return (index_y < thumb_y and index_y < middle_y
            and index_y < ring_y and index_y < pinky_y)

# Menyimpan posisi sebelumnya untuk setiap tangan
prev_positions = {}

def detect_hand_gesture(image):
    global drawing, color, drawing_mode, menu_selected

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, _ = image.shape
            index_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w)
            index_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h)

            # Cek jika telunjuk ada di area menu
            for option, (mx, my) in menu_positions.items():
                if mx - 50 < index_x < mx + 50 and my - 20 < index_y < my + 20:
                    menu_selected = option
                    if option == "Clear":
                        drawing.fill(0)
                    elif option == "Start":
                        drawing_mode = True
                    elif option == "Stop":
                        drawing_mode = False
                    elif option in menu_options and menu_options[option] not in ("clear", "draw", "stop"):
                        color = menu_options[option]

            # Cek jika gesture menulis aktif
            if drawing_mode and is_writing_gesture(hand_landmarks):
                if hand_no not in prev_positions:
                    prev_positions[hand_no] = (index_x, index_y)
                else:
                    prev_x, prev_y = prev_positions[hand_no]
                    cv2.line(drawing, (prev_x, prev_y), (index_x, index_y), color, 5)
                    prev_positions[hand_no] = (index_x, index_y)
            else:
                prev_positions.pop(hand_no, None)

    return image

# Setup kamera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow('Hand Gesture Menu', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Hand Gesture Menu', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Gagal menangkap frame")
        break

    frame = detect_hand_gesture(frame)
    draw_menu(frame)

    combined = cv2.addWeighted(frame, 0.7, drawing, 0.3, 0)
    cv2.imshow('Hand Gesture Menu', combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
