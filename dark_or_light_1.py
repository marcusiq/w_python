# START WITH EXAMPLE 1 -->  then EXAMPLE 2 -->  then EXAMPLE 3


# Step 1 - Create a numpy array of measurements X.
# Instead of 30, there will be only 4 features - one for each element in the 2x2 array of light and dark cells.

import numpy as np
zero_one = [0, 1]
X = [ np.array([a, b, c, d])  for a in zero_one   for b in zero_one  for c in zero_one  for d in zero_one  ]
# for x in X: print x

X_with_repeats = []
for x in X:
    X_with_repeats.append(x)
    for y in X:
        X_with_repeats.append(y)

print "The length of X_with_repeats is: ", len(X_with_repeats)
X = np.array(X_with_repeats)  # convert to a 2D np array


# Step 2 - Create a numpy array y with the targets or dark/light classification.

y = [sum(x)  for x in X]
# print y

def  dark_or_light(n):
    if n in [0, 1]: return 0
    else:
        return 1

y = [ dark_or_light(n) for n in y  ]
# print y


# * * * * * NEW STUFF FOR EXAMPLE 2 STARTS HERE

# Let's split our data into training and testing sets, this is done easily with SciKit Learn's
# train_test_split function from model_selection:

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# print "\nHere is the X_train data:\n", X_train

# print "\nHere is the X_test data:\n", X_test



# 2B * * * * * * * * * *  Data Preprocessing * * * * * * * * * * * *


"""
Data Preprocessing
    The neural network may have difficulty converging before the maximum number of iterations allowed if the data is not normalized. 
    Multi-layer Perceptron is sensitive to feature scaling, so it is highly recommended to scale your data. 
    Note that you must apply the same scaling to the test set for meaningful results. 
    There are a lot of different methods for normalization of data, we will use the built-in StandardScaler for standardization.
"""

#
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit only to the training data
scaler.fit(X_train)
#
print "\n\nWhat type of thing is scaler? ", type(scaler)
print scaler
#
# # Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#print "\nHere is the transformed X_train data:\n", X_train
#print "\nHere is the transformed X_test data:\n", X_test


# * * * * * NEW STUFF FOR EXAMPLE 32 STARTS HERE

# * * * * * * * * * * * * * * * NEW * * * * * * * * * * * * * * * * * *
# 3A * * * * * * * * * *  Train the Model * * * * * * * * * * * *






"""
Training the model
    Now it is time to train our model. SciKit Learn makes this incredibly easy, by using estimator objects. 
    In this case we will import our estimator (the Multi-Layer Perceptron Classifier model) 
    from the neural_network library of SciKit-Learn!
"""
from sklearn.neural_network import MLPClassifier



"""
Next we create an instance of the model, there are a lot of parameters you can choose to define and customize here, 
    we will only define the hidden_layer_sizes. 
    For this parameter you pass in a tuple consisting of the number of neurons you want at each layer, 
    where the nth entry in the tuple represents the number of neurons in the nth layer of the MLP model. 
    There are many ways to choose these numbers;  - - explore!!
"""


mlp_1 = MLPClassifier(hidden_layer_sizes=(20), solver='lbfgs', learning_rate_init=100)# most robust
#mlp_2 = MLPClassifier(hidden_layer_sizes=(20), solver='sgd', learning_rate_init=.01) # easiest to break
#mlp_3 = MLPClassifier(hidden_layer_sizes=(20), solver='adam', learning_rate_init=.01)# not as hard to break
# Now that the model has been made we can fit the training data to our model,S
# remember that this data has already been processed and scaled:

fitted_model_1 = mlp_1.fit(X_train,y_train)
#fitted_model_2 = mlp_2.fit(X_train,y_train)
#fitted_model_3 = mlp_3.fit(X_train,y_train)
print fitted_model_1
#print fitted_model_2
#print fitted_model_3
# You can see the output that shows the default values of the other parameters in the model.
# Play around with them and discover what effects they have on your model!
"""  3B
Predictions and Evaluation
    Now that we have a model it is time to use it to get predictions! 
    We can do this simply with the predict() method off of our fitted model:
"""
predictions_1 = fitted_model_1.predict(X_test)
pred_12 = mlp_1.predict(X_test)
#predictions_2 = fitted_model_2.predict(X_test)
#pred_22 = mlp_2.predict(X_test)
#predictions_3 = fitted_model_3.predict(X_test)
#pred_33 = mlp_3.predict(X_test)
#print "Here are the model's predictions after training:\n", predictions_1
#print pred_12
"""
    Now we can use SciKit-Learn's built in metrics such as a classification report 
    and confusion matrix to evaluate how well our model performed:
"""
from sklearn.metrics import classification_report,confusion_matrix
print "\n\nCONFUSION MATRIX"
Confusion_Matrix = confusion_matrix(y_test, predictions_1) # it's a numpy array
print "Model lbfgs fitted\n", Confusion_Matrix
conf_1 = confusion_matrix(y_test, pred_12)
print "Model lbfgs unfitted\n", conf_1
#Confusion_Matrix2 = confusion_matrix(y_test, predictions_2) # it's a numpy array
#print "Model sgd fitted\n", Confusion_Matrix2
#conf_2 = confusion_matrix(y_test, pred_22)
#print "Model sgd unfitted\n", conf_2
#Confusion_Matrix3 = confusion_matrix(y_test, predictions_3) # it's a numpy array
#print "Model adam fitted\n", Confusion_Matrix3
#conf_3 = confusion_matrix(y_test, pred_33)
#print "Model adam unfitted\n", conf_3
number_misclassified = Confusion_Matrix[0][1] + Confusion_Matrix[1][0]
print "The number of misclassified dark or light images is: ", number_misclassified

print "\n\nCLASSIFICATION REPORT"

print(classification_report(y_test,predictions_1))
print(classification_report(y_test,pred_12))



