from networksecurity.components.dataingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig,DataValidationConfig

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestion=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestion)
        logging.info("Enter the try block")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion is completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("initate data validation")
        data_validation_artifact=data_validation.initate_data_validation()
        logging.info("data validation is completed")
        print(data_validation_artifact)
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)