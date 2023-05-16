import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fun(data):
    dataset = pd.read_csv(data)
    # print(dataset.shape) #(rows,columns)
    # print(dataset.head(5)) #first 5 of the table

    """### Upper Confidence Bound"""

    import math
    observations = 10000
    no_of_Ads = 10
    ads_selected = []
    numbers_of_selections_of_each_ads = [0] * no_of_Ads
    sums_of_rewards_of_each_ads = [0] * no_of_Ads
    total_reward = 0
    for n in range(0, observations): #traversing rows
        ad = 0
        max_upper_bound = 0
        for i in range(0, no_of_Ads): #traversing columns
            if (numbers_of_selections_of_each_ads[i] > 0):#from dataset we are checking
                average_reward = sums_of_rewards_of_each_ads[i] / numbers_of_selections_of_each_ads[i]
                delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections_of_each_ads[i])
                upper_bound = average_reward + delta_i
            else:
                upper_bound = 1e400 #if not greater than zero then assign infinity
            if upper_bound > max_upper_bound:
                max_upper_bound = upper_bound
                ad = i
        ads_selected.append(ad)
        numbers_of_selections_of_each_ads[ad] = numbers_of_selections_of_each_ads[ad] + 1
        reward = dataset.values[n, ad]
        sums_of_rewards_of_each_ads[ad] = sums_of_rewards_of_each_ads[ad] + reward
        total_reward = total_reward + reward

    # print("Rewards by Ads = ",sums_of_rewards_of_each_ads)
    # print("Total Rewards by UCB = ",total_reward)
    # print("Ads selected at each round:",ads_selected)

    """### Visualizing Result"""

    plt.hist(ads_selected)
    plt.title('Histogram of ads selections')
    plt.xlabel('Ads')
    plt.ylabel('Number of times each ad was selected')
    plt.show()

    return sums_of_rewards_of_each_ads