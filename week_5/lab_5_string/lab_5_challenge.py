"""
Fletcher Ace Johnson
"""

def main():
	encoded_word = 'L3KAOUL'
	decode_word(encoded_word)
	encoded_word = "W3LARF3TTS"
	decode_word(encoded_word)
	encoded_word = "VQN3NQ"
	decode_word(encoded_word)
	encoded_word = "3TRAQDY T3LA"
	decode_word(encoded_word)
	encoded_word = "3TT LHA TILLTA LIMAS"
	decode_word(encoded_word)
	encoded_word = "LHA GRAAN FIATD GTA3MS IN LHA W3RM SUNVA3MS"
	decode_word(encoded_word)
	encoded_word = "TONG T3VS T3CKS L3SLY L3CO LIMA 3L TA3SL T3LATY"
	decode_word(encoded_word)
	
#encoded_word = "UUHO"  		#Used for Bonus
#encoded_word = "EOUUUUOUU" 	#Used for Bonus
  
def decode_word(word):
	worded = ''
	for letter in word:
		if letter == 'T':
			worded += 'L'
		elif letter == 'L':
			worded += 'T'
		elif letter == '3':
			worded += 'A'
		elif letter == 'A':
			worded += 'E'
		elif letter == 'Q':
			worded += 'A'
		elif letter == 'V':
			worded += 'B'
		else:
			worded += letter
	print(worded)

main()