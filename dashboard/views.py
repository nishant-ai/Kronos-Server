from rest_framework.decorators import api_view
from rest_framework.response import Response
from kronos.models import *
from kronos.serializers import *

# Dashboard APIs
@api_view(["GET"])
def satisfaction_rate(request):
    pos_count = Sentiment.objects.filter(sentiment="POS").count()
    neg_count = Sentiment.objects.filter(sentiment="NEG").count()
    rate = (pos_count*100)/(pos_count+neg_count)

    return Response({"satisfaction_rate": rate})

@api_view(["GET"])
def prods_by_sentiment(request):
    sentiment = request.GET.get("sentiment")
    objs = Sentiment.objects.filter(sentiment=sentiment)
    comments = [obj.comment for obj in objs]

    return Response(comments)