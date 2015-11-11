import enchant
import os
import time

def parse(path):
	""" Parses email and returns all strings to lower. 

	TODO: Have it read all emails
	"""

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
	
def getCount(d_text):
	""" Returns Dictionary as word_count = {"word" : count, ...} Deletes all keys with only 1 value """

	word_count = {}

	for word in d_text:
		if word not in word_count:
			word_count[word] = 1
		else:
			word_count[word] = word_count[word] + 1
	found = []
	for key in word_count:
		if word_count[key] == 1 or (len(key) == 1):
			found.append(key)

	for string in found:
		if string in word_count:
			del word_count[string]

	return word_count


def discriminate(full_text):
	""" Returns a discriminated dict of strings with their counts. Choose factors to discriminate below """
	# Select Discriminating Factors
	ignore_symbols = True
	ignore_common_words = True

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

