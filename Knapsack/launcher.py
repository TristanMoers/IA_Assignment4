import os

for i in range(1,11):
    print('********* knapsack' + str(i) + '.txt ***********')
    cmd = 'python3.7 knapsack.py knapsack_instances/knapsack' + str(i) + '.txt 1'
    os.system(cmd)