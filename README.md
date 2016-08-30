# awmachine

Website

## Getting started

Getting the app up and running on your localhost

### Install pip

````bash
apt install pip # debian / ubuntu
easy_install pip # mac (may have to use sudo)
````

### Install virtualenv (if not installed)

````bash
sudo pip install virtualenv
````

### Clone and serve

`````bash
git clone https://github.com/apongos/awmachine
cd awmachine
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py runserver # serve on port 8000, view in browser; Ctrl+C to kill process
deactivate # turn off virtual environment
````
