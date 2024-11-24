from dataclasses import dataclass



@dataclass
class DataIngestionartifact:
    train_file_path:str
    test_file_path:str
    