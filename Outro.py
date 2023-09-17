import time
import pygame
import os
from PIL import Image

# Set the path to your MP3 file
mp3_path = "C:/Users/maisa/Desktop/PracticeCode/Outro/Outro.mp3"
image_path = 'C:/Users/maisa/Desktop/PracticeCode/Outro/aight.jpg'

# Initialize pygame
pygame.init()

# Initialize the mixer module for audio
pygame.mixer.init()

# Create a new mixer channel (optional)
channel = pygame.mixer.Channel(0)

# Load the MP3 file
try:
    pygame.mixer.music.load(mp3_path)
    print(f"Playing {os.path.basename(mp3_path)}")
except pygame.error as e:
    print(f"Error loading {os.path.basename(mp3_path)}: {e}")
    pygame.quit()
    quit()

# Play the MP3 file
pygame.mixer.music.play()

image = Image.open(image_path)

# Wait for the MP3 to finish playing (optional)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    
    print ('life is a movie, and we are the audience')
    
    for i in range(0, 15):

        print ('System shutting down in' , 15 - i)
        time.sleep(1)
        
    image.show()
    print ('life is a movie, and we are the audience')
    print ('peace')
    os.system("shutdown /s /t 1")
    

# Quit pygame
pygame.quit()
