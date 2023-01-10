from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    # Home page for Learning Log
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    # Show all topics
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    # Show a single topic and all its entries
    topic = Topic.objects.get(id=topic_id)
    check_topic_user(topic.owner, request.user)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    # Add a new topic
    if request.method != 'POST':
        print(f"Doing {request.method} on new_topic")
        # No data submittied
        form = TopicForm()
    else: 
        # POST data submittied
        form = TopicForm(data=request.POST)
        print(f"Doing {request.method} on new_topic")
        if form.is_valid():
            # form.save()
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    # Add a new entry for a topic
    topic = Topic.objects.get(id=topic_id)

    check_topic_user(topic.owner, request.user)
    
    if request.method != 'POST':
        # No data submitted
        print(f"Doing {request.method} on new_entry")
        form = EntryForm()
    else: 
        print(f"Doing {request.method} on new_entry")
        # POST data submitted
        form = EntryForm(data=request.POST)
        if form.is_valid:
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
    
@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_user(topic.owner, request.user)

    if request.method != 'POST':
        # Form, prefill with current entry
        form = EntryForm(instance=entry)
    else: 
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)
    
def check_topic_user(owner, user):
    if owner != user:
        raise Http404