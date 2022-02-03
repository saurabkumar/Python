import razorpay

client = razorpay.Client(auth=("rzp_test_siY3oWUoOfReQu", "SycxzTuEmSm3sZ6HmDIbV9jo"))

value=client.order.payments(order_id="order_IbBVRU6YTWx2mt")

# value=client.order.payments("order_IbBVRU6YTWx2mt")

# value=client.payment.fetch("pay_IS6vpoblags0pb")

# Value=client.order.fetch("order_IbBVRU6YTWx2mt")

print(value)