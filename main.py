import base64
import random

class OneTimePad():


	BITMAP_CHARSET = [
		'a', 'b', 'c', 'd', 'e', 'f',
		'g', 'h', 'i', 'j', 'k', 'l',
		'm', 'n', 'o', 'p', 'q', 'r',
		's', 't', 'u', 'v', 'w', 'x',
		'y', 'z', 'A', 'B', 'C', 'D',
		'E', 'F', 'G', 'H', 'I', 'J',
		'K', 'L', 'M', 'N', 'O', 'P',
		'Q', 'R', 'S', 'T', 'U', 'V',
		'W', 'X', 'Y', 'Z', '0', '1',
		'2', '3', '4', '5', '6', '7',
		'8', '9'
	]


	def __init__(self, key=None, strength=64):

		self.key = key
		self.strength = strength - (strength % 32)


	def set_key(self, key):

		self.key = key


	def new_key(self, strength=None):

		self.strength = strength if strength != None else self.strength
		self.key = OneTimePad.gen_key(strength=self.strength)

	def cipher(self, string):

		_string = list(string)
		_key = list(self.key)
		_ciphered = ''

		i = 0
		for k in _key:

			_key[i] = OneTimePad.BITMAP_CHARSET.index(k)
			i += 1

		i = 0
		for s in _string:

			_string[i] = OneTimePad.BITMAP_CHARSET.index(s)
			i += 1

		j = 0
		for i in range(len(_string)):

			_v = (_string[i] + _key[j]) % len(OneTimePad.BITMAP_CHARSET)
			_ciphered += OneTimePad.BITMAP_CHARSET[_v]
			j += 1
			if j > len(_key) - 1:
				j = 0

		return _ciphered

	def uncipher(self, string):

		_string = list(string)
		_key = list(self.key)
		_unciphered = ''

		i = 0
		for k in _key:

			_key[i] = OneTimePad.BITMAP_CHARSET.index(k)
			i += 1

		i = 0
		for s in _string:

			_string[i] = OneTimePad.BITMAP_CHARSET.index(s)
			i += 1

		j = 0
		for i in range(len(_string)):

			_v = (_string[i] - _key[j]) % len(OneTimePad.BITMAP_CHARSET)
			_unciphered += OneTimePad.BITMAP_CHARSET[_v]
			j += 1
			if j > len(_key):
				j = 0
		return _unciphered

	def store_key(self, file_output='key.otp'):

		_key = self.key

		with open(file_output, 'w+') as f:

			f.write('------ PRIVATE KEY BEGINS ------')

			for i in range(0, len(_key), 32):

				f.write(f'\n{_key[i:i+32]}',)

			f.write('\n------ PRIVATE KEY ENDING ------')

	def load_key(self, file_input='key.otp'):

		with open(file_input, 'r') as f:

			data = f.read().split('\n')

		_key = ''.join(data[1:][:-1])

		self.key = _key

	@staticmethod
	def gen_key(charset=None, strength=64):

		_charset = charset if charset != None else OneTimePad.BITMAP_CHARSET
		_key = ''

		for i in range(strength):

			_key += random.choice(_charset)

		return _key

a = OneTimePad(key='ab')

print(a.cipher('abcdef'))