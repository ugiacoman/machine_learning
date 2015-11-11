import enchant
import os
import time
import tokens

def main():
	start_time = time.time()
	settings = open("settings.txt", "r")
	settings_dict = {}
	ham_path = ""
 	spam_path = ""

	for line in settings:
		line = line.split()
		if line[0] == "ham_path:":
			ham_path = line[1]
		else:
			spam_path = line[1]

	"""Ham Parse"""
	# Splits string into list of strings and lowercases them
	h_full_text = tokens.parse(ham_path)

	# Gets count of each string
	h_count_dict = tokens.getCount(h_full_text)

	# Eliminates strings we don't want to count
	h_d_text = tokens.discriminate(h_count_dict)
	# print(d_text)

	"""Spam Parse"""
	# Splits string into list of strings and lowercases them
	s_full_text = tokens.parse(spam_path)

	# Gets count of each string
	s_count_dict = tokens.getCount(s_full_text)

	# Eliminates strings we don't want to count
	s_d_text = tokens.discriminate(s_count_dict)
	# print(d_text)

	# Display results
	elapsed_time = time.time() - start_time
	print("")
	print("Results:")
	print("Time Elapsed: %f" % (elapsed_time))
	print("Ham: Amount of Words Before Discrimination: %d" % (len(h_full_text)))
	print("Ham: Amount of Words After Discrimination:  %d" % (len(h_d_text)))
	print("Spam: Amount of Words Before Discrimination: %d" % (len(s_full_text)))
	print("Spam: Amount of Words After Discrimination:  %d" % (len(s_d_text)))
	print("")


if __name__ == '__main__':
     main()