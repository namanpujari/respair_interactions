import pandas as pd
import numpy as np
import sys
import os
from argparse import ArgumentParser

class respair(object):
	def __init__(self, user_query):
		if(os.path.exists('respair.lst')):
			pass
		else:
			sys.exit('respair.lst NOT FOUND')
	        raw_data = pd.read_csv('respair.lst',
        	        sep = "\s+", header = None, names = ['Res', 'Partner',
			'VDW', 'Elect', 'Pairwise', 'Charge'])
		raw_data.set_index('Res', inplace = True)
		if(user_query not in set(raw_data.index)):
			sys.exit('AMINO ACID NOT IN respair.list. PLEAST TRY AGAIN')
		else:
			self.data = raw_data[ raw_data.index == user_query ]


	def analysis(self, threshold):
		self.user_threshold = threshold
		interaction_vals = self.data.ix[:, [1,2,3]].astype(float).abs()
		self.data['Interaction'] = interaction_vals.sum(axis = 1)
		self.total_interaction = np.sum(self.data['Interaction'].values)
		
		# checking whether any of the total interactions (for individual partners)
		# is a above a certain percentage threshold
		self.error_list = []
		for res_index in range(len(self.data['Interaction'])):
			if(self.data['Interaction'][res_index] >= (self.user_threshold*self.total_interaction)):
				self.error_list.append(res_index)

	def display(self):
		print('------------------------------------------------------')
		if(len(self.error_list) == 0):
			print('THERE ARE NO AMINO ACID PARTNERS THAT CAUSE AN INTERA-')
			print('CTION ENERGY GREATER OR EQUAL TO THE PERCENTAGE THRES-')
			print('HOLD. (' + str(self.user_threshold) + ')')
			print('THE TOTAL INTERACTION ENERGY WAS ' +  str(self.total_interaction))
		else:
			print('THE FOLLOWING AMINO ACIDS CONTRIBUTED AN INTERACTION')
			print('ENERGY VIOLATING THE THRESHOLD (' + str(self.user_threshold) + ')\n')
			print(self.data.ix[self.error_list, :])
			print('\nTHE TOTAL INTERACTION ENERGY WAS ' + str(self.total_interaction))		
		print('------------------------------------------------------')
	
def ask_arguments():
	parser = ArgumentParser(description = '''Checks for interaction energies
			that are very high (threshold indicated by user)''')
	# required arguments below:
	required = parser.add_argument_group('''Required arguments''')
	required.add_argument('-a', '--amino_acid', required = True, 
		type = str, help = '''Name of amino acid to be analyzed''')
	required.add_argument('-t', '--threshold', required = True,
		type = float, help = '''Threshold determining whether an
		interaction energy is erroneous or not''')
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = ask_arguments()
	
	#amino = 'ARG+A0002_'
	R = respair(args.amino_acid)
	R.analysis(args.threshold)
	R.display()

