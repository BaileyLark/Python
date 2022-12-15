from matplotlib import pyplot as plt

print(plt.style.available)

plt.style.use('seaborn-talk')
plt.xkcd

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
dev_y = [38496, 42000, 46753, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 74453]
pydev_y = [45372, 48874, 53850, 57831, 63045, 65234, 70420, 72042, 75604, 76534, 79534, 81374]

plt.plot(ages_x, pydev_y, label='All Devs', color='k', linestyle='--')
plt.plot(ages_x, dev_y, label='Python', color='b', linestyle='--', linewidth=3)
plt.title('Median Salary by Age')
plt.xlabel('Age')
plt.ylabel('Salary (USD)')
plt.legend()
plt.show()