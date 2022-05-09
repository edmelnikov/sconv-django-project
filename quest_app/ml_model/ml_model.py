import random


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
