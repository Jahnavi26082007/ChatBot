from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
Y = [30, 40, 50, 60, 70]

model = LinearRegression()

model.fit(X, Y)

prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])