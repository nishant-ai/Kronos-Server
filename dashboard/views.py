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

    return Response({"satisfaction_rate": round(rate, 2)})

# @api_view(["GET"])
# def prods_by_sentiment(request):
#     sentiment = request.GET.get("sentiment")
#     objs = Sentiment.objects.filter(sentiment=sentiment)
#     comments = [obj.comment for obj in objs]

#     return Response(comments)
    

@api_view(["GET"])
def customer_count(request):
    count = Customer.objects.count()
    return Response({
        "customer_count": count
    })

@api_view(["GET"])
def total_revenue(request):
    revenue=0
    all_sales = Sale.objects.all()

    for sale in all_sales:
        product_price = sale.product.price
        revenue+=(product_price*sale.quantity)

    return Response({
        "revenue": revenue
    })


@api_view(["GET"])
def total_profit(request):
    profit=0
    all_sales = Sale.objects.all()

    for sale in all_sales:
        product_price = sale.product.price
        prduct_cost = sale.product.cost
        profit+=((product_price-prduct_cost)*sale.quantity)

    return Response({
        "profit": profit
    })
