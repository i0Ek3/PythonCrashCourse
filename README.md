# PythonCrashCourse

Python learning notes. This is not my first time to learn Python,but its my first time to write .py files on github. Uh...that's cool, reference only!

```Python
print("Hello Python!")

```
## Python之禅
    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
[...More](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/zenOfPython.md 'More')

## Purpose
Enhence my coding ability and develop a python game.Just for fun

## Architecture
```Python
>code
    >>part1
        >>>basis gramar
    >>part2
        >>>proj1
            >>>>Alien Invasion
        >>>proj2
            >>>>Data Visualization
        >>>proj3
            >>>>Web Application
```

## Python Frame
* [Django](https://www.djangoproject.com/)-A web frame tool to help you developed interactive website.

## Notes
* Something you should know about write functions:
    * 给函数指定描述名称,且只用小写字母和下划线,模块名也如此:
    ```Python
    def function_name(parameter list) //recommand
    def functionName(parameter list) //unrecommand
    ```
    * 给形参指定默认值时,等号两边不要有空格,对于函数调用中的关键字实参也如此:
    ```Python
    def function_name(parameter1,parameter2='default value')
    function_name(value1,value2='value')
    ```
    * 不建议一行代码过长(>78字符),如果过长可使用回车后添加两个tab键:
    ```Python
    def make(
            parameter1,parameter2,parameter3,
            parameter4,parameter5,parameter6):
        function body... 
    ```
    * 所有的import都应该放在文件开头,除非文件开头使用了注释.
    * 在Python2.7中,类的创建如下:
    ```Python
    class ClassName(object):
        --snip--
    ```
    * 类名应采用驼峰命名法,即将类名中的每个单词首字母都大写,而不使用下划线．
    * 实例名和模块名都应采用小写+下划线的格式.
    * 对于每一个类,类定义后都应包含一个文档字符串.
    * 需要同时导入标准库模块和第三方及个人模块时,应先编写标准库模块语句后添加一个空行，再编写个人及第三方模块.


## Instances
[click me](https://github.com/i0Ek3/PythonCrashCourse/tree/master/code/part1)


## Updates
>2017
>>11-14:add function<br>
>>11-16:just add something about function,add other contents later...<br>
>>11-19:add class contents.<br>
>>11-20:add inherit contents.<br>
>>11-21:add something later.Like import part.<br>
>>11-22:add file operation and exception contents.<br>
>>11-24:add how to stored data use json.And add test model after my class end today!Actually thays really waste time to write,but I finished something and remains I commit tommorow!Thats all.<br>
>>11-25:no update cause of my pc-computer was broken!<br>
>>11-26:add something about unittest,but still have boom in exc.py,fix later...review day<br>
>>11-27:add part2.<br>
>>12-03:I'm back and modified something.<br>
>>12-04:add something about Django.<br>
>>12-05:add main page on application.<br>
>>[More...](https://github.com/i0Ek3/PythonCrashCourse/blob/master/code/updates.md 'More')
