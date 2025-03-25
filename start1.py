import tkinter as tk
import time
from PIL import Image, ImageTk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Start/Stop Timer")

        self.start_time = None
        self.running = False
        self.elapsed_time = 0
        self.total_time = 0


        self.time_label = tk.Label(root, text="00:00", font=("Tekton Pro", 48))
        self.time_label.pack()


        self.start_button = tk.Button(root, text="Start", font=("Tekton Pro", 14), command=self.start_timer)
        self.start_button.pack(pady=10)


        self.stop_button = tk.Button(root, text="Stop", font=("Tekton Pro", 14), state=tk.DISABLED, command=self.stop_timer)
        self.stop_button.pack(pady=10)


        self.elapsed_time_label = tk.Label(root, text="", font=("Tekton Pro", 18))
        self.elapsed_time_label.pack(pady=10)


        gif_path = "kitty.gif"
        gif_image = Image.open(gif_path)


        self.gif_frames = []
        for frame in range(gif_image.n_frames):
            gif_image.seek(frame)
            self.gif_frames.append(ImageTk.PhotoImage(gif_image.copy()))


        self.gif_label = tk.Label(root)
        self.gif_label.pack(pady=20)


        self.gif_label.config(image=self.gif_frames[0])


        self.animation_running = False

    def update_gif(self, frame_index=0):
        """Function to update the GIF to show the next frame in the animation"""
        if self.animation_running:
            self.gif_label.config(image=self.gif_frames[frame_index])
            frame_index = (frame_index + 1) % len(self.gif_frames)
            self.root.after(1000, self.update_gif, frame_index)

    def update_time(self):
        """Update the timer's display for the current session"""
        if self.running:
            self.elapsed_time = time.time() - self.start_time


            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            time_str = f"{minutes:02}:{seconds:02}"
            self.time_label.config(text=time_str)
            self.root.after(1000, self.update_time)

    def start_timer(self):
        """Start the timer and reset the current session"""
        if not self.running:
            self.start_time = time.time()
            self.elapsed_time = 0
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.animation_running = True
            self.update_gif()
            self.update_time()

    def stop_timer(self):
        """Stop the timer, accumulate the session time, and display total time"""
        if self.running:
            self.running = False
            self.total_time += self.elapsed_time
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.animation_running = False


            minutes = int(self.total_time // 60)
            seconds = int(self.total_time % 60)
            time_str = f"{minutes:02}:{seconds:02}"
            self.elapsed_time_label.config(text=f"Total Time: {time_str}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
