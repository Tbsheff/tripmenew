from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexPageView(request):
    lstData = [
        {
            "last_name": "Doe",
            "first_name": "John",
            "gpa": 3.87,
            "major": "Accounting",
        },
        {
            "last_name": "Lamb",
            "first_name": "Mary",
            "gpa": 3.91,
            "major": "Information Systems",
        },
        {
            "last_name": "Wheat",
            "first_name": "Buck",
            "gpa": 3.70,
            "major": "Marketing",
        },
        {
            "last_name": "Anderson",
            "first_name": "Greg",
            "gpa": 2.99,
            "major": "Fun",
        },
    ]

    context = {
        'school_name': 'BYU',
        'degrees': ["IS", "ACCT", "MKTG"],
        'data': lstData
    }

    return render(request, 'travelpages/index.html', context)
