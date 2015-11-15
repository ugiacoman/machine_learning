from __future__ import division
import os
import time
import math

def s_analysis(data):
	""" Calculates False Positive Rate """
	# False positive if ham is actually spam
	# True negative if ham is ham
	false_positive = 0
	true_negative = 0
	true_positive = 0
	false_negative = 0

	for email in data:
		if ("ham" in email) & (data[email] == "spam"):
			false_positive += 1
		if ("ham" in email) & (data[email] == "ham"):
			true_negative += 1
		if ("spam" in email) & (data[email] == "spam"):
			true_positive += 1
		if ("spam" in email) & (data[email] == "ham"):
			false_negative += 1

	true_positive_rate = (true_positive / (true_positive + false_negative))
	false_positive_rate = (false_positive / (false_positive + true_negative))
	false_negative_rate = (1 - true_positive_rate)
	true_negative_rate = (1 - false_positive_rate)

	analysis = [false_positive_rate, true_positive_rate, false_negative_rate, true_negative_rate]
	return(analysis)


def classify(path, h_p_text, s_p_text, unweighted_p):
	""" Returns dict with all emails in path and classifies them as either spam or ham"""
	data = []
	classify_dict = {}
	for dir_entry in os.listdir(path):
	    dir_entry_path = os.path.join(path, dir_entry)
	    if os.path.isfile(dir_entry_path):
	        with open(dir_entry_path, 'r') as my_file:
	            my_file_string = my_file.read()
	            word_list = my_file_string.split()
	            word_list = map(lambda x:x.lower(), word_list)
	            ham_probablity = 0
	            spam_probablity = 0
	            for word in word_list:
	            	if word in h_p_text:
	            		P = h_p_text[word] * unweighted_p # s_p_text[word] * Probablity without taking a look at data
	            		ham_probablity += math.log(P) 
	            	if word in s_p_text:
	            		P = s_p_text[word] * unweighted_p # s_p_text[word] * Probablity without taking a look at data
	            		spam_probablity += math.log(P)

	            	if ham_probablity > spam_probablity:
	            		classify_dict[dir_entry_path] = "ham"
	            	else:
	            		classify_dict[dir_entry_path] = "spam"	            		
	return classify_dict

def compile_data(classified_data, classifier):
	""" Calculates Misclassfication Rate  """
	spam_count = 0
	ham_count = 0
	total = 0
	for email in classified_data:
		if classified_data[email] == "spam":
			spam_count += 1
		else:
			ham_count += 1
	
	total = ham_count + spam_count

	if classifier == "ham":	
		misclassification_rate = (1 - (ham_count / total))
	else:
		misclassification_rate = (1 - (spam_count / total))

	gini_index = (ham_count / total * (1 - ham_count / total)) + (spam_count / total * (1 - spam_count / total))
	entropy = -((ham_count / total) * math.log(ham_count/total, 2) + (spam_count / total) * math.log(spam_count / total, 2))

	return (misclassification_rate, gini_index, entropy)

def parse_instances(path):
	""" Parses email and returns all strings to lower. """

	data = []
	for dir_entry in os.listdir(path):
	    dir_entry_path = os.path.join(path, dir_entry)
	    if os.path.isfile(dir_entry_path):
	        with open(dir_entry_path, 'r') as my_file:
	            data.append(my_file.read())
	emails = "".join(data)

	email = emails.split()
	email = map(lambda x:x.lower(),email)
	return email
	
def count_instances(path):
	count = 0
	for dir_entry in os.listdir(path):
	    dir_entry_path = os.path.join(path, dir_entry)
	    if os.path.isfile(dir_entry_path):
	        with open(dir_entry_path, 'r') as my_file:
	            count += 1
	return count

def getCount(full_text, remove_factor):
	""" Returns Dictionary as word_count = {"word" : count, ...} Deletes all keys with only 1 value """

	word_count = {}
	

	for word in full_text:
		if word not in word_count:
			word_count[word] = 1
		else:
			word_count[word] = word_count[word] + 1
	found = []
	for key in word_count:
		if word_count[key] <= remove_factor or (len(key) == 1):
			found.append(key)

	for string in found:
		if string in word_count:
			del word_count[string]

	return word_count


def probablity(d_text, M):
	""" Replaces value(count) of each key with the its probablity"""
	N = len(d_text)
	for key in d_text:
		N_k = d_text[key]
		P = ((N_k + 1)/(N+M))
		d_text[key] = P

	return d_text



def discriminate(full_text, ignore_symbols, ignore_common_words):
	""" Returns a discriminated dict of strings with their counts. Choose factors to discriminate below """

	# This list contains all words that we will ignore.
	common_words_list = ["subject:", "email", "the", "a"]
	
	# List of symbols and numbers that we will ignore
	symbol_list = ["1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^",
					"&","*","(",")","-","_", ".", ",", "<", ">", "?", "/", ":", "[", "]", "{", "}", "|", "\\", "'", "+", "`", "~", "="]

	full_discriminate_list = []

	if ignore_symbols == True:
		full_discriminate_list += symbol_list
	if ignore_common_words == True:
		full_discriminate_list += common_words_list

	# Starts Discrimination
	found = []

	for discriminate in full_discriminate_list:
		for string in full_text:
			if discriminate in string:
				found.append(string)

	for element in found:
		if element in full_text:
			del full_text[element]

	# Removes strings that are not in English Dictionary
	# d = enchant.Dict("en_US")
	# for string in full_text:
	# 	if not (d.check(string)):
	# 		full_text.remove(string)
	
	parsed_text = full_text 				
	return parsed_text

