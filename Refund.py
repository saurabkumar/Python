import razorpay
client = razorpay.Client(auth=("rzp_test_siY3oWUoOfReQu", "SycxzTuEmSm3sZ6HmDIbV9jo"))
payment_id = "pay_IohRfn5wSd7NpT"
payment_amount = 1000
speed='optimum'
value = client.payment.refund(payment_id, payment_amount,speed)
#Refund with Extra Parameters
notes = {'key': 'value'}
print(value)