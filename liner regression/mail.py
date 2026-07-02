import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data_file/house_prices_practice.csv" , delimiter = "," , skiprows = 1)
print(data)
x = data[:, :9]
y = data[:, 9].reshape(-1,1)
x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
x = np.c_[np.ones((x.shape[0],1)), x]
print(x.shape)
print(y.shape)

def model(x,y,learning_rate,iteration):
    m = y.size
    theta = np.zeros((x.shape[1],1))
    cost_list = []
    for i in range(iteration):
        y_pred = np.dot(x,theta)
        cost =  (1/(2*m)*np.sum(np.square(y_pred - y)))
        d_theta = (1/m)*np.dot(x.T,y_pred - y)
        theta =  theta - learning_rate*d_theta
        cost_list.append(cost)
        if i % 10 == 0:
            print(f"Iteration {i}, Cost = {cost}")
    return theta,cost_list  

iteration = 1000
learning_rate = 0.01
theta , cost_list= model(x,y,learning_rate = learning_rate,iteration = iteration)
rng = np.arange(0,iteration)
plt.scatter(rng,cost_list)
plt.show()
plt.plot(rng,cost_list)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost vs Iterations")
plt.show()

y_pred = np.dot(x, theta)
plt.scatter(y, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted")
plt.show()