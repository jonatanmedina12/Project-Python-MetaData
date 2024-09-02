from src.controller.metadata_controller import extract_metadata

if __name__=="__main__":
    file_path=""
    metadata = extract_metadata(file_path)
    for key,value in metadata.items():
        print(f"{key}:{value}")
