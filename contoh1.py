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
	wt = fwt(p, bt, q)
	# tat = ftat(p, bt, wt)
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
	tat = [0] * p
	for i in range(p):
		tat[i] = bt[i] + wt[i]
	return tat


def create_csv_array(table):
	csv_ex = [[] for i in range(len(table))]
	csv_header = []
	for i in range(len(table)):
		for key in table:
			csv_ex[i].append(table[key][i])
	
	for k in table:
		csv_header.append(k)

	return csv_header, csv_ex


def export_data(header, csv_ex):
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
