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


