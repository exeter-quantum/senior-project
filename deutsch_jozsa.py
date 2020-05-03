import numpy as np
from pyquil.api import WavefunctionSimulator
from pyquil import get_qc, Program
from pyquil.gates import *
import math
import random
import matplotlib.pyplot as plt


numX = 2 #only works for x = 2 as far as we've done
oracleDictionary = {0: 'con0',1: 'con1', 2: 'balXOR', 3: 'balNXOR', 4: 'balX1', 5: 'balNX1', 6: 'balX0', 7: 'balNX0'}

p = Program()
p += X(numX)

for i in range(numX+1):
    p += H(i)
 
 #oracle
functionID = random.randrange(8)

if functionID == 0 or functionID == 1:
    print("You don't know this yet, but f is constant")
    print("The secret oracle is " + oracleDictionary.get(functionID))
else:
    print("You don't know this yet, but f is balanced")
    print("The secret oracle is " + oracleDictionary.get(functionID))
    
if functionID == 1:
    p += X(2)
elif functionID == 2:
    p += CNOT(0,1)
    p += CNOT(1,2)
    p += CNOT(0,1)
elif functionID == 3:
    p += CNOT(0,1)
    p += CNOT(1,2)
    p += CNOT(0,1)
    p += X(2)
elif functionID == 4:
    p += CNOT(1,2)
elif functionID == 5:
    p += CNOT(1,2)
    p += X(2)
elif functionID == 6:
    p += CNOT(0,2)
elif functionID == 7:
    p += CNOT(0,2)
    p += X(2)

for i in range(numX):
    p += H(i)

ro = p.declare('ro', 'BIT', 2)

for i in range(numX):
    p += MEASURE(i, ro[i])
    
p.wrap_in_numshots_loop(1000)


wfn=WavefunctionSimulator().wavefunction(p)
print("Here's what the wavefunction, |y x1 x0>, should be after the algorithm:")
print(wfn)

qc = get_qc('3q-noisy-qvm') #we've also used Aspen-4-3Q-D', 'Aspen-7-3Q-C'
np = qc.compiler.quil_to_native_quil(p)
exe = qc.compiler.native_quil_to_executable(np)
output = qc.run(exe)

balCount = 0
conCount = 0
count00 = 0
count01 = 0
count10 = 0
count11 = 0

for state in output:
    if state[0] == 0 and state[1] == 0:
        conCount += 1
        count00 += 1
    elif state[0] == 1 and state[1] == 0:
        balCount += 1
        count01 += 1
    elif state[0] == 0 and state[1] == 1:
        balCount += 1
        count10 += 1
    else:
        balCount += 1
        count11 += 1
print("\n******************************************************************* \n")
print("Number of trials where f is found to be constant: " + str(conCount))
print("Number of trials where f is found to be balanced: " + str(balCount))

if conCount > balCount:
    print("We conclude the function is CONSTANT")
elif conCount < balCount:
    print("We conclude the function is BALANCED")
else:
    print("Inconclusive results")

names = ['|00> (Constant)','|01> (Balanced)', '|10> (Balanced)','|11> (Balanced)']
values = [count00,count01,count10,count11]

plt.figure(figsize=(10, 5))
plt.bar(names, values)
plt.title("Measurements of |x1 x0>")
plt.show()

print("\n******************************************************************* \n")

print("Pyquil:")
print(p)

print("Protoquil:")
print(np)
