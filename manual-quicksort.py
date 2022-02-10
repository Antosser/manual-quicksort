from os import system
from functools import cache
from random import shuffle
import pathlib
from time import sleep
import os

filepath = str(pathlib.Path(__file__).parent.resolve()) + '\\manual_quick_sort.txt'
print(filepath)

try:
	with open(filepath, 'x') as f: pass
except Exception:
	pass

system(filepath)

inp = []
with open(filepath) as f:
	inp = f.read().split('\n')

def cls():
	system('cls' if os.name == 'nt' else 'clear')

def quicksort(arr):
	shuffle(arr)
	if len(arr) <= 1:
		return arr

	pivot = arr[0]
	less = []
	greater = []

	for i in arr[1:]:
		while True:
			cls()
			print(f'1) {pivot}')
			print(f'2) {i}\n')
			pick = int(input('Pick: '))
			if pick == 1:
				less.append(i)
				break
			elif pick == 2:
				break
			else:
				continue

	less = quicksort(less)
	greater = quicksort(greater)

	return less + [pivot] + greater

cls()
sortedlist = quicksort(inp)
for i in range(len(sortedlist)):
	print(f'{i + 1}) {sortedlist[::-1][i]}')

sleep(9999)