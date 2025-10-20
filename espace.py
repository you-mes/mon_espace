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
#plott.grid(True)

plott.show()

categories = ['Electronics', 'Furniture', 'Clothing', 'Food', 'Toys']
category_sales = [1500, 1200, 950, 1800, 700]

color_multiple=['red', 'green', 'blue', 'yellow', 'violet']
plott.bar(categories, category_sales,  color=color_multiple)

plott.title('sales by produt categoriy')
plott.xlabel('category')
plott.ylabel('total sales(s)')
plott.grid(True)
plott.legend('barchar')
#plott.show()
