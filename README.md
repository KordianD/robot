# TODO
- pobieranie portu i wieku
- zaserwować jako grę z javy
- timeout rozkazów dla robota (200 ms, requesty co 100 ms)


# Robot controller
Simple web server to control a robot.  
Detailed explanation in project Wiki.

# Prerequisites
To install everything what is needed, run following command in the main directory.
    
    git clone https://github.com/KordianD/robot
    
    cd robot
        
    pip install -r requirements.txt


# How to run
You need to perform several commands.

    cd src

    python app.py
    
# General 

This project uses `flask` as a web framework.
The default port which is mapped is `5000`.


# Development

If you want to develop code, you need several packages, simply run:

    pip install -r requirements_dev.txt
    
This packages enable running tests on the local machine.

To run tests:

    make test

To apply python linters  to be align with PEP8

    make fix
