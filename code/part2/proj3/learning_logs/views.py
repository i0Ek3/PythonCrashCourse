from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm
# Create your views here.

def index(request):
    """Mainpage of Learning_logs"""

    return render(request,'learning_logs/index.html')

def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    """show single topic and it's all items"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

def new_topic(request):
    """add new topic"""
    if request.method != 'POST':
        #uncommit data then create new table
        form = TopicForm()
    else:
        # data committed by POST,procrssing data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request,'learning_logs/new_topic.html',context)






