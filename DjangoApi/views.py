from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from DjangoApi.models import Language
from .forms import LangaugeForm
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Create your views here.

data = pd.read_csv("DjangoApi\media\dataset.csv")
x = np.array(data["Text"])
y = np.array(data["language"])
cv = CountVectorizer()
X = cv.fit_transform(x)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.33,random_state = 42)
model = MultinomialNB()
model.fit(X_train,y_train)


def result(language):
    data = cv.transform([language]).toarray()
    output = model.predict(data)
    return output
def home(request):
    return render(request,'base.html')
def formView(request):
    if request.method=='POST':
        form = LangaugeForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            output = result(language)
            return render(request,'forms.html',{'output':f'This Language is {output[0]}'})
        
  
    form=LangaugeForm()
    return render(request, 'forms.html', {'form':form})