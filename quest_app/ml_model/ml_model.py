import random
import joblib

# this is a wrapper for the classification model, WIP
# the input is a dictionary with answers
# the output is a number of predicted class
def dummy_model(ans_dict):
    ans_dict = ans_dict.copy()

    ans_dict.pop(list(ans_dict.keys())[0], None)  # remove the first element (csrfmiddlewaretoken)
    ans_dict.pop('15', None)  # pop the answers that don't take part in prediction
    ans_dict.pop('16', None)

    # data preprocessing
    ans_list = []
    for i in range(14):
        ans_list.append(0)
    for key in ans_dict.keys():
        ans_list[int(key) - 1] = int(ans_dict[key])

    # predict using the pretrained model defined elsewhere in this module
    # the input of the classification model is a list of answers to the questionnaire
    # the output is the number of the predicted class
    # class_num = predict(ans_list) or something

    # this is a placeholder
    #class_num = random.randint(1, 6)  # number of a class
    class_num = 1   
    return class_num


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
