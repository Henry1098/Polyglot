from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import stripe

stripe.api_key = "sk_test_51LBc0LEg496HVlR1e7fdZCjaZe4aH4hU6GNWfQkAAZw7v8Ql9rikdGOtiqhRfAWoXpN8HNG3GdFYuiXv2zoKHyUV00IwMt4cEc"


@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
    amount=1000, currency='pln', 
    payment_method_types=['card'],
    receipt_email='test@example.com')
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)
