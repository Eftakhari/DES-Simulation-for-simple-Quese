# CoViD-19 Hospital V 1.2
import simpy
import numpy as np
from random import uniform, normalvariate, expovariate, seed, randint
from math import floor
import matplotlib.pyplot as mp
def QueueL(t=np.inf):         # Queue length at time (t)
    arr = set([int(Ă[k][1][9:]) for k in range(len(Ă)) if Ă[k][0] <= t])
    par = set([int(Ĵ[k][1][9:]) for k in range(len(Ĵ)) if Ĵ[k][0] <= t])
    return len(arr.difference(par))
def Patient(env, name, hp):
    arrive = env.now
    Ă.append((arrive, name))
    with hp.Bed.request() as request:
        patience = uniform(min_Tol, Max_Tol)
        results = yield request | env.timeout(patience)
        waitS = env.now - arrive
        if request in results:
            W.append(waitS)
            yield env.process(hp.Cure(name))
        else:
            waitF = env.now - arrive
            Ĵ.append((env.now, name))
            Ň.append((env.now, 0))
            W.append(waitF)
class Hospital(object):
    def __init__(self, env, Beds, CureTime):
        self.env = env
        self.Bed = simpy.Resource(env, Beds)
        self.CureTime = CureTime
    def Cure(self, name):
        Bedridden = normalvariate(CT, CT/6)
        yield self.env.timeout(Bedridden)
        B.append(CT)
        Ň.append((env.now, 1))
        Ĵ.append((env.now, name))

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	for y in [7, 14, 21, 28]:
		for h in range (10):
			R_Seed = h
			seed(R_Seed)
			Total_Beds = 10
			λ = x
			CT = normalvariate(y, y/6)
			min_Tol = uniform(0, 1)
			Max_Tol = uniform(1, 2)
			First_Batch = randint(1, 10)
			SIM_TIME = 100
			Ă = []; Ň = []; Q = []; B = []; W = []; Ĵ = []
			def setup(env, beds, CureTime, landa):
				hp = Hospital(env, beds, CureTime)
				for i in range(First_Batch):
					env.process(Patient(env, 'Patient #%d' %(i+1), hp))
					pass
				while True:
 					yield env.timeout(expovariate(landa))
 					i += 1
 					env.process(Patient(env, 'Patient #%d' %(i+1), hp))
			env = simpy.Environment()
			env.process(setup(env, Total_Beds, CT, λ))
			env.run(until=SIM_TIME)
			Nf = []
			for k in range(len(Ň)):
				if Ň[k][1] == 0:
					Nf.append(1)
			N_ = 100*sum(Nf) / len(Ň)
			A_ = []
			for a in Ă:
				A_.append(floor(a[0]))
			a1, a2, a3 = mp.hist(A_, int(SIM_TIME))
			A_bar = np.average(a1)
			N = []
			for k in range(len(Ň)):
				N.append(Ň[k][1])
			N_bar = 100*N.count(1) / len(N)
			QL = [QueueL(d) for d in range(SIM_TIME)]
			Q_bar = np.average(QL)
			B_bar = 100*(sum(B) / (Total_Beds*SIM_TIME))
			W_bar = sum(W) / len(W)
			J = []
			Jl = range(len(Ĵ))
			for k in Jl:
				J.append(floor(Ĵ[k][0]))
			j1, j2, j3 = mp.hist(J, int(SIM_TIME))
			J_bar = np.average(j1)
			# J_Success = []
			# for k in Jl:
			#     J_Success.append(Ĵ[k][1])
			# print(sum(J_Success)/len(J_Success))
			print(x, y, A_bar, N_bar, Q_bar, B_bar, W_bar, J_bar, N_)