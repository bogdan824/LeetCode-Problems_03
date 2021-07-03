"""
There is a restaurant with a single chef. You are given an array customers, 
where customers[i] = [arrivali, timei]:
- arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
- timei is the time needed to prepare the order of the ith customer.

When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. 
The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
"""

def average_waiting(customers):
	new_order_time = customers[0][0]
	total_time = 0

	for i in range (len(customers)):
		
		arrival_time = customers[i][0]
		#print("arrival_time",arrival_time)
		time_2cook = customers[i][1]
		#print("time_2cook",time_2cook)

		if arrival_time > new_order_time:
			new_order_time = arrival_time
		
		new_order_time += customers[i][1]
		#print("new_order_time",new_order_time)
		total_time += new_order_time - arrival_time
		#print("total_time",total_time)

		#print("---")
		
	print((total_time//len(customers)))
	


#customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]
average_waiting(customers)