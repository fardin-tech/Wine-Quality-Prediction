from mlproject.config.configuration import ConfigurationManger
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger


STAGE_NAME="Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManger()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer_config=ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()