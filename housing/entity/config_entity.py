from collections import namedtuple
from unicodedata import name

DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


DataValidationConfig=namedtuple("DataValidationConfig",["schema_file_path"])


DataTransformationConfig=namedtuple("DtaTransformationConfig", ["add_bedroom_per_room",
                                                              "transforme_train_dir",
                                                              "transformed_test_dir",
                                                              "preprocessd_object_file_path"])


ModelTrainerConfig=namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig=namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

ModePusherConfig=namedtuple("ModePusherConfig",["export_dir_path"])

TrainingPipelineConfig=namedtuple("TrainingPipelineConfig",["artifact_dir"])