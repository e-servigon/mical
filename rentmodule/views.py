from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from .models import *
from .forms import * 

def home (request):
    return render(request,'home.html',{})
