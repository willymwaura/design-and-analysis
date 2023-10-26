from django.shortcuts import render, redirect
from .stack import Stack
import random
from django.urls import reverse
from django.http import HttpResponse

# Initialize the stack
stack = Stack()

def index(request):
    elements = stack.items
    context = {
        'stack_length': stack.length(),
        'stack_elements': elements,
        'message': request.session.get('message', ''),  # Get the message from the session
    }
    return render(request, 'template/index.html', context)

def push(request):
    random_number = random.randint(1, 100)
    stack.push(random_number)
    request.session['message'] = "Pushed an element: " + str(random_number)  # Set the message in the session
    return redirect('index')  # Redirect to the index view

def pop(request):
    if not stack.is_empty():
        stack.pop()
        request.session['message'] = "Popped an element"  # Set the message in the session
        return redirect('index')  
    else:
        request.session['message'] = "The stack is empty"  # Set the message in the session
        return redirect('index')  
        

def top(request):
    top_item = stack.top()
    if top_item is not None:
        request.session['message'] = "Top item: " + str(top_item)
        return redirect('index')  
    else:
        request.session['message'] = "Stack is empty"
        return redirect('index')   # Redirect to the index view

def is_empty(request):
    if stack.is_empty():
        request.session['message'] = "True"
        return redirect('index')  
    else:
        request.session['message'] = "False"
        return redirect('index')  

def length(request):
    stack_length = stack.length()
    request.session['message'] ="Stack Length: " + str(stack_length)
    return redirect('index')
