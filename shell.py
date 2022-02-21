import armanna

while True:
	text = input('armanna > ')
	result, error = armanna.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)