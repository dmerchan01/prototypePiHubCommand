# Project Title: PiHubCommand

## Introduction
PiHubCommand is a voice-controlled interface for Raspberry Pi that allows users to interact with hardware components like LEDs and motors through spoken commands. This project leverages Python, speech recognition technologies, and GPIO interfacing to create an accessible and functional prototype.

## Requirements

### Hardware
- Raspberry Pi 4 Model B
- USB Microphone
- Speakers
- LEDs, resistors, and wires
- Breadboard

### Software
- Raspbian OS
- Python 3.x
- Required Python libraries:
  - RPi.GPIO
  - speech_recognition
  - gTTS
  - pygame (for audio output)

## Installation

1. **Set up Raspberry Pi**: Install Raspbian OS on your Raspberry Pi and connect it to the internet.
2. **Install Python Libraries**: Run the following commands in your terminal to install the required libraries:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install RPi.GPIO speech_recognition gTTS pygame
   pip3 install speech recognition
   pip3 install gtts
   pip3 install subproccess

## Code

1. **Copy and Run**: Take the code called prototype.py and run it with the Microphone and speakers connected. 
