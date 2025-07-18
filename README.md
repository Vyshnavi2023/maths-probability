# maths-probability
random experiments on probability
📌 Objective:
This project simulates rolling a fair six-sided dice multiple times to estimate the probability of getting an even number (2, 4, or 6). It helps visualize how experimental probability converges to theoretical probability over time using the Law of Large Numbers.

📈 What the Code Does:
Rolls a dice randomly for 100 trials.
Counts how many times an even number appears.

Calculates the running probability at each trial:
P(even) = (Number of even outcomes) / (Total rolls)

Plots the result using Matplotlib, with:
X-axis: Number of trials
Y-axis: Estimated probability
A red dashed line at 0.5 to represent the expected probability (since 3 out of 6 dice faces are even).
