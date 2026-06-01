# HandGesture ✋

Real-time hand gesture drawing app using **MediaPipe** and **OpenCV**. Draw on screen using your index finger via webcam — select colors, start/stop drawing, and clear the canvas, all with hand gestures.

## Features
- 🖐️ Detects up to 4 hands simultaneously
- ✏️ Draw by raising only your index finger
- 🎨 Switch colors: Blue, Green, Red, Pink
- 🖱️ Menu control via hand gesture (no mouse/keyboard needed)
- 🧹 Clear canvas gesture
- ⚡ Real-time at 30+ FPS

## Demo

Point your **index finger** at a menu option on screen to select it:

| Option | Action |
|--------|--------|
| Start  | Enable drawing mode |
| Stop   | Disable drawing mode |
| Clear  | Wipe the canvas |
| Blue / Green / Red / Pink | Change brush color |

## Setup

> **Requires Python 3.9 – 3.12** (Python 3.14 is NOT supported by mediapipe yet)

```bash
# 1. Clone repo
git clone https://github.com/rafiarsya07/HandGesture.git
cd HandGesture

# 2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python handgesture.py
```

Press **Q** to quit.

## Tech Stack
- Python 3.9–3.12
- [MediaPipe](https://mediapipe.dev/) 0.10.14
- OpenCV 4.10
- NumPy

## Notes
- Make sure your webcam is connected and accessible
- Works best with good lighting and a plain background
- mediapipe 0.10.21+ dropped `mp.solutions` support — use `0.10.14` as specified in requirements
# HandGesture
# HandGesture
# HandGesture
# HandGesture
