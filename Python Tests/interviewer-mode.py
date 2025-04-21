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

# NLP Related Questions

# Q1: What is tokenization? How does it differ in traditional NLP and transformer models?
# ANS: Tokenization is basically splitting a whole text into words or sentences we will take splitting whole corpus into words it helps us to convert those words to embeddings and then train the model for better pattern learning and also for transformer it helps to give attention to specific words right.

# Q2:  Explain how TF-IDF works. Why is it better than just frequency count?
# ANS: I have learn the implementation of it but I forgot it but I know that it helps to convert each text row into vector representation and I also know the frequency count one it is call BOW means the BOW will take the whole vocabulary words we can also set limit and then take each text row in our data and then if each word is present in our vocabulary which we have created we increment it with 1 otherwise 0 that will be our vector representation of each row in our data.

# Q3: What is POS tagging and why is it useful?
# ANS: I Think so it converts the word to its pos or it will tag the word to its respective pos, explain me if i am wrong.

# Q4: Difference between stemming and lemmatization? Which is more accurate and why?
# ANS: Good question, what stemming actually does is split the word into two parts and select one part means it removes the end es, ing, s, you got it. And Lemmatization does is it converts the word to its root word form means if there is a word running it will convert it to run if dancing so it will become dance, so stemming actually cuts the actual word and lemmatization actualy turns the word to its root form so lemmatization is a good option i think so.

# Q5: How do word embeddings like Word2Vec or GloVe work?
# ANS: Let me explain, In Old NLP techniques we convert the text into BOW, TF-IDF what it does is we are not actually getting words meaning so word embedding does is it gives us the words meaning so now come into its working, I think so we take the whole vocabulary from the corpus and then make a fake dataset in specific window size like 5 so it will take 4 words for X and 1 word for Y means dependent, independent features then we train a neural network with this and also I think so that neural network is not normal it I think so when the training of the specific independent feature row happens it takes embedding or OHE representation of each word and with this we got so many representation for each word and then we feed it all once to our single layer neural network and then its output goes to our output layer which consists of all vocabulary words count neurons so there we apply softmax and whatever words comes with maximum score its weights which are comming from neural network is consider as its Embedding.

# Q6: What are the steps in a full NLP pipeline?
# ANS: I think so it will be, Data Collecting, Data Preprocessing like stop word removal, lemmatization, lower case, then converts each row into its embedding using various embedding techniques, then now we have model ready to train data now we train our model with this data and also there is so many model like normal ML model, or DL model, or Sequential model if we want much better performance.

# Q7: What is Named Entity Recognition (NER)? How is it used?
# ANS: I think so it will be that we are assinging each word to its specific group like talha to name, Dubai to place.

# Q8: How do you evaluate the performance of an NLP model?
# ANS: I don't know, explain me.

# Q9: What are the limitations of traditional NLP methods (vs transformers)?
# ANS: Pretty interesting question, IN traditional NLP methods first of all before we are limited to normal models we are not able to learn patterns in our data sequentailly then sequential models comes but there is a problem occurs how can we do seq 2 seq tasks like giving sequence of words and predicting sequence of words this problem is solved by our transformer model now it will take sequence of words once and then generate sequence of words one by one.

# Q10: What are attention-based models and how did they change NLP?
# ANS: I have already explain it to you I will explain further in LLM Chapter.

# LLM Based questions

# Q1: What is a transformer architecture? Key components?
# ANS: Transformer architecture is a modern NLP model which use attention mechanism to train the seq 2 seq data, now let me tell you its key components, first of all our each words of a specific row while training converts into embedding then we add a positional encoding to each word embedding then we feed our vector to encoder block then we made 2 copy of each vector 1 will go for further process and 2 one will be go to add and normalize to 1 one output so we take the 1 one vector and make its query, key, value vector we do this for all words then we do is take each word query vector and dot product it with all words key vector then we got our score for all dot products then we scale each score and apply softmax to each value then now we got our attention score then we take each value vector of key vector which we dot product before now what we does is mulitply each value of the value vector with the specific attention score we do this for all vector now we add all of the value vector to one vector now we got a final representation of our query vector this whole process called self attention or scaled dot product attention now we do this for every query vector and now we send this output vector to normalize and now here we add the previous duplicate 2 vector now when everything get done now we do the same duplicate of the vector and send the first vector to our neural network when neural network output comes we again do the normalize thing and add the previous duplicate value we do this for every vector now there is our first step completes in encoder then I think so we do this whole encoder step 6 time then now our final vector comes from each words now we go to decoder part now in decoder we have ground truth row means what actually we have to predict we first train with the sentence in decoder we do all the embedding and posistional thing and now there is happening all thing with that ground truth words now there again comes multi head attention with masked let me mention you we do the vector thing in self attention for each word multiple times multi head, in there we actually masked means zero that vector attention score which has no relation to that query vector thats it means we are not giving any importance to that word it just dissapers now we also do the same normalize add thing and create multi head now all this thing go to again multi head self attention now here our query vector is decided but the key, and value vector is comming from encoder now we do all the things and again normalize and add it and then send it to neural network and again add and normalize it then we send it to our final nerual network from which we have vocabulary size neurons then we apply softmax and which ever word or neuron comes with most probabitly we will take it as our prediction and send compare with its orignal OHE and then send its groudn truth to next prediction I think so I explain it right

# Q2: How does self-attention work in LLMs?
# ANS: I have explained it to you already the whole transformer architecture.

# Q3: What is masked language modeling (MLM) and causal language modeling (CLM)?
# ANS: I don't know

# Q4: Difference between BERT and GPT architectures?
# ANS: I think so BERT is ENCODER based and GPT is DECODER based.

# Q5: What are prompt tokens, and how do LLMs interpret input prompts?
# ANS: They are for setting LLM limitations so mulitiple users will not use it too much, explain me.

# Q6: What is the role of position embeddings in transformers?
# ANS: Already Explained.

# Q7: What’s the difference between fine-tuning and prompt-engineering?
# ANS: So in propt-engineering we are using our LLM to its full potential with prompts already trained LLM remeber this thing, and in Fine Tuning we actually train some part of the model in our data I think so.

# Q8: How do you evaluate the performance of an LLM?
# ANS: I only know about BlEU.

# Q9: Explain how LangChain or similar frameworks allow LLM chaining or tool usage.
# ANS: In Langchain everything is runnable so when we use LLM noramally it is a runnable then when we use prompt template it is also a runnable so we combine LLM, Prompt and also OutputParser in a chain so now we have to invoke our chain to invoke all runnables, and in tool it is linked to agents what we are doing is giving tools to our LLM in which it will do our task by using that tools also.

# Q10: What are some limitations and risks of LLMs in real-world apps?
# ANS: It's vulgur and harmful knowledge if not control will make mess, explain more.

# Web Based Questions

# Q9. How would you build a full-stack app that takes a user-uploaded image and classifies it using your ML model?
# ANS: So simple, first of all we have to question that whate are we building, what is the input output, what the UI looks like, what tech are we using it, now comes to tech so basically we are using Machine Learning we have to collect too many data of images, preprocessed it, train our model on that data of images then we evaluate the model and improves its perfomance using all best practices, these all creates in components then we create a training pipeline from which all the components will initiate, then we create the frontend and then start building the backend we then also build a prediction pipeline from which we connect the backend and frontend via API then when the user sends an image from frontend to backend POST request then we fetches the image send it to prediction pipeline, pipeline will preprocessed the image sends to model for prediction and when the predictions comes we encode it with its categorie and then returns again to backend then show the response to frontend, then we also contarized the app and also deploy it on cloud, so simple