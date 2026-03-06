import requests
import pandas as pd
import csv
import time
from datetime import datetime, timedelta
from pathlib import Path

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

                    pd.DataFrame(request.json().get("data", [])).to_json(
                        f"dados/vagas/{label}.json", orient='index', indent=1, date_format='iso'
                    )

                    print(f"Found {len(response)} results for '{label}'...")
                    time.sleep(0.5)

                except Exception as e:
                    print(e)

        return responses
    
headers= {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)"
        }    

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


request_data(labels)

