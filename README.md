
# robot controller
Simple web server to control a robot. 


# How to run
You need to perform several commands.

    git clone https://github.com/KordianD/robot

    cd robot/src

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