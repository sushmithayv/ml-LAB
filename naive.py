import csv

# Load the dataset from a CSV file
data = []
with open('weather_dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Remove the header row
header = data[0]
data = data[1:]

# Split the data into features and target variable
X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Calculate the prior probabilities for each class
class_counts = {}
for value in y:
    if value in class_counts:
        class_counts[value] += 1
    else:
        class_counts[value] = 1

prior_probabilities = {}
for value, count in class_counts.items():
    prior_probabilities[value] = count / len(y)

# Calculate likelihood probabilities for each feature
likelihood_probabilities = {}
total_features = len(X[0])

for feature_index in range(total_features):
    feature_counts = {}
    for i in range(len(X)):
        feature_value = X[i][feature_index]
        label = y[i]
        
        if feature_value in feature_counts:
            if label in feature_counts[feature_value]:
                feature_counts[feature_value][label] += 1
            else:
                feature_counts[feature_value][label] = 1
        else:
            feature_counts[feature_value] = {label: 1}
    
    likelihood_probabilities[feature_index] = feature_counts

# Get user input for feature values
outlook = input("Enter outlook (Sunny, Overcast, Rainy): ")
temperature = input("Enter temperature (Hot, Mild, Cool): ")
humidity = input("Enter humidity (High, Normal): ")
windy = input("Enter windy (True, False): ")

# Calculate the probabilities for each class based on user input
class_probabilities = {}
for value in class_counts:
    class_probability = prior_probabilities[value]
    for feature_index in range(total_features):
        feature_value = eval(header[feature_index])[value]
        feature_likelihood = likelihood_probabilities[feature_index].get(feature_value, {}).get(value, 0)
        class_probability *= feature_likelihood / class_counts[value]
    
    class_probabilities[value] = class_probability

# Make a prediction based on user input
prediction = max(class_probabilities, key=class_probabilities.get)

# Print the predicted target value
print("Predicted target value:", prediction)
















import csv

# Load the dataset from a CSV file
data = []
with open('weather_dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Remove the header row
header = data[0]
data = data[1:]

# Split the data into features and target variable
X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Calculate the prior probabilities for each class
class_counts = {}
for value in y:
    if value in class_counts:
        class_counts[value] += 1
    else:
        class_counts[value] = 1

prior_probabilities = {}
for value, count in class_counts.items():
    prior_probabilities[value] = count / len(y)

# Calculate likelihood probabilities for each feature
likelihood_probabilities = {}
total_features = len(X[0])

for feature_index in range(total_features):
    feature_counts = {}
    for i in range(len(X)):
        feature_value = X[i][feature_index]
        label = y[i]
        
        if feature_value in feature_counts:
            if label in feature_counts[feature_value]:
                feature_counts[feature_value][label] += 1
            else:
                feature_counts[feature_value][label] = 1
        else:
            feature_counts[feature_value] = {label: 1}
    
    likelihood_probabilities[feature_index] = feature_counts

# Get user input for feature values
outlook = input("Enter outlook (Sunny, Overcast, Rainy): ")
temperature = input("Enter temperature (Hot, Mild, Cool): ")
humidity = input("Enter humidity (High, Normal): ")
windy = input("Enter windy (True, False): ")

# Calculate the probabilities for each class based on user input
class_probabilities = {}
for value in class_counts:
    class_probability = prior_probabilities[value]
    for feature_index in range(total_features):
        feature_value = eval(header[feature_index])[value]
        feature_likelihood = likelihood_probabilities[feature_index].get(feature_value, {}).get(value, 0)
        class_probability *= feature_likelihood / class_counts[value]
    
    class_probabilities[value] = class_probability

# Make a prediction based on user input
prediction = max(class_probabilities, key=class_probabilities.get)

# Print the predicted target value
print("Predicted target value:", prediction)

# Calculate accuracy
actual_value = input("Enter actual target value: ")
accuracy = 1 if actual_value == prediction else 0
print("Accuracy:", accuracy)
