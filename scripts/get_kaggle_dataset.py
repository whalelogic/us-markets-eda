import kaggle 
import os

def download_kaggle_dataset(dataset_name, download_path):
    """
    Downloads a dataset from Kaggle.

    Parameters:
    dataset_name (str): The name of the dataset in the format 'username/dataset-name'.
    download_path (str): The local path where the dataset should be downloaded.
    """
    # Ensure the download path exists
    os.makedirs(download_path, exist_ok=True)
    
    # Download the dataset
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"Dataset '{dataset_name}' downloaded to '{download_path}'")


if __name__ == "__main__":
    # Example usage
    dataset_name = "zynicide/wine-reviews"  # Replace with your desired dataset
    download_path = "./data/wine-reviews"   # Replace with your desired download path
    download_kaggle_dataset(dataset_name, download_path)
