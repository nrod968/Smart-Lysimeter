#!/bin/bash
echo "Starting GUI Now"
cd /home/pi/Smart-Lysimeter/
source venv/bin/activate
sudo python3 main.py
deactivate
