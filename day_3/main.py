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


def find_common(data):
	bits = len(data[0]) -1 
	print('bits is: ', type(bits), 'and= ', bits)
	com = ''
	for i in range(bits):

		zeros, ones = get_majority(i, puzzle_data)

		if zeros > ones:
			com = com + '0' 
		elif zeros <= ones:
			com = com + '1'
	return com


def find_uncommon(common):
	uncom = ''
	print('gamma is of type: ', type(common))

	for ch in common:
			if ch == '0':
				uncom = uncom + '1'
			elif ch == '1':
				uncom = uncom + '0'

	return uncom


def bin_to_dec(str):
	dec = 0
	index = int(len(str)) - 1
	print('positions:', index)
	
	while index > 0:

		for ch in str:

			if ch == '1':
				dec += 2**index 
			index -= 1

	return dec


def eliminate(data):
	bits = len(data[0]) - 1
	print('bits = ', bits)
	while len(data) > 1:

		for i  in range(bits):
			zeros , ones = get_majority(i, data)

			if zeros > ones:
				eliminations = []
				# print('the most common value in the ', i, 'bit position is 0')
				for input in data:
					if input[i] != '0':
						eliminations = eliminations + [input]
						# print('elimination of: ', input)
					# else:
						# print('proceed to next element')
			elif zeros <= ones:
				eliminations = []
				# print('the most common value in the ', i, 'bit position is 1')
				for input in data:
					if input[i] != '1':
						eliminations = eliminations + [input]
						# print('elimination of: ', input)
					# else:
						# print('proceed to next element')
		
			for el in eliminations:
				data.remove(el)
			# print('eliminations are: ',eliminations, 'and we keep the numbers: ', data)

	data = data[0]
	return data
			


if __name__ == '__main__':
	with open('test.txt','r') as f:
		puzzle_data = f.readlines()

		gamma = find_common(puzzle_data)
		epsilon = find_uncommon(gamma)

		dec_gamma = bin_to_dec(gamma)
		dec_epsilon = bin_to_dec(epsilon)
		
		print('gamma: ',gamma,'=', dec_gamma , 'and epsilon: ', epsilon, '=',dec_epsilon)
		product = dec_gamma * dec_epsilon
		print('The answer to PART ONE is: ', product)

		# END OF PART ONE

		oxygen_gen_rating = bin_to_dec(eliminate(puzzle_data))
		print( 'oxygen_gen_rating is: ' , oxygen_gen_rating)








		





		

				
