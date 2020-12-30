# Data Science / Machine Learning 
import numpy as np
from sklearn.metrics import accuracy_score,mean_squared_error

def standardize(X):

    """ Standardize Input Data """
    
    for c in X.columns:
        X[c] = (X[c] - X[c].mean()) / X[c].std()
    return(X)

class Linear_Regression(object):
    
    """Linear Regression
    
    Keyword arguments:
    eta -- Learning rate (between 0.0 and 1.0)
    n_iter -- Number of passes over the training set
    """
    
    def __init__(self,lr,iterations=1):
        
        self.learning_rate = lr
        self.iters = iterations
        
    def add_bias(self,X):
        
        """ Bias Vector Initialized at Zero with X Features"""        
        return(np.hstack([np.ones((X.shape[0],1)),X]))

    def predict_prob(self,X,alpha=0.50,add_bias=True):
        
        """ Predicted Class Label"""
    
        Xb = self.add_bias(X) if add_bias else X
        return(np.dot(Xb,self.weights))
        
    def gradient(self,X,y):
        
        """Compute Gradient"""
        gradient = np.ones(self.weights.shape)
        for x_i,y_i in zip(X,y):
            g = (y_i - self.predict_prob(x_i,add_bias=False))*x_i
            gradient += g.reshape(self.weights.shape)
        return(gradient/float(len(y)))

    def fit(self,X,y):
        
        """Fit Model to Training Set"""
        
        print('Original Data Shape: ',X.shape)
        
        #Initialize Weights
        X_bias = self.add_bias(X)
        
        num_obs, num_feats = X_bias.shape
        print('Data with Bias Term: ',X_bias.shape)
        
        #Weights
        self.weights = np.zeros((num_feats,1))
        print('Weight Vector Shape: ',self.weights.shape)
    
        #Iterate and Update Weights
        for i in range(self.iters):

            #Compute Gradient
            gradient = self.gradient(X_bias,y)
            
            #Update Weights
            self.weights += gradient*self.learning_rate
            
            
class Logistic_Regression(object):
    
    """Logistic Regression
    
    Keyword arguments:
    eta -- Learning rate (between 0.0 and 1.0)
    n_iter -- Number of passes over the training set
    """
    
    def __init__(self,lr,iterations):
        
        self.learning_rate = lr
        self.iters = iterations

    def sigmoid(self,z):
        
        """ Logistic Sigmoid Function """
        sigmoid = 1 / (1+np.exp(-z))
        return(sigmoid)
    
    def activation(self,X):
        
        """Activation of Logistic Neuron -- Returns Scalar Value"""
        z = np.dot(X,self.weights)
        return(self.sigmoid(z))
    
    def add_bias(self,X):
        
        """ Bias Vector Initialized at Zero with X Features"""        
        return(np.hstack([np.ones((X.shape[0],1)),X]))

    def predict_prob(self,X,alpha=0.50,add_bias=True):
        
        """ Predicted Class Label"""
    
        Xb = self.add_bias(X) if add_bias else X
        pred = np.where(self.activation(Xb) >= alpha,1,0)
        return(pred)
        
    def gradient(self,X,y):
        
        """Compute Gradient"""
        gradient = np.ones(self.weights.shape)
        for x_i,y_i in zip(X,y):
            g = (y_i - self.predict_prob(x_i,add_bias=False))*x_i
            gradient += g.reshape(self.weights.shape)
        
        return(gradient/float(len(y)))

    def fit(self,X,y):
        
        """Fit Model to Training Set"""
        
        print('Original Data Shape: ',X.shape)
        
        #Initialize Weights
        X_bias = self.add_bias(X)
        
        num_obs, num_feats = X_bias.shape
        print('Data with Bias Term: ',X_bias.shape)
        
        #Weights
        self.weights = np.zeros((num_feats,1))
        print('Weight Vector Shape: ',self.weights.shape)
    
        #Iterate and Update Weights
        for i in range(self.iters):

            #Compute Gradient
            gradient = self.gradient(X_bias,y)
            
            #Update Weights
            self.weights += gradient*self.learning_rate
            
def SVD(X):

    print ('=================  SVD  =================')
    
    #Compute AA^T and A^TA Matrices
    try:
        AA_T = np.dot(X,np.transpose(X)) 
        AT_A = np.dot(np.transpose(X),X) 
    
    except:
        print("Unexpected Error:", sys.exc_info()[0])

    #Compute U,S,V.T
    try:
        U = np.linalg.eig(AA_T)[1] #Eigenvectors of XX.T
        S = np.sqrt(np.linalg.eigvals(AT_A)) #Singular Values
        VT = np.linalg.eig(AT_A)[1].T #Eigenvectors of X.TX
    except:
        print("Unexpected Error:", sys.exc_info()[0])
      
    
    #Explained Variance Ratio
    S_ratio = [(i+1,s/np.sum(S)) for i,s in enumerate(sorted(S,reverse=True))]
    for i in S_ratio:
        print('{0:.0f} Component --  Variance Explained {1:.3f}'.format(i[0],i[1]))

    return(U,np.diag(S),VT)