import pandas as pd

def load_data():
    """
    Load the student academic performance dataset
    """
    file_path = "data/student_info.csv"
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    df = load_data()
    print("Dataset loaded successfully ✅")
    print("Shape of dataset:", df.shape)
    print("\nColumn Names:\n")
    for col in df.columns:
        print(col)
