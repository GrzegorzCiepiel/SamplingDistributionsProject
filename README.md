# Sampling distribution project #

## Introduction ##
  Using spotify_data.csv which is publicated at: 
  https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify
  I try to answer a following question: 
  I want to make a party and take randomly chosen music from spotify.
  I would like to play music that is 140bpm or more becouse it will be better to dance.
  I would like to have in my playlist plenty songs with more than 150 beats per minute. 
  
  ***What is the probability that the sample mean of 40 selected songs is less than 140bpm?***
  ***What is the probability that the same sample is greater than 150bpm?***

 ## Analyse ##
   I use python 3.11 and work on pycharm

   ### As a first part of that project I decided to make a review from sampling distribution. ###
  I selected "tempo" where each song is described in bits per minute
  I want to compare tempo  distribution in whole dataset with distribution of mean from 500 randomly
  chosen samples of 30 songs.

  

  ![pop_distribution](https://github.com/GrzegorzCiepiel/SamplingDistributionsProject/assets/135313652/1ae49a93-a34a-43c2-9ee4-bbcbfc6b860f)
![samp_mean_distribution](https://github.com/GrzegorzCiepiel/SamplingDistributionsProject/assets/135313652/57baa7fd-2707-4b64-b12e-478215566de7)

As we can see the mean of sample distribution of mean and the whole population of tempos mean are almost equal.
The spread of the sample distribution of the mean looks normally distributed. That is what Cental Limit Theorem stands for.

On the other hand here is a plot showing sample distribution of mean of minimal tempos:

![samp_min_distribution](https://github.com/GrzegorzCiepiel/SamplingDistributionsProject/assets/135313652/f7f44b8f-1517-4b13-b051-1184a2a64ce5)

As we can see this time - values of the mean of the sample minimum and population minimum are not even close to each other.

 ### Second part - answering questions. ###

The tempos population mean is equal to 147.74 bpm

standard_error = population_std/30**0.5 and is equal to: 4.35

I calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs:
prob1 = stats.norm.cdf(140, 147.74, 3.35).
Probability is equal to ***3.7%***

Calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs:
prob2 = stats.norm.cdf(150, 147.74, 3.35).
Probability is equal to ***30.3%***


***We can assume that in random sample from spotify music 3% of songs is under 140bps and 30% is over 150bps.***
