import paths
import os
from pathlib import Path
os.environ["PATH"] += os.pathsep + str(Path.home() / "bin")

import subprocess
import sys

import pymc as pm
import arviz as az
import pytensor.tensor as at

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import scipy.integrate as integrate
from scipy import stats

from matplotlib import rc
rc('font', **{'family':'sans-serif'})
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{physics}')

plt.rcParams['xtick.top'] =  True
plt.rcParams['xtick.direction'] =  'in'
plt.rcParams['xtick.major.width'] =  1.0
plt.rcParams['xtick.minor.width'] =  1.0
plt.rcParams['ytick.right'] =  True
plt.rcParams['ytick.direction'] =  'in'
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['ytick.minor.width'] =  1.0
plt.rcParams['lines.markeredgewidth'] =  1.0

### PyMC models ###

if __name__ == '__main__':

    with pm.Model() as model_uni:

        cosψ = pm.Uniform('cosψ',lower=-1,upper=1)
        
        ψ = pm.Deterministic('ψ', at.arccos(cosψ))
        sinψ = pm.Deterministic('sinψ', at.sqrt(1-cosψ**2))
        
        θ = pm.Uniform('θ', lower=0, upper=np.pi)
        cosθ = pm.Deterministic('cosθ', at.cos(θ))
        sinθ = pm.Deterministic('sinθ', at.sin(θ))

        # iorb
        iorb = np.pi/2

        # find λ in terms of ψ, θ, and iorb
        λ = pm.Deterministic('λ', at.arctan2(sinψ*sinθ, cosψ*at.sin(iorb)-sinψ*cosθ*at.cos(iorb)))
        cosλ = pm.Deterministic('cosλ', at.cos(λ))

        # find i in terms of ψ, θ, and iorb
        cosi = pm.Deterministic('cosi', sinψ*cosθ*at.sin(iorb)+cosψ*at.cos(iorb))
        i = pm.Deterministic('i', at.arccos(cosi))
        
        iso_cosi = pm.Uniform('iso_cosi', lower=0, upper=1)
        iso_cosψ = pm.Deterministic('iso_cosψ', at.sqrt(1-iso_cosi**2)*cosλ)
        
        uni = pm.sample()


    with pm.Model() as model_norm1:

        cosψ = pm.TruncatedNormal('cosψ', mu=0., sigma=0.2, lower=-1, upper=1)
        
        ψ = pm.Deterministic('ψ', at.arccos(cosψ))
        sinψ = pm.Deterministic('sinψ', at.sqrt(1-cosψ**2))
        
        θ = pm.Uniform('θ', lower=0, upper=np.pi)
        cosθ = pm.Deterministic('cosθ', at.cos(θ))
        sinθ = pm.Deterministic('sinθ', at.sin(θ))

        # iorb
        iorb = np.pi/2

        # find λ in terms of ψ, θ, and iorb
        λ = pm.Deterministic('λ', at.arctan2(sinψ*sinθ, cosψ*at.sin(iorb)-sinψ*cosθ*at.cos(iorb)))
        cosλ = pm.Deterministic('cosλ', at.cos(λ))

        # find i in terms of ψ, θ, and iorb
        cosi = pm.Deterministic('cosi', sinψ*cosθ*at.sin(iorb)+cosψ*at.cos(iorb))
        i = pm.Deterministic('i', at.arccos(cosi))
        
        iso_cosi = pm.Uniform('iso_cosi', lower=0, upper=1)
        iso_cosψ = pm.Deterministic('iso_cosψ', at.sqrt(1-iso_cosi**2)*cosλ)
        
        norm1 = pm.sample()

    with pm.Model() as model_norm2:

        cosψ = pm.TruncatedNormal('cosψ', mu=-0.4, sigma=0.2, lower=-1, upper=1)
        
        ψ = pm.Deterministic('ψ', at.arccos(cosψ))
        sinψ = pm.Deterministic('sinψ', at.sqrt(1-cosψ**2))
        
        θ = pm.Uniform('θ', lower=0, upper=np.pi)
        cosθ = pm.Deterministic('cosθ', at.cos(θ))
        sinθ = pm.Deterministic('sinθ', at.sin(θ))

        # iorb
        iorb = np.pi/2

        # find λ in terms of ψ, θ, and iorb
        λ = pm.Deterministic('λ', at.arctan2(sinψ*sinθ, cosψ*at.sin(iorb)-sinψ*cosθ*at.cos(iorb)))
        cosλ = pm.Deterministic('cosλ', at.cos(λ))
      
        # find i in terms of ψ, θ, and iorb
        cosi = pm.Deterministic('cosi', sinψ*cosθ*at.sin(iorb)+cosψ*at.cos(iorb))
        i = pm.Deterministic('i', at.arccos(cosi))
        
        iso_cosi = pm.Uniform('iso_cosi', lower=0, upper=1)
        iso_cosψ = pm.Deterministic('iso_cosψ', at.sqrt(1-iso_cosi**2)*cosλ)  
        
        norm2 = pm.sample()
        
    with pm.Model() as model_norm3:

        cosψ = pm.TruncatedNormal('cosψ', mu=0.4, sigma=0.2, lower=-1, upper=1)
        
        ψ = pm.Deterministic('ψ', at.arccos(cosψ))
        sinψ = pm.Deterministic('sinψ', at.sqrt(1-cosψ**2))
        
        θ = pm.Uniform('θ', lower=0, upper=np.pi)
        cosθ = pm.Deterministic('cosθ', at.cos(θ))
        sinθ = pm.Deterministic('sinθ', at.sin(θ))

        # iorb
        iorb = np.pi/2

        # find λ in terms of ψ, θ, and iorb
        λ = pm.Deterministic('λ', at.arctan2(sinψ*sinθ, cosψ*at.sin(iorb)-sinψ*cosθ*at.cos(iorb)))
        cosλ = pm.Deterministic('cosλ', at.cos(λ))

        # find i in terms of ψ, θ, and iorb
        cosi = pm.Deterministic('cosi', sinψ*cosθ*at.sin(iorb)+cosψ*at.cos(iorb))
        i = pm.Deterministic('i', at.arccos(cosi))
        
        iso_cosi = pm.Uniform('iso_cosi', lower=0, upper=1)
        iso_cosψ = pm.Deterministic('iso_cosψ', at.sqrt(1-iso_cosi**2)*cosλ)
        
        norm3 = pm.sample()


    ### Make the plot ###

    plt.figure(figsize=(5,5),dpi=110)


    ### cosψ ~ Uniform(-1,1) ###

    cosψ = uni.posterior.cosψ.values.ravel()
    λ = uni.posterior.λ.values.ravel()
    i = uni.posterior.i.values.ravel()

    plt.subplot(4,3,1)
    plt.hist(cosψ, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$\cos{\psi} \sim \mathcal{U}(-1,1)$')
    plt.ylim([0,0.6])
    plt.xlim([-1,1])

    plt.subplot(4,3,2)
    plt.hist(λ, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$\lambda$')
    plt.ylim([0,0.5])
    plt.xlim([0,np.pi])
    plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi], ['0', '', r'$\pi/2$', '', r'$\pi$'])

    plt.subplot(4,3,3)
    plt.hist(i, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$i_\star$')
    plt.xlim([0,np.pi])
    plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi], ['0', '', r'$\pi/2$', '', r'$\pi$'])
    plt.ylim([0,0.55])


    cosψ = np.linspace(-1,1,200)
    pcosψ = np.ones_like(cosψ)/2

    λ = np.linspace(0,np.pi,200)
    cosλ = np.cos(λ)
    pcosλ = np.zeros_like(cosλ)
    for i,this_cosλ in enumerate(cosλ):
        pcosλ[i] = integrate.quad(lambda x: (1-this_cosλ**2*x**2)**-1.5*1/2,
                             0, 1)[0]*2/np.pi

    istar = np.linspace(0,np.pi,800)
    cosi = np.cos(istar)
    pcosi = np.zeros_like(cosi)
    for i,this_cosi in enumerate(cosi):
        if this_cosi > 0:
            pcosi[i] = integrate.quad(lambda x: this_cosi/x**2/np.sqrt(1-this_cosi**2/x**2)/np.sqrt(1-x**2)*1/2,
                               this_cosi, 1)[0]*2/np.pi
        else:
            pcosi[i] = integrate.quad(lambda x: this_cosi/x**2/np.sqrt(1-this_cosi**2/x**2)/np.sqrt(1-x**2)*1/2,
                               this_cosi, -1)[0]*2/np.pi
        
    plt.subplot(4,3,1)
    plt.plot(cosψ,pcosψ,lw=1.2)

    plt.subplot(4,3,2)
    plt.plot(np.arccos(cosλ),pcosλ*np.sqrt(1-cosλ**2),lw=1.2)

    plt.subplot(4,3,3)
    plt.plot(np.arccos(cosi), pcosi*np.sqrt(1-cosi**2),lw=1.2)


    ### cosψ ~ Normal(0,0.2) ###

    σ = 0.2

    cosψ = norm1.posterior.cosψ.values.ravel()
    λ = norm1.posterior.λ.values.ravel()
    i = norm1.posterior.i.values.ravel()

    plt.subplot(4,3,4)
    plt.hist(cosψ, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$\cos{\psi} \sim \mathcal{N}(0,0.2)$')
    plt.ylim([0,2.5])
    plt.xlim([-1,1])

    plt.subplot(4,3,5)
    plt.hist(λ, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$\lambda$')
    plt.ylim([0,1.5])
    plt.xlim([0,np.pi])
    plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi], ['0', '', r'$\pi/2$', '', r'$\pi$'])

    plt.subplot(4,3,6)
    plt.hist(i, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$i_\star$')
    plt.xlim([0,np.pi])
    plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi], ['0', '', r'$\pi/2$', '', r'$\pi$'])
    plt.ylim([0,0.55])


    cosψ = np.linspace(-1,1,200)
    pcosψ = 1/np.sqrt(2*np.pi*σ**2)*np.exp(-cosψ**2/2/σ**2)

    λ = np.linspace(0,np.pi,200)
    cosλ = np.cos(λ)
    pcosλ = np.zeros_like(cosλ)
    for i,this_cosλ in enumerate(cosλ):
        pcosλ[i] = integrate.quad(lambda x: (1-this_cosλ**2*x**2)**-1.5
                                  *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(this_cosλ**2*x**2-this_cosλ**2)/(this_cosλ**2*x**2-1)/2/σ**2),
                             0, 1)[0]*2/np.pi

    istar = np.linspace(0,np.pi,800)
    cosi = np.cos(istar)
    pcosi = np.zeros_like(cosi)
    for i,this_cosi in enumerate(cosi):
        if this_cosi > 0:
            pcosi[i] = integrate.quad(lambda x: this_cosi/x**2/np.sqrt(1-this_cosi**2/x**2)/np.sqrt(1-x**2)
                                  *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(1-this_cosi**2/x**2)/2/σ**2),
                                  this_cosi, 1)[0]*2/np.pi
        else:
            pcosi[i] = integrate.quad(lambda x: this_cosi/x**2/np.sqrt(1-this_cosi**2/x**2)/np.sqrt(1-x**2)
                                *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(1-this_cosi**2/x**2)/2/σ**2),
                                this_cosi, -1)[0]*2/np.pi

    plt.subplot(4,3,4)
    plt.plot(cosψ,pcosψ,lw=1.2)

    plt.subplot(4,3,5)
    plt.plot(λ,pcosλ*np.sqrt(1-cosλ**2),lw=1.2)

    plt.subplot(4,3,6)
    plt.plot(istar, pcosi*np.sqrt(1-cosi**2),lw=1.2)


    ### cosψ ~ Normal(-0.4,0.2) ###

    cosψ = norm2.posterior.cosψ.values.ravel()
    λ = norm2.posterior.λ.values.ravel()
    i = norm2.posterior.i.values.ravel()

    plt.subplot(4,3,7)
    plt.hist(cosψ, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$\cos{\psi} \sim \mathcal{N}(-0.4,0.2)$')
    plt.ylim([0,2.5])
    plt.xlim([-1,1])

    plt.subplot(4,3,8)
    plt.hist(λ, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$\lambda$')
    plt.ylim([0,1.5])
    plt.xlim([0,np.pi])
    plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi], ['0', '', r'$\pi/2$', '', r'$\pi$'])

    plt.subplot(4,3,9)
    plt.hist(i, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$i_\star$')
    plt.xlim([0,np.pi])
    plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi], ['0', '', r'$\pi/2$', '', r'$\pi$'])
    plt.ylim([0,0.55])


    cosψ = np.linspace(-1,1,200)
    pcosψ = 1/np.sqrt(2*np.pi*σ**2)*np.exp(-(cosψ+0.4)**2/2/σ**2)

    λ = np.linspace(0,np.pi/2,200)
    cosλ = np.cos(λ)
    pcosλ = np.zeros_like(cosλ)
    for i,this_cosλ in enumerate(cosλ):
        pcosλ[i] = integrate.quad(lambda x: (1-this_cosλ**2*x**2)**-1.5
                                  *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(np.sqrt((this_cosλ**2*x**2-this_cosλ**2)/(this_cosλ**2*x**2-1))+0.4)**2/2/σ**2),
                             0, 1)[0]*2/np.pi
        
    plt.subplot(4,3,8)
    plt.plot(λ,pcosλ*np.sqrt(1-cosλ**2),lw=1.2)

    λ = np.linspace(np.pi/2,3*np.pi/2,200)
    cosλ = np.cos(λ)
    pcosλ = np.zeros_like(cosλ)
    for i,this_cosλ in enumerate(cosλ):
        pcosλ[i] = integrate.quad(lambda x: (1-this_cosλ**2*x**2)**-1.5
                                  *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(np.sqrt((this_cosλ**2*x**2-this_cosλ**2)/(this_cosλ**2*x**2-1))-0.4)**2/2/σ**2),
                             0, 1)[0]*2/np.pi

    plt.plot(λ,pcosλ*np.sqrt(1-cosλ**2), c='C0',lw=1.2)
        
    istar = np.linspace(0,np.pi,800)
    cosi = np.cos(istar)
    pcosi = np.zeros_like(cosi)
    for i,this_cosi in enumerate(cosi):
        if this_cosi > 0:
            pcosi[i] = integrate.quad(lambda x: this_cosi/x**2/np.sqrt(1-this_cosi**2/x**2)/np.sqrt(1-x**2)
                                    *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(np.sqrt(1-this_cosi**2/x**2)-0.4)**2/2/σ**2),
                               this_cosi, 1)[0]/np.pi
        else:
            pcosi[i] = integrate.quad(lambda x: this_cosi/x**2/np.sqrt(1-this_cosi**2/x**2)/np.sqrt(1-x**2)
                                    *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(np.sqrt(1-this_cosi**2/x**2)-0.4)**2/2/σ**2),
                               this_cosi, -1)[0]/np.pi

    plt.subplot(4,3,7)
    plt.plot(cosψ,pcosψ,lw=1.2)

    plt.subplot(4,3,9)
    plt.plot(istar, pcosi*np.sqrt(1-cosi**2),lw=1.2)

    ### cosψ ~ Normal(0.4,0.2) ###

    cosψ = norm3.posterior.cosψ.values.ravel()
    λ = norm3.posterior.λ.values.ravel()
    i = norm3.posterior.i.values.ravel()

    plt.subplot(4,3,10)
    plt.hist(cosψ, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$\cos{\psi} \sim \mathcal{N}(0.4,0.2)$')
    plt.ylim([0,2.5])
    plt.xlim([-1,1])

    plt.subplot(4,3,11)
    plt.hist(λ, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$\lambda$')
    plt.ylim([0,1.5])
    plt.xlim([0,np.pi])
    plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi], ['0', '', r'$\pi/2$', '', r'$\pi$'])

    plt.subplot(4,3,12)
    plt.hist(i, color='#e5e1e0', density=True, bins=40)
    plt.title(r'$i_\star$')
    plt.xlim([0,np.pi])
    plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi], ['0', '', r'$\pi/2$', '', r'$\pi$'])
    plt.ylim([0,0.55])


    cosψ = np.linspace(-1,1,200)
    pcosψ = 1/np.sqrt(2*np.pi*σ**2)*np.exp(-(cosψ-0.4)**2/2/σ**2)

    λ = np.linspace(0,np.pi/2,200)
    cosλ = np.cos(λ)
    pcosλ = np.zeros_like(cosλ)
    for i,this_cosλ in enumerate(cosλ):
        pcosλ[i] = integrate.quad(lambda x: (1-this_cosλ**2*x**2)**-1.5
                                  *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(np.sqrt((this_cosλ**2*x**2-this_cosλ**2)/(this_cosλ**2*x**2-1))-0.4)**2/2/σ**2),
                             0, 1)[0]*2/np.pi
        
    plt.subplot(4,3,11)
    plt.plot(λ,pcosλ*np.sqrt(1-cosλ**2),lw=1.2)

    λ = np.linspace(np.pi/2,3*np.pi/2,200)
    cosλ = np.cos(λ)
    pcosλ = np.zeros_like(cosλ)
    for i,this_cosλ in enumerate(cosλ):
        pcosλ[i] = integrate.quad(lambda x: (1-this_cosλ**2*x**2)**-1.5
                                  *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(np.sqrt((this_cosλ**2*x**2-this_cosλ**2)/(this_cosλ**2*x**2-1))+0.4)**2/2/σ**2),
                             0, 1)[0]*2/np.pi

    plt.plot(λ,pcosλ*np.sqrt(1-cosλ**2), c='C0',lw=1.2)
        
    istar = np.linspace(0,np.pi,800)
    cosi = np.cos(istar)
    pcosi = np.zeros_like(cosi)
    for i,this_cosi in enumerate(cosi):
        if this_cosi > 0:
            pcosi[i] = integrate.quad(lambda x: this_cosi/x**2/np.sqrt(1-this_cosi**2/x**2)/np.sqrt(1-x**2)
                                    *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(np.sqrt(1-this_cosi**2/x**2)-0.4)**2/2/σ**2),
                               this_cosi, 1)[0]/np.pi
        else:
            pcosi[i] = integrate.quad(lambda x: this_cosi/x**2/np.sqrt(1-this_cosi**2/x**2)/np.sqrt(1-x**2)
                                    *1/np.sqrt(2*np.pi*σ**2)*np.exp(-(np.sqrt(1-this_cosi**2/x**2)-0.4)**2/2/σ**2),
                               this_cosi, -1)[0]/np.pi

    plt.subplot(4,3,10)
    plt.plot(cosψ,pcosψ,lw=1.2)

    plt.subplot(4,3,12)
    plt.plot(istar, pcosi*np.sqrt(1-cosi**2),lw=1.2)

    plt.tight_layout()

    plt.savefig(paths.figures / "transform.pdf", bbox_inches="tight", dpi=600)
    plt.close()