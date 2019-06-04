# Robot controller
Simple web server to control a robot.  
Detailed explanation in project Wiki.

# Prerequisites
To install everything what is needed, run following command in the main directory.
    
    git clone https://github.com/KordianD/robot
    
    cd robot
        
    pip install -r requirements.txt
# How to run

## Linux
Connect the robots to PC using bluetooth.  
Add the robot Bluetooth MAC addresses to `mac_addresses.py`.  
Remember to check if ports for both servers are open.  
Run commands:  

    cd src

    python app.py

## Windows
Create COM ports for each robot (in bluetooth settings).  
Add the robot COM ports addresses to `mac_addresses.py`.  
Remember to check if ports for both servers are open.  
Run commands:  

    cd src

    python app.py

    
# General 

This project uses `flask` as a web framework.
The default port `5000`, you can change it using `--port N` command.
In `config.py` you can change maximum robot speed.


# Development

If you want to develop code, you need several packages, simply run:

    pip install -r requirements_dev.txt
    
This packages enable running tests on the local machine.

To run tests:

    make test

To apply python linters  to be align with PEP8

    make fix
