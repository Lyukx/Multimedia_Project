# -*- coding: utf-8 -*-  

import copy

def LZW_encode(strIn):
	strOut = []
	dictionary = {}
	s = strIn[0]
	index = 1
	dict_len = 0

	for i in range(0, len(strIn)):
		c = strIn[i]
		if c not in dictionary:
			dictionary[c] = dict_len + 1
			dict_len += 1

	dictionary_origin = copy.deepcopy(dictionary)

	while index <= len(strIn):
		if(index == len(strIn)):
			c = ''
		else:
			c = strIn[index]
		
		if (s + c) in dictionary:
			s = s + c
			if(index == len(strIn)):
				strOut.append(str(dictionary[s + c]))
		else:
			strOut.append(str(dictionary[s]))
			dictionary[s + c] = dict_len + 1
			dict_len += 1
			s = c

		index = index + 1

	return strOut, dictionary_origin

def LZW_decode(strIn, dictIn):
	s = ''
	strOut = ''
	index = 0
	dictionary = {}
	dict_len = 0

	for i in dictIn.keys():
		dictionary[dictIn[i]] = i
		dict_len += 1

	while index < len(strIn):
		k = int(strIn[index])
		entry = dictionary[k]
		strOut += entry
		if(s != ''):
			dictionary[dict_len + 1] = s + entry[0]
			dict_len += 1
		s = entry
		index = index + 1

	return strOut

# encode,dictionary = LZW_encode('test message')
# print encode
# print dictionary
# decode = LZW_decode(encode, dictionary)
# print decode