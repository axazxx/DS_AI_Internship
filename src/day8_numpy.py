#task 1

import numpy as np

np.random.seed(42) 
scores = np.random.randint(50, 101, size=(5, 3))

subject_means = scores.mean(axis=0)

centered_scores = scores - subject_means

print("Original Scores:\n", scores)
print("\nCentered Scores:\n", centered_scores)

#task 2

import numpy as np

sensor_data = np.arange(24)

reshaped_data = sensor_data.reshape(4, 3, 2)

final_data = reshaped_data.transpose(0, 2, 1)

print("Final Shape:", final_data.shape)
print("\nFinal Array:\n", final_data)
