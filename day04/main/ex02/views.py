from django.shortcuts import render
from . import forms
from django.conf import settings
import logging


def get_history(request):
    f = open(settings.HISTORY_LOG_FILE, 'a')

    logger = logging.getLogger('history')
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(stream = f)
    handler.setFormatter(logging.Formatter(fmt='%(asctime)s: %(message)s'))
    logger.addHandler(handler)

    if request.method == 'POST':
        form = forms.LogHistory(request.POST)
        if (form.is_valid()):
            logger.info(form.cleaned_data.get('history_log'))
    f.close()
    historys = []
    with open(settings.HISTORY_LOG_FILE, 'r') as f:
        f = open(settings.HISTORY_LOG_FILE, 'r')
        historys = [line for line in f.readlines()]
    return render(request, 'ex02/index.html', {'form' : forms.LogHistory(), "historys" : historys})
