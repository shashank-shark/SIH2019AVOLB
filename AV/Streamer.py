import argparse

import cv2
import zmq
import subprocess

from camera.Camera import Camera
from constants import PORT, SERVER_ADDRESS
from utils import image_to_string
from threading import Thread
from subprocess import Popen, PIPE


class Streamer:

    def __init__(self, server_address=SERVER_ADDRESS, port=PORT):

        print("Connecting to ", server_address, "at", port)
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.PUB)
        self.footage_socket.connect('tcp://' + server_address + ':' + port)
        self.keep_running = True

    def start(self):
        """
        Starts sending the stream to the Viewer.
        Creates a camera, takes a image frame converts the frame to string and sends the string across the network
        :return: None
        :Need to work here for SIH
        """
        print("Streaming Started...")
        # camera = Camera()
        # camera.start_capture()
        cap = cv2.VideoCapture(0)
        self.keep_running = True

        while self.footage_socket and self.keep_running:
            try:
                # frame = camera.current_frame.read()  # grab the current frame
                ret, frame = cap.read()
                image_as_string = image_to_string(frame)
                self.footage_socket.send(image_as_string)

            except KeyboardInterrupt:
                cv2.destroyAllWindows()
                break
        print("Streaming Stopped!")
        cv2.destroyAllWindows()

    def stop(self):
        """
        Sets 'keep_running' to False to stop the running loop if running.
        :return: None
        """
        self.keep_running = False


def main():
    print ("Entered usual process")
    port = PORT
    server_address = SERVER_ADDRESS

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server',
                        help='IP Address of the server which you want to connect to, default'
                             ' is ' + SERVER_ADDRESS,
                        required=True)
    parser.add_argument('-p', '--port',
                        help='The port which you want the Streaming Server to use, default'
                             ' is ' + PORT, required=False)

    args = parser.parse_args()

    if args.port:
        port = args.port
    if args.server:
        server_address = args.server

    streamer = Streamer(server_address, port)
    streamer.start()

def call_audio():
#    p = subprocess.call(['python','mic_server.py'],stdout=PIPE, stderr=PIPE)
    proc = Popen (['python','mic_client.py','localhost','4444'],shell=True,stdin=None,stdout=None,stderr=None,close_fds=True)
    # proc.communicate()
    print ("Child client process successfully generated")


if __name__ == '__main__':
    call_audio()
    main()