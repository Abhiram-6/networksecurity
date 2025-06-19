from networksecurity.components.dataingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestion=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestion)
        logging.info("Enter the try block")
        dataingestiontartifact=data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)