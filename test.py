#-*-coding:utf-8-*-
from LZW_Encode_Decode import LZW_encode
from LZW_Encode_Decode import LZW_decode
from huffman import huffman_encode
from huffman import huffman_decode
print 'Start program'
try:
	print 'Start open files'
	source = open('source.txt')
	print 'Open source...OK'
	target_lzw = open('lzw_result.txt', 'w')
	target_lzw_dict = open('lzw_dict.txt', 'w')
	target_huffman = open('huffman_result.txt', 'w')
	target_huffman_dict = open('huffman_dict.txt', 'w')
	all_text = source.read()
	print 'open files...OK'
except IOError as e:
	print 'error'

lzw_encode_text, lzw_encode_dict = LZW_encode(all_text)
print 'lzw encode...OK'
target_lzw.write(''.join(lzw_encode_text))
target_lzw_dict.write(''.join(lzw_encode_dict))
print 'lzw file write...OK'

coding = {}
result = huffman_encode(all_text, coding)
print 'huffman encode...OK'
target_huffman.write(''.join(result))
target_huffman_dict.write(''.join(coding))
print 'huffman file write...OK'

target_huffman.close()
target_lzw.close()
target_huffman_dict.close()
target_lzw_dict.close()