# This script plots audio using matplotlib into
# a series of images, which are stitched together using
# ffmpeg to create an audio visualization

import librosa
import matplotlib.pyplot as plt
import moviepy
import numpy as np
from itertools import cycle

# Load audio
filename = input("Filename: ")
y, sr = librosa.load(filename)
frame_len = len(y)
print(f"Need to process {frame_len} frames")
# Frame rate for the video
fps = 40

# Duration of each frame in seconds
frame_duration = 1 / fps

# Number of samples per frame
samples_per_frame = int(sr * frame_duration)

# Modify Colors here
colors = [
  "#FEFFC9", #pale yellow/white
  "#443C3F", #dark grey
  "#56050C", # deep red
  "#525751", # grey
  "#F2544C", #light red
]

# Create frames
color_flip_condition = 20
color_flip_counter = 0
color_index = int(input("Start color offset [0|1]: "))
counter = 0

frames = []

color = colors[color_index]
for i in range(0, len(y), samples_per_frame):
    # Extract a segment of the audio for this frame
    frame_data = y[i:i + samples_per_frame]
    counter +=1

    # Create a plot
    plt.figure(figsize=(10, 4))

    #Custom hacks to make the graph look bigger
    amplitude_scale = 1.5  # Increase amplitude by 50%
    frame_data = frame_data * amplitude_scale

    plt.plot(frame_data, color=colors[color_index])
    plt.ylim(-1, 1)  # Set y-axis limits to amplitude range
    plt.axis('off')  # Hide axes

    # Save the plot as an image
    plt.savefig(f"frame_{i}.png", bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()

    # Add to the list of frames
    frames.append(f"frame_{i}.png")
    color_flip_counter += 1
    if color_flip_counter > color_flip_condition:
        color_index +=1
        color_flip_counter = 0
    
        if color_index >= len(colors):
            color_index = 0

# Create a clip from the frames
print("Total Counts: ", counter)
clip = moviepy.ImageSequenceClip(frames, fps=fps)

# Write the video file
clip.write_videofile("audio_visualization.webm", codec="vp9", ffmpeg_params=["-vf", "format=yuva420p"])

# Cleanup images lying around
import os
for frame in frames:
    os.remove(frame)