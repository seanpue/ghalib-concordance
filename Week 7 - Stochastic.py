# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Stochastic signals
# 
# Described by the laws of probablity; mean, variance, probability distributions

# <markdowncell>

# ### Autocorrelation
# 
# $Z_xx[k]=\sum\limits_{n=0}^{n=N-1} x[n]x[n+k]$ $k-N+1,...,N-1$
# 
# Measure periodicity of a signal, or degree of repeating patterns
# 
# Can be used to measure stochasticity; the lower the value, the higher the stochasticity

# <markdowncell>

# ### Power spectral density
# 
# $Xp[k] = lim_{N->\infty }|X[k]|^2$
# 
# where
# 
# $X[k]=\sum\limits_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$ $k=0,..,N-1,N$
# 
# basically the DFT to the limit; square value of the absolute value of the DFT
# N-> infiity; converges to  a function that is our spectral density

# <markdowncell>

# ### Stochastic model
# 
# There are many. We will use:
#     
# $yst[n]=\sum\limits_{k=0}^{N-1} u[n]h[n-k]$
# 
# $u[n]$: white noise
# 
# $h[n]$: impulse response of filter approximating input signal x[n]
# 
# Convolution of two signals; convolution of signal with white noise

# <markdowncell>

# ##### Spectral view:
#     
# $Yst_l[k]=|H_l[k]||U[k]|e^{j(\sphericalangle H[k]+\sphericalangle U[k])} =|\hat{X}_l[k]|e^{j\sphericalangle U[k]}$
# 
# $\hat{X}[k]|$: approximation of magnitude spectrum of input single $x[n]$
# 
# $\sphericalangle U[k]:$ spectral phases of noise signal
# 
# $l$: frame number
# 
# Convolution in the spectral domain is the product of the two spectra
# 
# In polar coordinates, the product of two magnitude spectra multiplied by exponential e to the j and the sum of the two phase spectra
# 
# Magnitude spectra of white noise is a flat line; a constant, so we can take out of equation.
# 
# As phase of model, use phase of white noise.
# 
# Take approximation of magnitude spectrum of our signal $|\hat{X}_l[k]|$ and take random phases $e^{j\sphericalangle U[k]}$for the modeling of the phase spectrum
# 
# details of shape are not relevant; rather, approximation of the time varying magnitude spectrum of the input signal.
# 
# phase = sequence of random numbers

# <markdowncell>

# ### LPC approximation
# 
# Linear Predictive Coding
# 
# 
# $\hat{x}[n] = \sum\limits_{k=1}^{K}a_kx[n-k]$ Linear combination of past samples = expression of IR filter — infinite impulse response filter—linear combination of previous samples; goal=find coefficients
# 
# $Error=\sum\limits_{n=-\infty }^{n=\infty}(x[n]+\sum\limits_{k=1}^{K} a_kx[n-k])^2$  — sum of original with approximated ; then narrowed to finite length signals; find a coefficient that minimizes the error signal
# 
# obtain a sample set of filter coefficients (sub k) and the frequency response of the resulting filter approximates the spectrum
# 
# voice sound commonly approximated with LPC; a way to approximate the resonances, the formants, of a signal; 

# <markdowncell>

# ### Envelope approximation
# 
# $\tilde{a}[k] = IDFT(LP(DFT(a[k])))$
# LP: low-pass filter [only accept lower part of spectrum]
# 
# $b[k]=IDFT(ZP(DFT(\tilde{a}[k])))$
# ZP: zero-padding
# 

# <markdowncell>

# ## Stochastic Synthesis using LPC
# 
# $yst[n] = \sum\limits_{k=1}^{K}a_ku[n-k]$
# $a_k$: filter coefficients
# $u[n]$: white noise
# 
# filter of white noise
# 
# can be direct for or lattice structure

# <markdowncell>

# ## Stochastic Synthesis using envelopes
# 
# $yst[n]=IDFT(|\tilde{X}[k]|e^{j\sphericalangle U[k]})$
# 
# smooth approximation of the signal; random phases; inverse of DFT
# 
# stochastic compression (take 1 of every 10 samples of magnitude spectrum
# 

# <markdowncell>

# ##7T2: Sinusoidal + Residual Modeling
# 
# Sinusoidal/Harmonic plus residiual model (SpR, HpR)
# Residual subtraction
# Harmonic plus residual system
# Sinusoidal/Harmonic plus stochastic model (SpS, HpS)
# Stochastic model of residual
# Harmonic plus stochastic system

# <markdowncell>

# ### Sinusoidal + Residual Model
# 
# $y[n]=\sum\limits_{r=1}^{R}A_r[n]cos(2\pi f_r[n]n)+xr[n]=ys[n]+xr[n]$
# 
# $R$: number of sinusoidal components
#     
# $A_r[n]$: instantaneous amplitude
#     
# $f_r[n]$: instantaneous frequency (Hz)
#     
# $xr[n]$=$x[n]-ys[n]$: residual component
#     
# $ys[n]$: sinusoidal component

# <markdowncell>

# ### Spectral View 
# 
# We develop from here; sum of the sinusoid as the sum of the transform the windows shifted to a frequency and scaled to the amplitudes of these sinusoids, plus the spectrum of the residiual components.
# 
# $Y_l[k]=\sum\limits_{r=1}^{R_l}A_{(r,l)}W[k-\hat{f}_{(r,l)}]+Xr_l[k]=Ys_l[k]+Xr_l[k]$]
# 
# $W[k]$ = spectrum of analysis window
# 
# $R_l$: number of sinusoidal components
# 
# $A_{(r,l)}$: amplitude of sinusoid
# 
# $\hat{f}_{(r,l)}$: normalized frequency of sinusoid
# 
# $Xr_l[k]=X_l[k]-Ys_l[k]$: resiudent component spectrum
# 
# $Ys_l[k]$: sinusoidal component spectrum
# 
# $l$: frame number
# 
# subtract generated from spectrum of same size and window=residual spectrum (usual 512 samples); use blackman-harris so it can be easily subtracted
# 
# inverse of that shows residual signal (e.g. breath noise of flute)

# <markdowncell>

# 
# To improve stocastic:
#     
#     smaller hop size, increase approx size-- A FINER GRAIN
#     
# With speak sound (not completely stochastic): 256 Hop, .2 approx
#     
# get rid of phase spectrum smooth out magnitude spectrum — sounds like a whispered type of sound
# FFT:
#     
# Blackman window—stable sound; good for low sidelobes; good signal to noise ratio
# 
# M:  blackman: 6 bins * fps / fundamental frequency—odd; to minimize rest of components, make bigger
#         
# analyze middle of sound
#     
# look for high stochastic in high frequencies; less harmonic; not clearly defined as partials
# 
# 1. Apply same parameters to harmonic model
# 
# inf crease max freq deviation in harmonic track shows unstable harmonics in high (with flute)
# 
# Stochastic approximation factor: reduces the whole spectrum by 90%
# 
# For stochastic, no need for odd-sized window or zero-padding for the FFT
# 
# DV?
# 
# resample: FFT approach; to downsample a signal
# 
# xw=x[10000:10000+M] * w
# mX = 20 * np.log10(abs([X[:

# <codecell>

Blackman is good for stable sound due to low sidelobes; good signal to noise ratio
window size: 6 * 44100 / 440 hz
    

# <markdowncell>

# 
# 6*44100/200=1323 (for DFT)
# 
# see low frequency harmonics
# unstable in high frequencies

# <codecell>

44100*6/100
2001
2048
-100
.1
100
40
300
5
0.01
.2

