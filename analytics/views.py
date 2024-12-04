from django.shortcuts import render
from surveys.models import Survey


def survey_analytics(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    responses = survey.responses.all()
    # Data processing to create graphs
    context = {'survey': survey, 'responses': responses}
    return render(request, 'analytics/survey_analytics.html', context)