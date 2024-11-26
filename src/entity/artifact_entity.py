from dataclasses import dataclass



@dataclass
class DataIngestionartifact:
    train_file_path:str
    test_file_path:str
    

@dataclass
class DataValidationartifact:
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str




@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str