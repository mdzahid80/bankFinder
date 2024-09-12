from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,request
import pandas as pd


df = pd.read_csv('../bankFinder/bank_branches.csv')

def search_data(request):
    keyword = request.GET.get('keyword', '')
    if keyword:
        # Perform search on the DataFrame
        results = df[df['branch'].astype(str).str.contains(keyword, case=False)]
    else:
        results = df
    # Convert results to JSON
    data = results.to_dict(orient='records')
    return JsonResponse(data, safe=False)