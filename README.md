# HandGesture ✋

Real-time hand gesture drawing app using **MediaPipe** and **OpenCV**. Draw on screen using your index finger through a webcam — control colors, start/stop drawing, and clear the canvas, all with hand gestures.

## Features

- ✏️ Draw on screen by raising only your index finger
- 🎨 Switch brush color: Blue, Green, Red, Pink
- 🖐️ Supports up to 4 hands at once
- 🧹 Clear canvas by hovering over the Clear button
- ⚡ Real-time processing via webcam

## How It Works

The app uses **MediaPipe Hands** to detect 21 hand landmarks per hand in real time. It checks whether only the index finger is raised (writing gesture), then draws a line between the current and previous fingertip position using **OpenCV**.

Menu options (Start, Stop, Clear, color buttons) are positioned on-screen. When the index finger tip enters a button's area, the action triggers automatically — no mouse or keyboard needed.

## Controls

| On-Screen Button | Action |
|-----------------|--------|
| Start | Enable drawing mode |
| Stop | Disable drawing mode |
| Clear | Wipe the canvas |
| Blue / Green / Red / Pink | Change brush color |

Press **Q** to quit the app.

## Setup

> ⚠️ Requires **Python 3.9 – 3.12**. Python 3.14 is NOT supported by MediaPipe.

```bash
# 1. Clone repo
git clone https://github.com/rafiarsya07/HandGesture.git
cd HandGesture

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python handgesture.py
```

## Tech Stack

- Python 3.11
- MediaPipe 0.10.14
- OpenCV 4.10
- NumPy 1.26.4

## Notes

- Make sure your webcam is connected before running
- Works best in a well-lit room with a plain background
- `venv/` folder is excluded from this repo — install dependencies manually via `requirements.txt`