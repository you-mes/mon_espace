import matplotlib.pyplot as plott 
import random
def generate_age(n, min, max):
             ag=[random.randint(min, max) for _ in range(n)]
             return ag 
age=generate_age(100, 18, 70)
#print(age)  

plott.hist(age, bins=100, color='blue', edgecolor='black')

plott.title('age distribution of your customers')
plott.xlabel('age')
plott.ylabel('frequency')
plott.grid(True)

plott.show()


