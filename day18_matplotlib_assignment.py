import matplotlib as plt
import numpy as np
#plot 1:
x=np.array([10,20,30,40])
y=np.array(['A','B','C','D'])
plt.xlabel('Category')
plt.ylabel('Alphabets')
plt.subplot(1, 2, 1)
plt.barh(x, y,color="green",height=0.4)
#plot 2:
x=np.array([1,10])
y=np.array([8,280])
plt.xlabel('x')
plt.ylabel('y')
plt.subplot(1, 2, 2)
plt.plot(x, y,color="blue",marker='o')
#plot3;
x=np.array([35,25,30,40])
plt.subplot(1,2,3)
plt.plot(x)
#plot4:
x=np.array([3,5,10,20])
y=np.array([7,11,22,40])
plt.subplot(1, 2, 4)
plt.bar(x, y,color="magenta")
plt.show()
