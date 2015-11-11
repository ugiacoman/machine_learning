import enchant
import os
import time
import tokens

def main():
	start_time = time.time()
	settings = open("settings.txt", "r")
	ham_path = ""
 	spam_path = ""

	for line in settings:
		line = line.split()
		if line[0] == "ham_path:":
			ham_path = line[1]
		else:
			spam_path = line[1]

	"""Parse Ham emails"""
	# Splits string into list of strings and lowercases them
	h_text = tokens.parse_instances(ham_path)

	# Gets count of each string
	h_c_text = tokens.getCount(h_text)

	# Eliminates strings we don't want to count
	h_d_text = tokens.discriminate(h_c_text)
	h_N = len(h_d_text) 

	"""Parse Spam emails"""
	# Splits string into list of strings and lowercases them
	s_text = tokens.parse_instances(spam_path)

	# Gets count of each string
	s_c_text = tokens.getCount(s_text)

	# Eliminates strings we don't want to count
	s_d_text = tokens.discriminate(s_c_text)
	s_N = len(s_d_text) 
	M = h_N + s_N

	h_p_text = tokens.probablity(h_d_text, M)
	s_p_text = tokens.probablity(s_d_text, M)



	# Display results
	elapsed_time = time.time() - start_time
	print("")
	print("Results:")
	print("Time Elapsed: %f" % (elapsed_time))
	print("Ham: Amount of Words Before Discrimination: %d" % (len(h_text)))
	print("Ham: Amount of Words After Discrimination:  %d" % (h_N))
	print("Spam: Amount of Words Before Discrimination: %d" % (len(s_text)))
	print("Spam: Amount of Words After Discrimination:  %d" % (s_N))
	print("")


if __name__ == '__main__':
     main()