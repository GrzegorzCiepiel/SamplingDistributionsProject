import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def choose_statistic(x, sample_stat_text):
  # calculate mean if the text is "Mean"
  if sample_stat_text == "Mean":
    return np.mean(x)
  # calculate minimum if the text is "Minimum"
  elif sample_stat_text == "Minimum":
    return np.min(x)
  # calculate variance if the text is "Variance"
  elif sample_stat_text == "Variance":
    return np.var(x)
  # calculate variance if the text is "Mode"
  elif sample_stat_text == "Mode":
      return np.mode(x)
  # calculate variance if the text is "St deviation"
  elif sample_stat_text == "Std":
      return np.std(x)

  else:
    raise Exception('Make sure to input "Mean", "Minimum", "Mode", "Std" or "Variance"')


def population_distribution(population_data, mean):
  # plot the population distribution
  sns.histplot(population_data, stat='density', color=("#5A9"))
  plt.title(f"Population Distribution \n"
            f"Population mean : {round(np.mean(mean), 2)}")
  plt.axvline(mean, color='red', linestyle='dashed', label=f'Population {mean}')
  # remove None label
  plt.xlabel('')
  plt.show()
  plt.clf()


def sampling_distribution(population_data, samp_size, stat):
# list that will hold all the sample statistics
  sample_stats = []
  for i in range(500):
    # get a random sample from the population of size samp_size
    samp = np.random.choice(population_data, samp_size, replace=False)
    # calculate the chosen statistic (mean, minimum, or variance) of the sample
    sample_stat = choose_statistic(samp, stat)
    # add sample_stat to the sample_stats list
    sample_stats.append(sample_stat)

  pop_statistic = round(choose_statistic( population_data, stat), 2)

  # plot the sampling distribution
  sns.histplot(sample_stats, stat='density', bins=30, color='purple')
  plt.title(f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n "
            f"Population {stat}: {pop_statistic}")
  plt.axvline(pop_statistic, color='green', linestyle='dashed', label=f'Population {stat}')
  # plot the mean of the chosen sample statistic for the sampling distribution
  plt.axvline(np.mean(sample_stats), color='orange', linestyle='dashed', label=f'Mean of the Sample {stat}s')
  plt.legend()
  plt.show()
  plt.clf()