import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def create_model():
    # Import Data
    coordinate_data = pd.read_csv('room_data.csv')

    # Split Data
    X = coordinate_data.drop(columns=['HIT']) # !! NEEDS to be 2D array apparently
    y = coordinate_data['HIT']

    # To test for accuracy, general rule allocate 80% of data for training, 20% for testing
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

    # Create Model using Decision Tree Algorithim
    model = DecisionTreeClassifier()

    # Train Model
    model.fit(x_train.values, y_train.values)
    
    return model, y.values

def predict_model(model, coord, hit_data):    
    # Make Predictions
    predictions = model.predict([ [ coord[0], coord[1] ] ])
    
    '''
    # Evaluate Model
    accuracy = accuracy_score(hit_data, predictions)
    '''
    return predictions
