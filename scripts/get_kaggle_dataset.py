import kaggle 
import os

def download_kaggle_dataset(dataset_name, download_path):
    """
    Downloads a dataset from Kaggle.

    Parameters:
    dataset_name (str): The name of the dataset in the format 'username/dataset-name'.
    download_path (str): The local path where the dataset should be downloaded.
    """
    os.makedirs(download_path, exist_ok=True)
    
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"Dataset '{dataset_name}' downloaded to '{download_path}'")


if __name__ == "__main__":
    dataset_name = "zynicide/wine-reviews"  # Replace 
    download_path = "./data/wine-reviews"   # Replace 
    download_kaggle_dataset(dataset_name, download_path)
