from __future__ import division
import enchant
import os
import time
import tokens

def main():
	start_time = time.time()
	settings = open("settings.txt", "r")
	ham_path = ""
 	spam_path = ""
 	ham_test_path = ""
 	spam_test_path = ""

 	""" Variables: Adjust model here. To view symbols and common words used go to tokens.py discriminate() """
 	remove_factor = 20
 	ignore_symbols = True
	ignore_common_words = True

	for line in settings:
		line = line.split()
		if line[0] == "training_ham_path:":
			ham_path = line[1]
		elif line[0] == "training_spam_path:":
			spam_path = line[1]
		elif line[0] == "testing_ham_path:":
			ham_test_path = line[1]
		else:
			spam_test_path = line[1]

	"""Parse Ham emails"""
	# Splits string into list of strings and lowercases them
	h_text = tokens.parse_instances(ham_path)

	# Gets count of each string
	h_c_text = tokens.getCount(h_text, remove_factor)

	# Eliminates strings we don't want to count
	h_d_text = tokens.discriminate(h_c_text, ignore_symbols, ignore_common_words)
	h_N = len(h_d_text) 

	"""Parse Spam emails"""
	# Splits string into list of strings and lowercases them
	s_text = tokens.parse_instances(spam_path)

	# Gets count of each string
	s_c_text = tokens.getCount(s_text, remove_factor)

	# Eliminates strings we don't want to count
	s_d_text = tokens.discriminate(s_c_text, ignore_symbols, ignore_common_words)
	s_N = len(s_d_text) 

	M = h_N + s_N

	h_p_text = tokens.probablity(h_d_text, M)
	s_p_text = tokens.probablity(s_d_text, M)

	# Classifies all emails in directory as spam or ham
	test_ham_classify = tokens.classify(ham_test_path, h_p_text, s_p_text)
	test_spam_classify = tokens.classify(spam_test_path, h_p_text, s_p_text)

	# Finds misclassification rate
	h_misclass_data = tokens.compile_data(test_ham_classify, "ham")
	s_misclass_data = tokens.compile_data(test_ham_classify, "spam")


	# Display results
	elapsed_time = time.time() - start_time
	print("")
	print("Variables:")
	print("remove_factor: %d" % (remove_factor))
	print("ignore_symbols: %r" % (ignore_symbols))
	print("ignore_common_words: %r" % (ignore_common_words))
	print("")
	print("Training Ham Path: %s" % (ham_path))
	print("Training Spam Path: %s" % (spam_path))
	print("")
	print("Results:")
	print("Time Elapsed: %f" % (elapsed_time))
	print("Ham: Amount of Words Before Discrimination: %d" % (len(h_text)))
	print("Ham: Amount of Words After Discrimination:  %d" % (h_N))
	print("Spam: Amount of Words Before Discrimination: %d" % (len(s_text)))
	print("Spam: Amount of Words After Discrimination:  %d" % (s_N))
	print("")
	print("** Ham Test Data ** (%s)" % (ham_test_path))
	print("Misclassification Rate: %f" % (h_misclass_data[0]))
	print("Gini Index: %f" % (h_misclass_data[1]))
	print("Entropy: %f" % (h_misclass_data[2]))
	print("")
	print("** Spam Test Data ** (%s)" % (spam_test_path))
	print("Misclassification Rate: %f" % (s_misclass_data[0]))
	print("Gini Index: %f" % (s_misclass_data[1]))
	print("Entropy: %f" % (s_misclass_data[2]))
	print("")


if __name__ == '__main__':
     main()