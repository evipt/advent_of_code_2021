

def compare(lis):
	n = 0

	for i in range(len(lis) - 1):
		if lis[i + 1] > lis[i]:
			n += 1
	return(n)	


def sliding_window(lis):
	# new auxiliary list
	sum_list = []

	# list of sums of triplets
	for i in range(len(lis) - 2):
		triplet = []
		for j in range(i, i + 3):
			triplet.append(lis[j])
			s = sum(triplet)
		# print(triplet, s)
		sum_list.append(s)
		s = 0
	return (sum_list)


if __name__ == "__main__":

	with open('input.txt','r') as f:
		depth_data = f.read()
		# print(type(depth_data))

	data_list1 = list(depth_data.split())
	data_list2 = list(map(int, data_list1))
	data_list3 = sliding_window(data_list2)
	
	ans1 = compare(data_list2)
	ans2 = compare(data_list3)

	print('The answer for part 1 is: ', ans1)
	print('The answer for part 2 is: ', ans2)


