import asyncio
import os

from viam.module.module import Module
from models.person_detector import PersonDetector

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.camera import Camera
from viam.services.mlmodel import MLModelClient
from viam.services.vision import VisionClient

# Set API key as environment variable
# API_KEY = os.getenv("VIAM_API_KEY", "")
# API_KEY_ID = os.getenv("VIAM_API_KEY_ID", "")

async def connect():
    opts = RobotClient.Options.with_api_key( 
        # Use below when testing with API key as environment variable
        # api_key=API_KEY,
        # api_key_id=API_KEY_ID,
        # Use below when testing with API key hardcoded
        # Replace "<API-KEY>" (including brackets) with your machine's api key 
        api_key='<API-KEY>',
        # Replace "<API-KEY-ID>" (including brackets) with your machine's api key id
        api_key_id='<API-KEY-ID>'
    )
    return await RobotClient.at_address('paige-machine-main.fyqbtxpbvl.viam.cloud', opts)

async def main():
    machine = await connect()

    person_detected = 0  # initialize first and set to false
    # Create vision_person_detector  
    vision_person_detector = PersonDetector.from_robot(machine, "vision_person_detector")
    # Get detections from camera where "my_camera" is the name of your connect
    person_detector_return_value = await vision_person_detector.get_detections_from_camera("my_camera")    

    # Check if there are any detections
    if person_detector_return_value:
        # Loop through detections to find a person
        for detection in person_detector_return_value:
            if detection.confidence > 0.6 and detection.class_name == "Person":
                person_detected = 1
                break

    print(f"person_detected: {person_detected}")


    # close machine 
    await machine.close()

if __name__ == '__main__':
    asyncio.run(main())
