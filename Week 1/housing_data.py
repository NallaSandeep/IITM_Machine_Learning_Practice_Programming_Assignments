from sklearn.datasets import fetch_california_housing
housing_data = fetch_california_housing()
print(housing_data.data.shape)
print(housing_data.target[:5])
print(housing_data.feature_names)
print(housing_data.target_names)