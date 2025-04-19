# Advance Python Questions With Answers

# Q1. What is the difference between deed and shallow copy in python?
# ANS:

# Shallow copy example

# a = [1, 2, 3, 4, 5]
# b = a
# b[2] = 10
# print(b)
# print(a)

# Deep Copy Example

# a = [1,2, 3, 4, 5]
# b = a.copy()
# b[2] = 10
# print(a)
# print(b)

# Q2: I don't have an idea yet, so ignore this one.

# Q3: What are python generators and how are they different from iterators?
# ANS:

# Iterators Example

# lst = [1,2,3,4,5]

# iter_object = iter(lst)

# for i in iter_object:
#     print(i)

# Iterator just iterate over a sequence

# Generator Example

# def generate(x):
#     for i in range(0, x):
#         yield i

# for i in generate(10):
#     print(i)

# Generator Generate storing one item at a time in memory

# Q4: Explain Decorators, How do they work under the hood?

# Normal Without decorator
# def greet(name):
#     print(f'Hello, {name}')

# greet('talha') 

# With Decorator
# def outer_func(func):
#     def wrapper(*args, **kwargs):
#         print(f'Good Morning')
#         func(*args, **kwargs)
#         print('Bye, Bye...')

#     return wrapper

# @outer_func
# def greet(name):
#     print(f'Hello, {name}')

# greet('talha')

# Q5: What's the Global Interpreter Lock (GIL)?
# ANS: I don't actually Know this but I know something that when you run python it actually run a single thread which go line by line so thats why we create multiple threads and also when the threads are running they are actually not running paralley I think so it is related to GIL.

# Q6: What are python data model (dunder) methods?
# ANS: Dunder methods are actually called magic methods which use case is when ever we called and create our class object so there are some dunder methods in it which automatically calls whenever the object is created like.

# class Demo:
#     def __init__(self):
#         print('This initiates automatically...')

# obj = Demo()

# Q7: What are the difference between @classmethod, @staticmethod, and the instance methods like self.
# ANS: See, whenever we create a class the self represents in it that for what object we are creating our class instance the self is basically that object name for which all the methods and attributes will be assigned. Class method is a decorator which can be used in a method in class normally a method is assigned to object (self) but with @classmethod decorator the object is now initiating for class means the method is now for class. @staticmethod is used to use the method of a class without creating any object of that class so it means that we don't have to put self in the method because the method is not initiating for object of that class.

# Q8: How would you implement a custom context manager (with 'with' statement)?
# ANS: 

# class ContextManager:
#     def __init__(self, file, mode):
#         self.file = open(file, mode)

#     def __enter__(self):
#         return self.file
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()

# with ContextManager('test.txt', 'w') as f:
#     f.write('Test')

# Q9: What's the difference between 'is' and '==' ? 
# ANS: '==' sign basically compares value and on other hand 'is' compares type.

# a = 1000
# b = 1000

# print(id(a))
# print(id(b))

# print(a == b)
# print(a is b)

# Q10: I will learn this later so yes, thats it.

# Data Science Related Questions

# Q1: How would you handle missing data in a large dataset? Different strategies?
# ANS: Handling Missing data it depends, whether its a numerical column or categorical column for categorical we can use mode tecnique and for numerical we can use mean if the column distribution is good else median.

# Q2: Explain broadcasting in NumPy. 
# ANS: I think so it is like an array is able to add, mulitply, divide, subtract to an array matrix or scalar.

# Q3: What’s the difference between .loc, .iloc, and .at in Pandas?
# ANS: I know it they use in accessing the location of a row in a data frame.

# Q4: How would you identify and remove multicollinearity?
# ANS: Multicollinearity means unnecessary columns which cause overfitting so we can use Reqularization techniques and PCA.

# Q5: What are the steps of performing Exploratory Data Analysis (EDA)?
# ANS: First of all collect data then we do low level analysis like checking out the shape, datatypes, missing values, duplicates then we start doing univariate analysis means analyzing only single and each columns there comes so much varaitey of plots then we do bivariate analysis in which we use 2 and more colums for our analysis.

# Q6: How do you deal with outliers in a dataset? When should you remove them?
# ANS: When the distribution of a column is messed out so we use outlier removal techniques like z-score in which we calculate 25percentile and 75percentlie of our data and then we calculate IQR and use a formula I am not gettting up with that but yes we can cap up or trim the higher and lower range.

# Q7: I don't know yet

# Q8: I want to know.

# Q9: What are some feature engineering techniques you frequently use?
# ANS: I want to know, but I use simple things like add two columns and that kind of things.

# Q10: How would you handle categorical data in ML preprocessing? Multiple ways?
# ANS: Handling Categorical data depends on our categories in data if we have non-order categories like ['Male', 'Female'] we simply use One Hot Encoding because the categoires have no order but if there is an order in categories we use ordinal encoding or also we can custom map it.

# Machine Learning Questions

# Q1: What’s the difference between bias and variance? What is the bias-variance tradeoff?
# ANS: Bias means low learning and Variance means high almost learns everything I need better explanation, and bias-variance tradeoff means our goal is to find the generalized model low variance low bias model 

# Q2: When would you use Logistic Regression over a Decision Tree and vice versa?
# ANS: I acutually forogot what is better over what but I know the working of these models Like logistic regression is used for classification purposes learning from data and used to predict classes it is like linear regression but there is some changes like the formula (y = mx + b) the output of this we will take and check if its greater than 0 than we assign it with one class and if less than 0 than again we assign it a class so it will become binary classification we can also do multi-class classification but what makes logistic regression is sigmoid because without sigmoid we are actually not caputuring the non linearity in our data with sigmoid we can now caputure non-linearity by squishing the outputs between 0-1 and forming a sigmoid curve. Decision tree can be both used with classification and regression purposes it has no forumlas like previous but it learns from decisions decision tree form trees of decsions while learning from our data.

# Q3: How does regularization work in linear models (L1 vs L2)?
# ANS: we basically make some changes to our formula with it like avoiding the loss to go to zero I want more explanation.

# Q4: What is the ROC curve and what does AUC represent?
# ANS: I want to know.

# Q5: Difference between bagging and boosting? Examples of algorithms?
# ANS: These all are ensemble techniques like in bagging we have a data in which we use some random data and feed it into one model we do this with several models with different different data, In boosting we will give the data to our first model which outputs then go into other model I think so I need more clarity.

# Q6: How does random forest reduce overfitting?
# ANS: Because it uses bagging technique in which we feed different data to decision tree and then aggregate or mean the outputs of each dt model.

# Q7: What is cross-validation and why do we use it?
# ANS: In cross-validation we basically test our model with our data by not actually training it but testing our model on data I also want explanation of it.

# Q8: How does SVM work and what is the kernel trick?
# ANS: I know this but I forgot now I only know there is positive and negative marginal plane this svm can be used in classifiaction and regression tasks like in classification our goal is to find the most spaced marginal plane I want more explanation.

# Q9: What is dimensionality reduction and how does PCA work?
# ANS: PCA is used to reduce mulicollinearity and curse of dimensionality in our data and also helps us to understand high dimensional data into like 2 or 3 dimensional lets say we have 100d data now what PCA does is plot all the variance to let say 2d or 3d right.

# Q10: How do you handle class imbalance in classification problems?
# ANS: I have an idea but not in detailed let me explain it to you like we have imbalanced classes like 500 in one class and 100 in other so our goal is to balance it by using upsampling, downsampling and SMOTE techniques.

# Deep Learning Questions.

# Q1: What is the vanishing gradient problem? How do ReLU and batch normalization help?
# ANS: So when our Neural Network forward propagates on our data and then when we calculates our loss and then backward propagates we calculate gradients and update each weights in our architecture so when we use sigmoid lets say as an activation function then if the architecture is big so the gradients become so small for the early layers by chain ruling so the early start layers wieghts stops training thats called vainishing gradients and in exploding gradients the gradients becomes so large and with ReLU the outputs of a neuron squished into (0, x) which will help to reduce these problems.

# Q2: What are the differences between CNNs and RNNs? When would you use each?
# ANS: So simple CNNs means Convolutional Neural Networks it is used in learning patterns from images it has bunch of filters in it which are used to learn and extract images patterns edges and more so basically it is used to learn pattern from images. RNNs other hand used for learning patterns from textual data in older technique we only convert text into vector representation and then train that data to our normal ML algorithms but there is a problem we are not learning sequence in our data so thats why we use RNNs it helps us to learn not only patterns from data but the sequnence of the text.

# Q3: How does dropout work and why is it useful?
# ANS: We use dropout in our Neural Network Architecutre bascially it will turn off some % of neurons in a layer, % will be set and also the layers, basically it will help us to learn patterns without forming complex model.

# Q4: Explain how backpropagation works. What gets updated during training?
# ANS: So lets suppose we have a fully build Neural Network Architecture and we have a data with some features and rows now we initiate the training of our data we take first row of our data passes from all the neurons weighted average all the weights with the inputs and do this same withh all neurons and further with every layers then when the final output layers comes and also when the prediction will come from the model we calculate the loss of the prediction and actual output then our goal is to optimze the model performance by adjusting weights so we backpropagate it by chain ruling we go to each weights and use optimiziers like Adam to optimize the weigths there is techiques like we can optimze the weights by epochs or by each iteration over each rows.

# Q5: What is the role of the learning rate in training a neural network?
# ANS: Learning rates play a important role in optimzing the weights the lower the learning rate the lower the training time will the higher the learning rate the faster the training will be I think so it will manipulate the gradients.

# Q6: What are weight initialization techniques and why are they important?
# ANS: I don't know but I remember that when training starts the weight will initialize randomly so I think so it is connected to the question.

# Q7: What is transfer learning and how do you use pretrained models effectively?
# ANS: In transfer learning we use pretrained model with our model means lets say we have a pretrained model trained on images so what we does is remove the nn layers from it and include ours so now what happens is when we train the model weights of filter is not training only for NN with this the training will be fast and model will be good or we can unfreeze some convolutional layers.

# Q8: Explain attention mechanism in deep learning.
# ANS: I can explain you the whole Transformer Architecture but Lol it will take whole day, btw In attention mechanism we are giving attention to not all the words only that words which have connection.

# Q9: What’s the difference between Batch Norm and Layer Norm?
# ANS: I don't know.

# Q10: Explain the architecture of a typical ResNet model and its skip connections.
# ANS: I don't know.