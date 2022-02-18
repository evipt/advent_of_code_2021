


if __name__ == '__main__':
	with open('input.txt','r') as f: 
		puzzle_data = f.readlines()

# PART ONE
		forwards = 0
		downs = 0 
		ups = 0
		aim = 0 
		for input in puzzle_data:

			#print(input)
			step = input.split()
			#print(step)

			command = step[0]
			#print("command: ", command)

			num = int(step[1])
			#print("ammount: ", num)

			if command == 'forward':
				forwards += num
			elif command == 'down':
				downs += num
			elif command == 'up':
				ups += num

		horizontal = forwards
		depth = downs - ups
		product = horizontal*depth

		print('The horizontal position is:', horizontal, ', the depth is:', depth, ' and the answer to PART ONE is:', product)


# PART TWO
	forwards = 0
	depth = 0
	aim = 0 
	for input in puzzle_data:

		# print(input)
		step = input.split()
		# print(step)

		command = step[0]
		# print("command: ", command)

		num = int(step[1])
		# print("ammount: ", num)

		if command == 'forward':
			forwards += num
			# print('for:',forwards)
			depth += aim * num
			# print('aim:',aim)
			# print('depth:',depth)
		elif command == 'down':
			aim += num
			# print('aim:',aim)
		elif command == 'up':
			aim -= num
			# print('aim:',aim)

	horizontal = forwards
	product = horizontal*depth

	print('The horizontal position is:', horizontal, ', the aim is:', aim, ', the depth is:', depth, ' and the answer to PART TWO is:', product)

	
