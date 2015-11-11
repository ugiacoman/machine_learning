from __future__ import division
import enchant
import os
import time
import math

def classify(path, h_p_text, s_p_text):
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
	            		P = h_p_text[word]
	            		ham_probablity += math.log(P)
	            	if word in s_p_text:
	            		P = s_p_text[word]
	            		spam_probablity += math.log(P)
	            	if ham_probablity > spam_probablity:
	            		classify_dict[dir_entry_path] = "ham"
	            	else:
	            		classify_dict[dir_entry_path] = "spam"
	return classify_dict





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
	
def getCount(full_text, remove_factor):
	""" Returns Dictionary as word_count = {"word" : count, ...} Deletes all keys with only 1 value """

	word_count = {}
	# i.e. remove_factor = 4 (we will remove all words with a count less than or equal to 4)

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

