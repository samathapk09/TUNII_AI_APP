import cv2
import sys

def try_open_video_device():
    for i in range(10):  # Try the first 10 indices
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print(f"Opened video device at /dev/video{i}")
            return cap
    raise IOError("Error: Could not open any video device")

try:
    cap = try_open_video_device()

    # Continue with your processing logic here
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Display or process the frame as needed
        cv2.imshow('Frame', frame)
        # Exit loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the video capture object and close any windows
    cap.release()
    cv2.destroyAllWindows()

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
