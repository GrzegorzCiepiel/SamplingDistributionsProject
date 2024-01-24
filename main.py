from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Read data from csv file
spotify_data = pd.read_csv('spotify_data.csv')
# Preview the dataset
print(spotify_data.head())
# Prepare dataset to work on
song_tempos = spotify_data.tempo


# Calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)

# Plot the population distribution with the mean labeled
population_distribution(song_tempos, population_mean)
# Sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean" )
# Sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")
# Sampling distribution of the sample variance


# Calculate the standard error
standard_error = population_std/30**0.5
print(standard_error)
# Calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140, 147.74, 4.35))
# Calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
print(1 - stats.norm.cdf(150, 147.74, 4.35))