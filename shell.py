import armanna

while True:
		text = input('armanna > ')
		result, error = armanna.run('<մուտք>', text)

		if error:
			print(error.as_string())
		else:
			print(result)