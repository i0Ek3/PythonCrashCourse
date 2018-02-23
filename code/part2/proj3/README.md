# Learning Log Developed Flows

The goal of this project is developed a web application--Learning Log.<br>

**ATTENTION!!!All of root folder leaning_log/ mentioned in this README.md same as my folder proj3/,please note.**

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
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ant-add.jpg)<br>

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
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ant3.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ant4.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ant5.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ant6.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ant7.jpg)<br>


### Add New Item

- Tables As Add Item

We need to create a table which is related with model Entry but high coustomlizition than TopicForm.<br> 

- URL Partten new_entry()

- View Function new_entry()

It's just look like new_topic().<br>

- Template new_entry

Looks like template new_topic.<br>

- Link To Page new_entry

We should add a link to page new_entry which shown special topic.<br>


### Edit Item

- URL Pattern edit_entry

Revise /learning_logs/ulrs.py to transfer item id you want to edit.<br>

- View Function edit_entry()

Edit views.py to make changes can save into database.<br>

- Template edit_entry

edit_entry.html looks same as new_entry.html.<br>

- Link To page edit_entry

Add link to page edit_entry for every item.<br>


## Create User Account

### Create New Application *users*

Use command to create as follows:<br>
```Shell
$ python manage.py startapp users
```

- Add Application users Into settings.py

Add this new application into INSTALLED_APPS in file /learning_log/settings.py.Then Django will include this application in project.<br>

- A URL Includes Application users

Now we need to revise urls.py in /learning_log to make it includes defined URL for application users.<br>

### Login Page

This step we will use default login view to implement the function of login page supported by Django.We do so,the pattern URL will differ with before.Under folder /learning_log/users,create a new file named urls.py and add codes.<br>

- Template login.html

We should create a new folder templates under learning_log(my folder is proj3/)/users/,as well as create a new folder users under templates/.<br> 

- Link To Login Page

Add link to login page in learning_logs/templates/learning_logs/base.html.<br> 

- Use Login Page

Please visit http://localhost:8000/admin/ to check our login page whether work.If that page not work well please close last command first and re-run it.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/login_page.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/login_page1.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/login_page2.jpg)<br>


### Logout

Now we need to define a pattern URL for logout link to make users logout easily.<br>

- Logout URL

Define a URL pattern for logout in learning_log/users/urls.py.<br>

- View Function logout_view()

Function logout_view() is sample just import and call logout() form Django then redirect it to homepage.Now we should revise users/views.py and add codes.<br>

- Link To Logout View

Now we need to add a logout link in base.html.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/logout_page.jpg)<br>

### Register Page

Next we will create a page make users who can register for it as well as we use table UserCreationForm to write ourself function and template of view which is supported by Django.<br> 

- The URL Pattern of Register Page

Now we need to revise users/urls.py to define the URL pattern of register page.<br>

- View Function register()

`register()` need to display a null register table when register page first time to be requested,then process the table when users comnmitted.Now we should add codes in /users/views.py.<br>

- Template Register

Similar with template of login page,write a register.html and save it into folder which login.html exist.<br> 

- Link To Register Page

We add codes to show unregister users register page in base.html.<br>

![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/register.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/register1.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/register-test.jpg)<br>

Now we finished user login,logout,register function,the next we will make users have their own independent data,let us wait and see what happens!<br>


## Make Users Have Their Own Independent Data

We will create a system to make users enable input their spefic data then shows different page to different users according by data whose belonged.<br> 

### Use @login_required to Limit Access

@login_required is a decorator supported by Django,it can be easily implement the gogal above.<br>

- Limit Access To topics Page

We need revise codes in /learning_logs/views.py to limit access and revise codes in /learning_log/settings.py to redirect unlogin users to login page.<br>

- Limit Access To Project 'Learning_log' Fully

To protect some page avoid dangers we should limit access fully.So we should add @login_required for all views expect view index() in /learning_logs/views.py.<br>

- Relevance Data To Users

We just need to relevance high level data to users，that is to say we need relevance topic.So we need to revise model Topic to add a foreign key in /learning_logs/models.py..<br>

- Ensure Users

Now we should check all users ID we created by commands follows:<br> 
```Shell
$ python manage.py shell
>>> from django.conrtib.auth.models import User
>>> User.objects.all()
>>> for user in User.objects.all():
...     print(user.username, user.id)
...     
(u'll_admin', 1)
(u'test, 2) 
```
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ensure_users.jpg)<br>


- Migrate Database
```Shell
$ python manage.py makemigrations learning_logs
$ python manage.py migrate
```
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/migrate_databse.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/migrate.jpg)<br>
When done,you should do this on last django shell:<br>
```Shell
>>> from learning_logs.models import Topic
>>> for topic in Topic.objects.all():
...     print(topic, topic.owner)
...
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/ensure_migrate.jpg)<br>
```

### Only Users Access Their Own Topic

Current suiation we can visit all topic we want,now let us change this suiation.So you should revise code in /learning_logs/views.py.<br>

### Protect Topic Form Users

Revise  /learning_logs/views.py to check requested topic belonged to current user.<br>

### Relevance New Topic To Current User

Actually you will see an IntegrityError when you add a new topic.That's means you must assign a value for owner segment when you add a new topic.So we need to revise codes in /learning_logs/views.py.<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/intergtityerror.jpg)<br>
![](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/part2/proj3/pic/add_new_topic.jpg)<br>

## Style And Deploy

- Install django-bootstrap3
```Shell
$ sudo pip install django-bootstrap3
```
    - revise settings.py and application under the INSTALLED_APPS

- Use Bootstrap Set Project Style
    - revise base.html with bootstrap template
    - revise /learning_logs/templates/learning_logs/login.html with jumbotron
    - set topic page style:revise new_topic.html
    - set topics page style:revise topics.html
    - set item style in topic page

- Deploy
    - Use Heroku To Deploy
        - visit https://heroku.com/ to register a new account
        - install heroku toolbet
        ```Shell
        $ brew install heroku/brew/heroku
        ```
        - install dependencies
        ```Shell
        $ sudo pip install dj-database-url dj-static static3 gunicorn
        ```
    - create a file named requirements.txt which includs package list
    ```Shell
    $ pip freeze > requirements.txt
    ```
        - add this line `psycopg2>=2.7.4` in requirements.txt
    - appoint python version
        - create a new file named `runtime.txt` in root folder
    - revise settings.py
    - create a file named `Procfile` for boot progress in root folder
    - revise wsgi.py with Cling
    - create a folder `static` to store static files under learning_log/
    - use gunicorn server on local
    ```Shell
    $ heroku local
    ```
    - use git to track project files
        - config git(help yourself)
    - commit project
    - push to Heroku
    ```Shell
    $ heroku login
    $ heroku create
    $ git push heroku master
    $ heroku ps
    $ heroku open
    ```


# Issues
It's hard to avoid some errors,if you find something wrong please tell me generously and welcome to issue me.Any others problem you can visit [Django Documents](https://docs.djangoproject.com/en/2.0/ 'welcome to click me!').
