#Creacion del repositorio JSON

import json
import os
from typing import List, Dict
class JSONRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path
        folder = os.path.dirname(self.file_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)