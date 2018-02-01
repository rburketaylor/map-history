from glob import glob
from os import rename

year = 1900

for fname in glob('*.png'):
	rename(fname, str(year) + ".png")
	year += 1