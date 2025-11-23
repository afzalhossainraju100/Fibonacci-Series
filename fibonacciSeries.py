"""Simple Fibonacci series generator.

Usage:
 - Run interactively: `python fibonacciSeries.py`
 - With argument: `python fibonacciSeries.py 10`

Examples:
 > python fibonacciSeries.py 7
 0 1 1 2 3 5 8
"""

import sys


def fibonacci(n):
	"""Return a list of the first n Fibonacci numbers (starting from 0).

	This uses a simple iterative approach (O(n) time, O(n) memory).
	"""
	if n <= 0:
		return []
	seq = [0]
	if n == 1:
		return seq
	seq.append(1)
	while len(seq) < n:
		seq.append(seq[-1] + seq[-2])
	return seq


def main():
	# Accept optional command-line argument for convenience.
	if len(sys.argv) > 1:
		arg = sys.argv[1].strip()
		if arg.lstrip('-').isdigit():
			n = int(arg)
		else:
			print("Please provide an integer for the number of terms.")
			return
	else:
		s = input("Enter number of Fibonacci terms to generate: ").strip()
		if s.lstrip('-').isdigit():
			n = int(s)
		else:
			print("Invalid input. Please enter a non-negative integer.")
			return

	if n < 0:
		print("Please enter a non-negative integer.")
		return

	seq = fibonacci(n)
	if seq:
		print(" ".join(str(x) for x in seq))
	else:
		print("No terms to show (n=0).")


if __name__ == "__main__":
	main()

