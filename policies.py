#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:30:30 2019

@author: 3701494
"""
import numpy as np
def valueIter():
    V0=np.rand(nbstates)*1
    for i in range(len(V0)):
        
        
def value_iteration(env, gamma = 0.99,eps = 1e-20):
    """ Value-iteration algorithm """
    statedic, mdp = env.getMDP()  # recupere le mdp : statedic
    nb_State=len(statedic)
    v = np.random.rand(nb_State)  # initialize value-function
    max_iterations = 100000
    
    for i in range(max_iterations):
        prev_v = np.copy(v)
        for s in mdp.keys():
            for action in mdp[s].keys():
                for (pb_Trans,state_Dest,reward,done) in enumerate(mdp[s][action])
                    q_sa = [sum([p*(r + gamma*prev_v[s])  
                    v[s] = max(q_sa)
        if (np.sum(np.fabs(prev_v - v)) <= eps):
            print ('Value-iteration converged at iteration# %d.' %(i+1))
            break
    return v



