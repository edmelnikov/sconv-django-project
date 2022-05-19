import joblib
import os

# Model class that loads up the model and predicts the trajectory number
class Model:
    '''
    model_path - path to the model, saved by joblib
    trans_pipe_path - path to the transformations pipeline object, applied to the input data, saved by joblib
    '''

    def __init__(self, model_path=None, trans_pipe_path=None):
        if model_path:
            self._model = joblib.load(model_path)

        if trans_pipe_path:
            self._trans_pipe = joblib.load(trans_pipe_path)

    def predict(self, X, transform=True):
        '''
        This method performs transformations to the input data (if transform=True)
        and predicts target value
        X - input data: list(list(int))
        '''
        if transform:
            X = self._trans_pipe.transform(X)

        prediction = self._model.predict(X)
        return prediction

    def load_model(self, path):
        self._model = joblib.load(path)

    def load_trans(self, path):
        self._trans_pipe = joblib.load(path)


# This is a wrapper function for the classification model class
# the input is a dictionary with 14 answers
# the output is a number of a predicted class from 1 to 6
def predict_trajectory(ans_dict, verbose=False):
    # preprocess data
    ans_dict = ans_dict.copy()
    ans_dict.pop(list(ans_dict.keys())[0], None)  # remove the first element (csrfmiddlewaretoken)
    ans_dict.pop('15', None)  # pop the answers that don't take part in prediction
    ans_dict.pop('16', None)

    # convert into the list
    ans_list = []
    for i in range(14):
        ans_list.append(0)
    for key in ans_dict.keys():
        ans_list[int(key) - 1] = int(ans_dict[key])

    # predict
    model = Model(model_path=os.path.join(os.path.dirname(__file__), 'classifier/model.joblib'),
                  trans_pipe_path=os.path.join(os.path.dirname(__file__), 'classifier/pipe_transforms.joblib'))
    class_num = model.predict([ans_list])[0]

    if verbose:
        print(f"--- Answer list: {ans_list}")
        print(f"--- Predicted trajectory number: {class_num}")

    return class_num


