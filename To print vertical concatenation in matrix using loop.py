test_list = [["Akbar", "is"], ["not", "good"], ["boy"]]

print("The original list : " + str(test_list))

res = []
N = 0
while N != len(test_list):
	temp = ''
	for idx in test_list:
		
		try: temp = temp + idx[N]
		except IndexError: pass
	res.append(temp)
	N = N + 1

res = [ele for ele in res if ele]

print("List after column Concatenation : " + str(res))