from datetime import datetime
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
        my_classifier = joblib.load(classifier_file)
        return my_classifier

    def get_model_update_date():
        """
            Returns when the model was last updated
        """
        return datetime.now()