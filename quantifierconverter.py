#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD

class QuantifierConverter(object):

	def quantifierConverter(self,s):
		#Start writing your code from here
            A = '\u2200'
            E = '\u2203'
            str2 = s.replace("for every", A)
            return str2.replace("there exists", E)