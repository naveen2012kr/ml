import numpy as np
import math
import matplotlib.pyplot as plt
import csv
def get_binomial_log_likelihood(obs,probs):
    """ Return the (log)likelihood of obs, given the probs"""
    N = sum(obs);#number of trials  
    k = obs[0] # number of heads
    binomial_coeff = math.factorial(N) / (math.factorial(N-k) * math.factorial(k))
    prod_probs = obs[0]*math.log(probs[0]) + obs[1]*math.log(1-probs[0])
    log_lik = binomial_coeff + prod_probs
    return log_lik
data=[]
with open("cluster.csv") as tsv:
    for line in csv.reader(tsv):    
        data=[int(i) for i in line]
    
# represent the experiments
head_counts = np.array(data)
tail_counts = 10-head_counts
experiments = list(zip(head_counts,tail_counts))
# initialise the pA(heads) and pB(heads)
pA_heads = np.zeros(100); pA_heads[0] = 0.60
pB_heads = np.zeros(100); pB_heads[0] = 0.50
# E-M begins!
delta = 0.001  
j = 0 # iteration counter
improvement = float('inf')
while (improvement>delta):
    expectation_A = np.zeros((len(experiments),2), dtype=float) 
    expectation_B = np.zeros((len(experiments),2), dtype=float)
    for i in range(0,len(experiments)):
        e = experiments[i] 
        ll_A = get_binomial_log_likelihood(e,np.array([pA_heads[j],1-pA_heads[j]])) 
        ll_B = get_binomial_log_likelihood(e,np.array([pB_heads[j],1-pB_heads[j]])) 
        weightA = math.exp(ll_A) / ( math.exp(ll_A) + math.exp(ll_B) ) 
        weightB = math.exp(ll_B) / ( math.exp(ll_A) + math.exp(ll_B) ) 
        expectation_A[i] = np.dot(weightA, e) 
        expectation_B[i] = np.dot(weightB, e) 
    pA_heads[j+1] = sum(expectation_A)[0] / sum(sum(expectation_A)); 
    pB_heads[j+1] = sum(expectation_B)[0] / sum(sum(expectation_B)); 
    improvement = ( max( abs(np.array([pA_heads[j+1],pB_heads[j+1]]) - 
                    np.array([pA_heads[j],pB_heads[j]]) )) )
    print(np.array([pA_heads[j+1],pB_heads[j+1]]) - 
                    np.array([pA_heads[j],pB_heads[j]]) )
    j = j+1
plt.figure();
plt.plot(range(0,j),pA_heads[0:j])#for plotting the graph coin A
plt.plot(range(0,j),pB_heads[0:j])#for plotting the graph coin B
plt.show()