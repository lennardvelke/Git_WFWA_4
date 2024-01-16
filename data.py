import numpy as np

# kleine Matrix mit Beispielverteilungen
data_1_P = np.array([
	[0.3, 0.2, 0.3, 0.5, 0.8],
	[0.3, 0.6, 0.4, 0.3, 0.1],
	[0.4, 0.2, 0.3, 0.2, 0.1]
])
data_1_Q = np.array([
	[0.4, 0.3, 0.2, 0.5, 0.8],
	[0.3, 0.3, 0.6, 0.3, 0.2],
	[0.3, 0.4, 0.2, 0.2, 0.0]
])

# Erzeugen von zufaelligen Matrizen mit Verteilungen
def random_distribution_matrix(seed:int=1234, shape=(1000, 100)):
	np.random.seed(seed=seed)
	M = np.random.random(size=shape)
	M /= np.expand_dims(M.sum(axis=0), axis=0) # Summe jeder Spalte muss 1 ergeben!
	return M