from matplotlib import pyplot as plt 

days = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600]
names = ['Sempiternal','TTS','amo','PHSH','PHNG']
time = [81, 325, 157, 359, 589]


# also plt.plot, barh, bar
plt.barh(names, time) # can do color=''


plt.title('Days Between releases')
plt.xticks()
plt.xlabel('Days')
plt.ylabel('Albums')
plt.tight_layout()


plt.show()
