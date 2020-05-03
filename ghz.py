import numpy as np
from pyquil.api import WavefunctionSimulator
from pyquil import get_qc, Program
from pyquil.gates import *
import matplotlib.pyplot as plt

numQubit = 10
count = []
numShot = 1000

for i in range(2**numQubit):
    count.append(0)

p = Program(H(0))
for i in range(numQubit-1):
    p += CNOT(i,i+1)

ro = p.declare('ro', 'BIT', numQubit)

for i in range(numQubit):
    p += MEASURE(i, ro[i])

p.wrap_in_numshots_loop(numShot)

##get qc then compile and run program
qc = get_qc(str(numQubit) + 'q-noisy-qvm') #Aspen-4-3Q-D, Aspen-7-3Q-C
executable = qc.compile(p)
result = qc.run(executable)

index = 0
for i in range(numShot):
    for j in range(numQubit):
        index += 2**(numQubit-j-1)*result[i][j]

    count[index] += 1
    index = 0

names = []
for i in range(2**numQubit):
    tempName = str(bin(i))[2:]
    while len(tempName) < numQubit:
        tempName = '0' + tempName
    names.append(tempName)

values = count

plt.figure(figsize=(20, 5))
plt.bar(names, values)
if numQubit > 5:
    plt.gca().axes.get_xaxis().set_visible(False)
plt.show()
