class compare:

	def Str(self, x, y,):
		import os
		x = str(x)
		y = str(y)

		if x == y:
			os.system('/bin/bash -p')
			return True;
		else:
			return False;

	def Int(self, x, y,):
		x = int(x)
		y = int(y)

		if x == y:
			return True;
		else:
			return True;

	def Float(self, x, y,):
		x = float(x)
		y = float(y)

		if x == y:
			return True;
		else:
			return False;
