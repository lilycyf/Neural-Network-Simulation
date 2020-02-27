
# --------------x1  x2 x3 x4 x5 d
training_set1 = [1, 1, 1, 1, 1, 1,
                 1, 1, 0, 1, 1, 1,
                 1, 0, 1, 1, 1, 1,
                 0, 1, 1, 1, 1, 1,
                 1, 0, 1, 0, 1, 1,
                 0, 0, 1, 1, 1, 1,
                 0, 1, 0, 1, 1, 1,
                 1, 0, 0, 1, 1, 1,
                 1, 1, 0, 0, 1, 1,
                 1, 1, 1, 0, 0, 1,
                 0, 1, 1, 0, 1, 1,
                 0, 0, 0, 0, 0, 0,
                 0, 0, 1, 0, 1, 0,
                 0, 1, 0, 0, 1, 0,
                 1, 0, 0, 0, 1, 0,
                 0, 0, 0, 1, 0, 0,
                 1, 0, 0, 0, 1, 0,
                 1, 1, 0, 0, 0, 0,
                 0, 1, 1, 0, 0, 0, 
                 0, 0, 1, 1, 0, 0,
                 0, 0, 0, 1, 1, 0];                           

# ~~~ Use these varibles in the learning portion of the Perceptron 

x_0 = 1.0 #value of input 0 of the perceptron; it's the bias
x_1 = 0.0 #hold actual value of input 1 of the perceptron
x_2 = 0.0 #hold actual value of input 2 of the perceptron
x_3 = 0.0 #hold actual value of input 3 of the perceptron
x_4 = 0.0 #hold actual value of input 4 of the perceptron
x_5 = 0.0 #hold actual value of input 5 of the perceptron


d = 0.0 #hold actual desired output
y = 0.0 #hold the actual dot product of training sample

w_0 = 0.0 #holds actual weight of input 0
w_1 = 0.0 #hold actual weight of input 1
w_2 = 0.0 #hold actual weight of input 2
w_3 = 0.0 #hold actual weight of input 3
w_4 = 0.0 #hold actual weight of input 4
w_5 = 0.0 #hold actual weight of input 5


f_x = 0         #binary output of the perceptron
threshold = 0.5 #deside when the perceptron 'fires'
alpha = 0.1     #learning parameter where 0<α≤1
error = 0       #hold actual error of the training sample
error_sum = 5.0 #hold the error sum of the training set
counter = 0     #counter for training samples
t = 0           #auxiliary variable 

# ~~~ These are for the Testing portion

X_1 = 0.0 #hold actual value of input 1 of the perceptron for application
X_2 = 0.0 #hold actual value of input 2 of the perceptron for application
X_3 = 0.0 #hold actual value of input 3 of the perceptron for application
X_4 = 0.0 #hold actual value of input 4 of the perceptron for application
X_5 = 0.0 #hold actual value of input 5 of the perceptron for application

Y = 0.0 #hold dot product with final weights




def learn(trainingData, inputSize, bias, threshold, alpha):

    total_cycles = 20 
    current_cycle = 0
    data_sets = int(len(trainingData)/(inputSize+1))


    t=0 #auxiliary variable 

    while current_cycle < total_cycles:
        error_sum=0.0 #reset error sum
        for j in range(data_sets):
            x_1 = trainingData[t]                    
            x_2 = trainingData[t+1]  
            x_3 = trainingData[t+2]
            x_4 = trainingData[t+3]
            x_5 = trainingData[t+4]
            d = trainingData[t+5]  
            t = t + inputSize + 1
        
            global w_0, w_1, w_2, w_3, w_4, w_5
            y = x_0 * w_0 + x_1 * w_1 + x_2 * w_2 + x_3 * w_3 + x_4 * w_4 + x_5 * w_5


                    
            if y > threshold:
                f_x = 1
            else:
                f_x = 0
                
                    
            error = d - f_x

            error_sum = error_sum + abs(error)

            #Change the weights of the hidden layer
        
            w_0= w_0 + alpha * x_0 * error
            w_1= w_1 + alpha * x_1 * error            
            w_2= w_2 + alpha * x_2 * error
            w_3= w_3 + alpha * x_3 * error
            w_4= w_4 + alpha * x_4 * error
            w_5= w_5 + alpha * x_5 * error
        
        
        
        current_cycle = current_cycle + 1
        t = 0

        print(f"Cycle: {current_cycle}")
        print(f"Error Sum = {error_sum}")
        print(" ")

    print("Learning progress finished!")

    print(f"y = {w_0}x_0 + {w_1}x_1 + {w_2}x_2 + {w_3}x_3 + {w_4}x_4 + {w_5}x_5")



def test(X_1, X_2, X_3, X_4, X_5): 

    Y = x_0 * w_0 + X_1 * w_1 + X_2 * w_2 + X_3 * w_3 + X_4 * w_4 + X_5 * w_5
    
    
    if ( Y > threshold ):
        f_x = 1
    else:
        f_x = 0
    
    print(Y)
    print(f"The desired output is: {f_x}")


learn(training_set1, 5, w_0, threshold, alpha)

test(0,0,0,0,0)

test(0,1,1,0,1)
