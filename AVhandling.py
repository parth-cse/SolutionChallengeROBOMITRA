import cv2
import pyaudio
import socket

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize audio stream
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Create a socket connection to the user interface
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('user_interface_ip', 5000))  # Replace with actual IP and port

# Continuously capture and stream data
while True:
    ret, frame = cap.read()

    # Send frame through socket (replace with your preferred communication method)
    frame_bytes = frame.tobytes()
    client_socket.sendall(frame_bytes)

    # Read audio data
    data = stream.read(1024)

    # Send audio data through socket (replace with your preferred communication method)
    client_socket.sendall(data)

# Close resources
client_socket.close()
stream.stop_stream()
stream.close()
audio.terminate()
cap.release()
