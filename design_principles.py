import os

class FilePath:
    def __init__(self, product_id):
        self.file_path = f"products/{product_id}.txt"

    def file_path(self):
        return self.file_path

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path


    def read_file(self):
        try:
            file = open(self.file_path.file_path, "r")
            data = file.read()
            file.close()
            return data
        except FileNotFoundError:
            print("File not found")
        
        
    def write_file(self, data):
        try:
            file = open(self.file_path.file_path, "w")
            file.write(data)
            file.close()
        except IOError as e:
            print(e)


    def delete_file(self):
        try:
            os.remove(self.file_path.file_path)
        except FileNotFoundError:
            print("File not found")

class FileReader:
    def __init__(self, file_manager, file_path):
        self.file_manager = file_manager
        self.file_path = file_path

    def get_product_info(self):
        return self.file_manager.read_file()
    
class FileWriter:
    def __init__(self, file_manager, file_path):
        self.file_manager = file_manager
        self.file_path = file_path

    def save_product_info(self, data):
        self.file_manager.write_file(data)



# Example usage
product_id = "P12345"
file_path = FilePath(product_id)
file_manager = FileManager(file_path)

# 

file_reader = FileReader(file_manager, file_path)
product_info = file_reader.get_product_info()
print("Product information:", product_info)

file_writer = FileWriter(file_manager, file_path)
new_data = "This is some updated product information."
file_writer.save_product_info(new_data)

file_manager.delete_file()
print("Product information deleted.")
