from sys import argv
from math import log

S = 0

def read_cover(filename):
    cover = {}
    global S
    nodes = set()
    with open(filename) as f:
        for line in f:
            node, c = line.split()
            nodes.add(node)
            if c not in cover:
                cover[c] = set([node])
            else:
                cover[c].add(node)
    S = len(nodes)
    return cover, nodes

def mutual_info(c_A, c_B):
    N_mA = len(c_A)
    N_mB = len(c_B)
    I_num = 0
    for i in c_A:
        for j in c_B:
            n_i = len(c_A[i])
            n_j = len(c_B[j])
            n_ij = len(c_A[i] & c_B[j])
            if n_ij == 0:
                continue
            log_term = log((n_ij * S) / (n_i * n_j))

            I_num += n_ij * log_term
    I_num *= -2

    I_den = 0
    for i in c_A:
        n_i = len(c_A[i])
        I_den += n_i * log(n_i / S)

    for j in c_B:
        n_j = len(c_B[j])
        I_den += n_j * log(n_j / S)

    I = I_num / I_den
    return I

def main():
    if len(argv) < 3:
        print('Enter the filename of the two covers as command line args')
        return

    c_A, nodes_A = read_cover(argv[1])
    c_B, nodes_B = read_cover(argv[2])
    
    if nodes_A == nodes_B:
        print('Improper covers! Please check the inputs.')
        return
    I = mutual_info(c_A, c_B)
    print('The mutual information of the two covers is {}'.format(I))

if __name__ == '__main__':
    main()
