from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, authenticate, login
import pandas as pd
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Create your views here.
def login(request):
    return HttpResponse("Good work boi")