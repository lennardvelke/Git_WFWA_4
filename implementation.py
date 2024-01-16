import numpy as np
import matplotlib.pyplot as plt

def hellinger_distance(P, Q):
	"""
		Berechnet Hellinger-Distanz zwischen zwei Matrizen.

		Args:
			- P (np.ndarray): NumPy-Array der Matrix P
			- Q (np.ndarray): NumPy-Array der Matrix Q

		Returns:
			H (np.array) mit der Hellinger-Distanz zwischen P und Q
	"""

	return 1/(2 ** 0.5) * (np.sum((P ** 0.5 - Q ** 0.5) ** 2, axis=0) ** 0.5)

def select_best_cols(P, Q, H):
	"""
		Bestimmt die beiden Spalten, die zwischen P und Q die minimale 
		Distanz zwischen P und Q repraesentieren (wobei die Distanz mittels
		H uebergeben wird).

		Args:
			- P (np.ndarray): NumPy-Array der Matrix P
			- Q (np.ndarray): NumPy-Array der Matrix Q
			- H (np.array): Hellinger-Distanz-Vektors (wie z.B. von
				`hellinger_distance(P, Q)` ausgegeben)

		Returns:
			Matrix mit zwei Spalten:

				[[    Spalte,     Spalte],
				 [       mit,        mit],
				 [Verteilung, Verteilung],
				 [       aus,        aus],
				 [         P,          Q]]
	"""
	
	min = np.where(H == np.min(H))[0][0]
	
	return np.array([P[:,min],Q[:,min]]).T
	
def plot_distance(H):
	"""
		Erstellt einen Bar-Plot des Hellinger-Distanz-Vektors.
		Grafik soll dem Beispiel auf dem Aufgabenblatt moeglichst nah
		sein! 

		Args:
			- H (np.array): Hellinger-Distanz-Vektors (wie z.B. von
				`hellinger_distance(P, Q)` ausgegeben)

		Returns:
			Das Plt-Modul von Matplotlib.

			Die Grafik soll dann z.B. durch Aufruf der Funktion `show()` auf den hier 
			zurueckgegebenen Wert angezeigt werden können.
	"""
	#plt.plot(H)
	plt.bar(np.arange(len(H)),H, label="HD")
	
	plt.legend(loc='upper right')
	plt.title('Hellinger-Distanzen')
	plt.xlabel('Verteilung (Matrixspalte)')
	plt.ylabel('Distanz')
	return plt