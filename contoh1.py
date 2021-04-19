# waiting time = wt
# number of process = p
# turaround time = tat
# burst time = bt
# time quantum = q
# remaining process time = t
# find waiting time = fwt
# remaining burst time = rbt
# find turnaround time = ftat
# find average time = fat
# total waiting time = twt
from tabulate import tabulate
import csv

def rr(p, bt, q):
	"""
	a function that print round robin stats,
	that is process number, burst time, 
	waiting time, average waiting time

	Parameter
	---------
	p: int
		number that represent how many process are running
	bt: list
		list of number that contain burst time of process 1 to p
	q: int
		time quantum, a number that tell how long a process can run
		before switching to another process

	Returns
	-------
	table: dict
		a dictionary containing list of process number, list of
		burst time, list of waiting time
	"""
	
	wt = fwt(p, bt, q)
	twt = 0

	for i in range(p):
		twt = twt + wt[i]
	
	table = {
		"process": [x for x in range(1, p + 1)],
		"burst time": bt,
		"waiting time": wt
	}
	
	print(tabulate(table, headers="keys", tablefmt="fancy_grid"))
	print(f"average waiting time = {twt / p}")

	return table


def fwt(p, bt, q):
	"""
	a function that calculate waiting time, it take p,
	bt, and q. Then create a copy of bt. Then endlessly
	loop to calcutate wt until all bt copy is 0

	Parameter
	---------
	p: int
		number that represent how many process are running
	bt: list
		list of number that contain burst time of process 1 to p
	q: int
		time quantum, a number that tell how long a process can run
		before switching to another process
	
	Returns
	-------
	wt: list
		waiting time of each process, hence wt
	"""

	wt = [0] * p
	rbt = [0] * p
	t = 0
	for i in range(p):
		rbt[i] = bt[i]

	while(1):
		done = True
		for i in range(p):
			if rbt[i] > 0:
				done = False
				if rbt[i] > q:
					t = t + q
					rbt[i] = rbt[i] - q
				else:
					t = t + rbt[i]
					wt[i] = t - bt[i]
					rbt[i] = 0

		if done == True:
			break
	
	return wt


def ftat(p, bt, wt):
	"""
	function that calculate turnaound time,
	that is (burst time) + (waiting time)

	Parameter
	---------
	p: int
		number that represent how many process are running
	bt: list
		list of number that contain burst time of process 1 to p
	wt: list
		waiting time of each process, hence wt

	Returns
	-------
	tat: list
		turnaround time for each process, hence tat 
	"""

	tat = [0] * p
	for i in range(p):
		tat[i] = bt[i] + wt[i]
	return tat


def create_csv_array(table):
	"""
	function that take a dictionary and
	turn it into 2 dimentional array that
	can be turned into csv file
	
	Parameter
	---------
	table: dict
		the dictionary format must be:
		{
			"table header 1": [data1, data2, data3, ...],
			"table header 2": [data1, data2, data3, ...],
			...
		}

	Returns
	-------
	csv_header: list
		list of string that will be the csv
		header file
	csv_ex: list
		2 dimentional list(list that contain list) that
		contain csv data
	"""

	csv_ex = [[] for i in range(len(table))]
	csv_header = []
	for i in range(len(table)):
		for key in table:
			csv_ex[i].append(table[key][i])
	
	for k in table:
		csv_header.append(k)

	return csv_header, csv_ex


def export_data(header, csv_ex):
	"""
	a function that turn list of header
	and list of list into csv file named
	round_robin.csv in the same directory
	that this script reside

	Parameter
	---------
	header: list
		list of string that will be the csv
		header file
	csv_ex: list
		list of list that contain csv data 
	"""
	with open("round_robin.csv", "w") as f:
		f = csv.writer(f, delimiter=",")
		f.writerow(header)
		f.writerows(csv_ex)


if __name__ == "__main__":
	default = input("default input[y|n]: ")
	if default.lower() == "y":
		p = 4
		q = 3
		bt = [11, 9, 10, 8]
	else:
		p = int(input("input process: "))
		q = int(input("input time quantum: "))
		bt = [0] * p
		for i in range(p):
			bt[i] = int(input(f"input the {i + 1}-th burst time: "))
	tab = rr(p, bt, q)
	want_export = input("do you want to export[y|n]: ")
	if(want_export == "y"):
		header, csv_ex = create_csv_array(tab)
		export_data(header, csv_ex)
	else:
		pass
