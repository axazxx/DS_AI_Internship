#task 2

import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.bar(['Electronics', 'Clothing', 'Home'],[300, 450, 200])
plt.title("Bar Chart")
plt.subplot(1,2,2)
plt.plot([2,4,6,8,10],[500,2000,1500,700,1200])
plt.tight_layout()
plt.show()