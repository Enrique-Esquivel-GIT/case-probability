import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# Known statistic
P_deadline = 0.80
deadline = 3  # months

# Choose shape parameter (spread)
sigma = 0.6

# Solve for mu so that P(T <= 3) = 0.80
q = lognorm.ppf(P_deadline, s=sigma, scale=1)
mu = np.log(deadline / q)

# Define distribution
dist = lognorm(s=sigma, scale=np.exp(mu))

# Time grid (case age)
t = np.linspace(0, deadline, 200)

# Conditional probability
F_deadline = dist.cdf(deadline)
F_t = dist.cdf(t)

P_conditional = (F_deadline - F_t) / (1 - F_t)

# Plot
plt.figure()
plt.plot(t, P_conditional)
plt.xlabel("Case age (months)")
plt.ylabel("P(resolution ≤ 3 months | survived to t)")
plt.title("Probability of finishing by 3 months vs case age")
plt.show()

print("mu =", mu, "sigma =", sigma)
