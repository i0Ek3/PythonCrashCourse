# Learning Log Developed Flows

The goal of this project is developed a web application--Learning Log.

## Features
    * Record and append items
    * Register and login
    * Create new topic and check existed items


## Build Virtual Environment
```Shell
python(3) -m venv ll_env
```
If created not successed maybe you should check your syetem whether have related dev packages:
```Shell
sudo apt-get install python3-venv pip(3)
```
Or run:
```Shell
pip install --user virtualenv
```

## Activate Virtual Environment
```Shell
source ll_env/bin/activate
```
And run `deactivate` to stop virtual environment.

##  Install Diango
```Shell
pip install Django
```
##  Create new project under the Django
```Shell
django-admin.py startproject learning_log .
```
Then you can use commands `ls` and `ls learning_log` to check files created just now.

##  Create Database
You can run under command to create database
```Shell
python(3) manage.py migrate
```
Then use `ls` to check it!

##  Check Project
```Shell
python(3) manage.py runserver
```
Then the picture like this:

![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/django-powered.png)

If not and with error `That port is already in use`,please run command `python(3) manage.py runserver port` to change your port until avaiable.

## Create Application
Open a new terminal and change the directory where is `manage.py` in there.
```Shell
source ll_env/bin/activate #activate environment
python(3) manage.py startapp learning_logs #build the enssencial dev
```
Then use commands `ls` and `ls learning_logs` to look what is generated.

### Define Model
* Modified models.py and add class Topic:
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/classTopic.png)

### Activate Model
* Modified settings.py and add your application:
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/applications.png)

Then under the directory of manage.py to run command:
```Shell
python(3) manage.py makemigrations learning_logs #let Django ensure how to revise database
python(3) manage.py migrate #apply this migrate let Django to revise database
```
So every time you should execute under three steps while you need to revise the datas managed by 'Learning_logs':
* modified models.py
* call makemigrations to learning_logs/
* make Django migrate project

