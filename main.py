import pandas as pd
import numpy as np

class respair(object):
	def __init__(self, file_loc, user_query):
	        raw_data = pd.read_csv(file_loc,
        	        sep = "\s+", header = None, names = ['Res', 'Partner',
			'VDW', 'Elect', 'Pairwise', 'Charge'])
		raw_data.set_index('Res', inplace = True)
		self.data = raw_data[ raw_data.index == user_query ] 
		#print(self.data)
	
	def calculate_total_energies(self):
		interaction_vals = self.data.ix[:, [1,2,3]].astype(float)
		self.data['Interaction'] = interaction_vals.sum(axis = 1)
		print(self.data)
		self.total_interaction = np.sum(self.data['Interaction'].values)
		print(self.total_interaction)


	

if __name__ == '__main__':
	respair_location = '/home/naman/respair_interactions/respair.lst'
	amino = 'ARG+A0002_'
	R = respair(respair_location, amino)
	R.calculate_total_energies()	

