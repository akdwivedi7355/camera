from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Line
from kivy.graphics.texture import Texture
import cv2

class CameraApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)  # Open the first camera
        self.visible = True

        # Main layout (vertical box layout)
        self.main_layout = BoxLayout(orientation='vertical')

        # Camera feed layout (top section)
        self.camera_layout = BoxLayout(size_hint_y=0.9)
        self.image = Image()
        
        # Draw a frame outline around the camera feed
        with self.image.canvas.before:
            self.frame_color = Color(1, 0, 0, 1)  # Red color
            self.frame = Line(width=2, close=True)
        
        # Bind the update of the frame outline to size and pos changes of the image
        self.image.bind(size=self._update_frame, pos=self._update_frame)
        
        self.camera_layout.add_widget(self.image)
        self.main_layout.add_widget(self.camera_layout)

        # Button layout (bottom section, vertical orientation)
        self.button_layout = BoxLayout(size_hint_y=0.1, orientation='vertical')
        
        # Create attractive buttons
        self.attendance_button = Button(text="Mark Attendance", background_color=(0.2, 0.6, 0.3, 1), size_hint_y=None, height=50)
        self.record_button = Button(text="Record", background_color=(0.2, 0.6, 0.8, 1), size_hint_y=None, height=50)
        self.register_button = Button(text="Register", background_color=(0.8, 0.6, 0.2, 1), size_hint_y=None, height=50)
        
        # Add padding and font size to buttons for better appearance
        for button in [self.attendance_button, self.record_button, self.register_button]:
            button.font_size = 20
            button.padding = (10, 10)

        # Bind button actions
        self.attendance_button.bind(on_press=self.mark_attendance)
        self.record_button.bind(on_press=self.record)
        self.register_button.bind(on_press=self.register)

        # Add buttons to the button layout
        self.button_layout.add_widget(self.attendance_button)
        self.button_layout.add_widget(self.record_button)
        self.button_layout.add_widget(self.register_button)

        # Add button layout to the main layout
        self.main_layout.add_widget(self.button_layout)

        Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update at 30 fps

        return self.main_layout

    def update(self, dt):
        if self.visible:
            ret, frame = self.capture.read()
            if ret:
                buf = cv2.flip(frame, 0).tobytes()
                texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.image.texture = texture

    def mark_attendance(self, instance):
        # Implement the logic to mark attendance here
        print("Mark Attendance button pressed")

    def record(self, instance):
        # Implement the logic to record here
        print("Record button pressed")

    def register(self, instance):
        # Implement the logic for registration here
        print("Register button pressed")

    def _update_frame(self, *args):
        # Update the frame coordinates to match the size of the image widget
        self.frame.points = [0, 0, self.image.width, 0, self.image.width, self.image.height, 0, self.image.height]

    def on_stop(self):
        self.capture.release()  # Release the camera when the app is closed

if __name__ == "__main__":
    CameraApp().run()
