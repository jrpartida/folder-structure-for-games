import os
import constants
class App:

    def __init__(self, root_dir):
        self.root_dir = root_dir
    
    @staticmethod
    def create_new_folder(folder_name):
        if os.path.isdir(folder_name):
            print("Folder " + folder_name + "already exists")
            return False
        
        os.mkdir(folder_name)
        print ("Folder " + folder_name + " created")
        return True


    def create_folder_structure(self):
        self.create_new_folder(self.root_dir)
