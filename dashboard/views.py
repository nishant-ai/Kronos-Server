from rest_framework.decorators import api_view
from rest_framework.response import Response
from kronos.models import *
from django.db.models import Count, Sum
from kronos.serializers import *

# Dashboard APIs
@api_view(["GET"])
def satisfaction_rate(request):
    pos_count = Sentiment.objects.filter(sentiment="POS").count()
    neg_count = Sentiment.objects.filter(sentiment="NEG").count()
    rate = (pos_count*100)/(pos_count+neg_count)

    return Response({"satisfaction_rate": round(rate, 2)})

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

@api_view(["GET"])
def gender_composition(request):
    male_count = Customer.objects.filter(gender="M").count()
    female_count = Customer.objects.filter(gender="F").count()
    total_customers = Customer.objects.count()

    return Response({
        "male_compo": (male_count*100)/total_customers,
        "female_compo": (female_count*100)/total_customers,
        "others_compo": ((total_customers-male_count-female_count)*100)/total_customers
    })

@api_view(["GET"])
def age_groups(request):
    under_25 = Customer.objects.filter(age__lte=25).count()
    under_40 = Customer.objects.filter(age__lte=40, age__gte=26).count()
    under_75 = Customer.objects.filter(age__lte=75, age__gte=41).count()

    return Response({
        "under_25": round((under_25*100)/(under_25+under_40+under_75), 2),
        "under_40": round((under_40*100)/(under_25+under_40+under_75), 2),
        "under_75": round((under_75*100)/(under_25+under_40+under_75), 2)
    })

@api_view(["GET"])
def latest_orders(request):
    latest_orders = Sale.objects.order_by('-created_at')[:6]
    orders = []

    for order in latest_orders:
        orders.append({
                        "product": order.product.name,
                       "customer": order.customer.name,
                       "created_at": str(order.created_at)[:11],
                        "quantity": order.quantity
                       })

    return Response(orders)

@api_view(["GET"])
def latest_products(request):
    latest_products = Product.objects.order_by('-created_at')[:6]
    serializer = ProductSerializer(latest_products, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def high_perf_prods(request): 
    # Perform left join and aggregation to get highest selling products
    highest_selling_products = Product.objects.annotate(
        sale_count=Sum('sale__quantity')
    ).order_by('-sale_count')

    # Serialize the data
    serializer = ProductSaleSerializer(highest_selling_products, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def low_perf_prods(request): 
        # Perform left join and aggregation to get least selling products
        least_selling_products = Product.objects.annotate(
            sale_count=Sum('sale__quantity')
        ).order_by('sale_count')

        # Serialize the data
        serializer = ProductSaleSerializer(least_selling_products, many=True)

        return Response(serializer.data)


# PRODUCT PAGE
# @api_view(["GET"])
# def prods_by_sentiment(request):
#     sentiment = request.GET.get("sentiment")
#     objs = Sentiment.objects.filter(sentiment=sentiment)
#     comments = [obj.comment for obj in objs]

#     return Response(comments)

@api_view(["GET"])
def comments_by_prod(request):
    sentiment = request.GET.get("sentiment")
    product = request.GET.get("product")

    if sentiment == "ALL":
        comments = Sentiment.objects.filter(product=product)
    else:
        comments = Sentiment.objects.filter(sentiment=sentiment, product=product)
    serializer = SentimentSerializer(comments, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)

    return Response(serializer.data)