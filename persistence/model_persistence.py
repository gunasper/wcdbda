import joblib

class ModelPersistence():
    MODEL_FOLDER = 'persistence/models/'
    MODEL_NAME = 'cls.pkl'

    @staticmethod
    def read_model():
        """
            Reads the model wherever it is
        """
        my_classifier = None
        classifier_file =  ModelPersistence.MODEL_FOLDER + ModelPersistence.MODEL_NAME
        #####
        #
        #   Your code here!
        #
        #####
        return my_classifier
