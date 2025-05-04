from kachaka_api import KachakaApiClient
from google import genai

# Initialize Google genAI client
client = genai.Client(api_key="AIzaSyBmCYnioteR-kyXW-fhtr6H0Afd3vyws58")  # Replace with a secure key storage method

myfile = client.files.upload(file="/home/rakesh/Audio/2025-04-21-13-45-59.mp3")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["If the speaker wants the robot to come to the kitchen, return '1'. Otherwise, return '0'.", myfile]
)

print(response.text)

if response.text == "1":
    # Initialize Kachaka API client
    client = KachakaApiClient(target="172.30.21.96:26400")

    # Check the robot's current pose
    try:
        current_pose = client.get_robot_pose()
        print(f"Current pose: {current_pose}")
    except Exception as e:
        print(f"Error fetching robot pose: {e}")

    # Example of existing operations
    client.speak("Hello, moving now!")
    client.move_forward(0.5)

    # Additional API functionalities
    def rotate(self, angle_degrees):
        """Rotates the robot by a given angle in degrees."""
        request = pb2.RotateRequest(angle=angle_degrees)
        response = self.stub.Rotate(request)
        return response.status

    def get_battery_status(self):
        """Returns the battery status of the robot."""
        request = pb2.EmptyRequest()
        response = self.stub.GetBatteryStatus(request)
        return {"level": response.level, "charging": response.charging}

    def control_led(self, state, color=None):
        """Controls the robot's LED lights."""
        request = pb2.LedControlRequest(state=state, color=color)
        response = self.stub.LedControl(request)
        return response.status

    def play_sound(self, sound_file):
        """Plays a specified sound file on the robot's speaker."""
        request = pb2.PlaySoundRequest(file_path=sound_file)
        response = self.stub.PlaySound(request)
        return response.status

    def follow_path(self, path_coordinates):
        """Commands the robot to follow a series of waypoints."""
        request = pb2.FollowPathRequest(coordinates=path_coordinates)
        response = self.stub.FollowPath(request)
        return response.status

    # Example usage of new functionalities
    client.rotate(90)  # Rotate 90 degrees clockwise
    battery_status = client.get_battery_status()
    print(f"Battery status: {battery_status}")
    client.control_led("ON", [255, 0, 0])  # Turn on LED to red
    client.play_sound("/home/rakesh/sounds/alert.wav")
    client.follow_path([(0.0, 0.0), (1.0, 1.0), (2.0, 0.0)])  # Follow a triangular path

# ROS Environment Activation
# Ensure proper setup activation before running the script:
# source /opt/ros/<distro>/setup.bash
# conda activate kachaka_env


# source ~/anaconda3/bin/activate
# conda activate kachaka_env
# python3 test.py

# gemini api key : AIzaSyBmCYnioteR-kyXW-fhtr6H0Afd3vyws58