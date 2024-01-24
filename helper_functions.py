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