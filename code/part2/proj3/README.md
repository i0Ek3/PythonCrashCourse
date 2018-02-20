# Learning Log Developed Flows

The goal of this project is developed a web application--Learning Log.

## Features
* Record and append items
* Register and login
* Create new topic and check existed items

# Steps

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
pip(3) install --user virtualenv
```

## Activate Virtual Environment
```Shell
source ll_env/bin/activate
```
And run `deactivate` to stop virtual environment.

##  Install Diango
```Shell
pip(3) install Django
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
* Modified models.py and add class Topic:<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/classTopic.png)

### Activate Model
* Modified settings.py and add your application:<br>
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

### Use Django Manage Website
* Create Super User
```Shell
python(3) manage.py createsuperuser #create super user,username:ll_admin,passwd:python@123,others default
```
* Register Model for the Manage Website<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/admin.png)<br>

Then we can access manage website through `http://localhost:8000/admin/` and enter your username and passwd then you can see like this:<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/login.png)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/logged.png)<br>

* Add Topic
    * Click Topics entry topic page
    * Click Add to add something
    * Save
The picture like this:<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/addtopic.png)

### Define Model Entry
* Modified models.py and add class Entry:<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/entry.png)

### Migrate Model Entry
* Modified models.py
* python(3) manage.py makemigrations app_name
* python(3) manage.py migrate

### Register Entry to Manage Website
* Modified admin.py<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/adminEntry.png)<br>
* Add items to topics

### Django Shell
```Shell
python(3) manage.py shell
```
```Python
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
```
The picture like this:
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/DjangoShell.png)

## Create Page:Learning_logs Mainpage
In short,you need to do under these steps:
* Define URL:describe URL how to design
* Compile View
* Compile Template

### Reflect URL
* Add learning_log's url on /learning_log/urls.py.Don't forget header<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/log_urls.png)<br>
* Add urls.py under /learning_logs/<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/logs_urls.png)

### Compile View
* Add view on /learning_logs/views.py<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/view.png)

### Compile Template
* Create new folder whose named template under the learning_logs/
* Create new folder whose named learning_logs under the templates/
* Create a file whose named index.html and add something<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/index.png)<br>
Then you check http://localhost:8000/ again will show you under this:<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/indexhtml.png)

## Create Other Webpages

### Template Inherit
* Father Template
Create a base.html under the direction where the file index.html exisited.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/basehtml.png)

* Child Template
Rewrite index.html to inherit base.html.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/reindexhtml.png)

### Show Pages of All Topics
* URL Pattern
Revise urls.py under the learning_logs/<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/revise-urls.png)

### View<br>
Add codes on views.py.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/addtoview.png)

### Template<br>
Create a file whose named topics.html under the learning_logs/templates/learning_logs/.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/topichtml.png)

Revise father template.<br> 
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/revise-topic-2.png)<br>
Then you can see like under this while you access http://localhost:8000/topics/:<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/html4topics.png)

### Show Pages of Specific Topic
* URL Pattern<br>
Revise urls.py under learning_logs/.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/addIdToUrls.png)

* View<br>
Revise views.py under learning_logs/.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/addTopicToView.png)

* Template<br>
Create a file whoes named topic.html under learning_logs/templates/learning_logs/.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/newTopic.png)

* Set Every Topic As a Link on Pages of All Topics Shown<br>
Revise topics.html.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/addToTopics.png)<br>
Then access http://localhost:8000/topics/1/ you can see like under this:<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/showidhtml.png)



# Users Account

## Let Users Can Input Data

This step same as before web we created. 

### Add New Topic

- Tables As Add Topic<br>

We always use ModelForm to create table in Django.Now we create a file named forms.py and store it in the folder which is file models.py exisit.<br>

- URL Pattern *new_topic*

Add url() into urls.py under learning_logs/.<br>

- View Function new_topic()

Add somthing into views.py.<br>

- Request GET And POST
    - GET:read data only form server,null table
    - POST:users commit info from table,nonnull table

- Template new_topic

Create new file new_topic.html under learning_logs/templates/learning_logs/.<br>

- Link To Page new_topic

Add a link in topics to new_topic.<br>

![add new topic1](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ant1.jpg)<br>
![add new topic2](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ant2.jpg)<br>

### Add New Item








# Issues
It's hard to avoid some errors,if you find something wrong please tell me generously and welcome to issue me.Any others problem you can visit [Django Documents](https://docs.djangoproject.com/en/2.0/ 'welcome to click me!').
