if __name__ == '__main__':
    input = "input.txt"
    with open(input, 'r') as infile:
        data = [[int(n) for n in line.strip()] for line in infile]
#for row in data:
#    print(row)
#print()
n_iterations = 1
while True:
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] += 1
    any_flashed = True
    while any_flashed:
        any_flashed = False
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] > 9:
                    any_flashed = True
                    data[i][j] = 0
                    for k in range(max(i-1, 0), min(i+2, len(data))):
                        for l in range(max(j-1, 0), min(j+2, len(data[i]))):
                            if data[k][l] > 0:
                                data[k][l] += 1
    if all(sum(row)== 0 for row in data):
        print(n_iterations)
        break
    else:
        n_iterations +=1
    #for row in data:
        #print(row)
    #print()
