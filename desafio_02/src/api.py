import time
import pandas as pd
import yaml
import requests


with open('configs/dev.yaml') as f:
    config = yaml.safe_load(f)
    
RAW_PATH = config['paths']['vagas']
URL = config['api']['api_path']
LABELS = config['api']['api_labels']

def request_data(labels):
        print(labels)
        responses = []

        with requests.Session() as session:
            for label in labels:
                print(f"Requesting for '{label}'...")
                url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

                try:
                    request = session.get(url, headers=headers)
                    response = request.json().get("data", [])
                    responses.append(response)
                    
        return responses
    
labels = [
    "analista",
    "dados",
    "python",
    "data",
    "Desenvolvedor",
    "Dev",
    "Front-end",
    "Back-end",
    "Full Stack",
    "FullStack",
    "Software",
    "DevOps",
    "Business Intelligence",
    "Machine Learning",
    "Inteligência Artificial",
]


