import os

def get_data_path():
    data_path = os.path.join(os.path.dirname(__file__), "..","data")
    os.makedirs(data_path, exist_ok=True)
    return os.path.abspath(data_path)

def get_model_path():
    model_path = os.path.join(os.path.dirname(__file__), "..", "models")
    os.makedirs(model_path, exist_ok=True)  # Create the directory if it doesn't exist
    return os.path.abspath(model_path)

def get_temp_path():
    temp_path = os.path.join(os.path.dirname(__file__), "..", "temp")
    os.makedirs(temp_path, exist_ok=True)
    return os.path.abspath(temp_path)

def main():
    for name, func in [
        ("Data Path", get_data_path),
        ("Model Path", get_model_path),
        ("Temp Path", get_temp_path),
    ]:
        print(f"{name}: {func()}")
if __name__ == "__main__":
    main()