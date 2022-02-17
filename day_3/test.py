def get_majority(n, data):

	z = 0
	o = 0

	for input in data:
		# print(input)

		if input[n] == '0':
			z += 1
		else:
			o += 1

	return z, o


def eliminate(data):
	bits = len(data[0]) - 1
	print('bits = ', bits)
	while len(data) > 1:

		for i  in range(bits):
			zeros , ones = get_majority(i, data)

			if zeros > ones:
				eliminations = []
				print('the most common value in the ', i, 'bit position is 0')
				for input in data:
					if input[i] != '0':
						eliminations = eliminations + [input]
						print('elimination of: ', input)
					else:
						print('proceed to next element')
			elif zeros <= ones:
				eliminations = []
				print('the most common value in the ', i, 'bit position is 1')
				for input in data:
					if input[i] != '1':
						eliminations = eliminations + [input]
						print('elimination of: ', input)
					else:
						print('proceed to next element')
		
			for el in eliminations:
				data.remove(el)
			print('eliminations are: ',eliminations, 'and we keep the numbers: ', data)

	return data 


if __name__ == '__main__':
	with open('test.txt','r') as f:
		puzzle_data = f.readlines()
		
		# a = '10110'
		
		# indeces = [i for i, x in enumerate(a) if x == '1']

		# print(indeces)

		oxygen = eliminate(puzzle_data)	
		print('oxygen = ', oxygen)

# FIRST ATTEMPT FOR PART TWO

	# def eliminate(str, data):
	# 	eliminations = []
	# 	for i in range(5):
	# 		print('i is:', i)

	# 		for input in data:
	# 			print('element is:', input)
	# 			# print(type(input), input, type(str), str[0])
	# 			print('gammas i-st ch is:', str[i],'while datas i-st ch is:' ,input[i])
				

	# 			if input[i] != str[i]:
	# 				eliminations = eliminations + [input]
	# 			print('eliminations is: ', eliminations)				

	# 			# print('positions is: ',positions)
	# 		for el in eliminations:
	# 			# print(data[el])
	# 			data.remove(el)


				# if input[i] != str[i]:
				# 	print('we found difference in chars: ', str[i], 'NET', input[i])
				# 	print('we are going to remove: ', input)
				# 	data.remove(input)
				# else:
				# 	print('we proceed to the next element')

		# 	print('now the data we get is: ', data)
		# 	eliminations = []
		# return data 

# 2ND ATTEMPT ON PART TWO 

	
	
	

