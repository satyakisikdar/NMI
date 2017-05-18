# NMI
Find normalized mutual information of two covers of a network *G(V, E)* where each cover has **|V|** lines, each having the node label and the corresponding community label and finds the normalized mutual information. 

The code uses the exact definition from the paper 'Module identification in bipartite and directed networks' (https://arxiv.org/pdf/physics/0701151v2.pdf) including the naming conventions. 

Note: The node and the community labels need not be integers, but both the covers must cover all the nodes. 

Sample I/O
```
python mutual_info.py cover1 cover2

The mutual information of the two covers is 0.4920936619047235
```

where ```cover1``` is 
```
a 0
b 0
3 1
d 1
6 2
```
and ```cover2``` is 
```
a 0
b 0
3 0
c 0
d 1
6 1
````
