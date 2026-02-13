#task 1

import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]
plt.xlabel("months")
plt.ylabel("revenue")
plt.plot(months, revenue)
plt.title("Monthly Revenue Growth")
plt.show()