from tkinter import E

from scipy.sparse import data
from housing.config.configuration import configuration
from housing.logger import logging
from housing.exception import HousingExceptions

from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.component.data_ingestion import DataIngestion

import sys , os

class Pipeline:
    def __init__(self,config:configuration=configuration()):
        try:
            self.config=config
        
        except Exception as e:
            raise HousingExceptions(e, sys) from e

    def start_data_ingestion(self):
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())

            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingExceptions (e,sys) from e


    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:  
            raise HousingExceptions(e, sys) from e                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          


