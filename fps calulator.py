import tkinter as tk
from tkinter import messagebox
import webbrowser

# Function to calculate the duration each picture should be shown in a video editor
def calculate_picture_duration():
    try:
        # Get the user inputs
        frames = int(entry_frames.get())
        fps_setting = float(entry_fps.get())
        
        # Ensure inputs are positive numbers
        if frames <= 0 or fps_setting <= 0:
            raise ValueError
        
        # Calculate the duration each picture needs to be displayed (in seconds)
        seconds_per_frame = 1 / fps_setting
        
        # Total video duration based on the number of frames and FPS
        total_video_duration = frames * seconds_per_frame

        # Display the results in the labels
        label_result.config(text=f"Each picture should be displayed for: {seconds_per_frame:.4f} seconds")
        label_total_duration.config(text=f"Total video duration: {total_video_duration:.2f} seconds")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter positive numerical values for frames and FPS.")

# Function to open the YouTube channel link
def open_link(event):
    webbrowser.open_new("https://youtube.com/@IamVortexViking")

# Create the main window
root = tk.Tk()
root.title("Picture to FPS Calculator")
root.geometry("400x350")

# Create and place widgets
label_frames = tk.Label(root, text="Enter total number of pictures:")
label_frames.pack(pady=10)
entry_frames = tk.Entry(root)
entry_frames.pack(pady=5)

label_fps = tk.Label(root, text="Enter desired FPS (frames per second):")
label_fps.pack(pady=10)
entry_fps = tk.Entry(root)
entry_fps.pack(pady=5)

# Button to trigger the calculation
button_calculate = tk.Button(root, text="Calculate", command=calculate_picture_duration)
button_calculate.pack(pady=10)

# Labels to display results
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

label_total_duration = tk.Label(root, text="")
label_total_duration.pack(pady=5)

# Create a label for the hyperlink
label_credit = tk.Label(root, text="Made by Vortex Viking", fg="blue", cursor="hand2")
label_credit.pack(pady=20)
label_credit.bind("<Button-1>", open_link)  # Bind the click event to the open_link function

# Start the Tkinter event loop
root.mainloop()
