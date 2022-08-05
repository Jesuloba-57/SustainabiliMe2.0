import requests
import json
from requests.structures import CaseInsensitiveDict

url = "https://beta3.api.climatiq.io/estimate"
api_key = "VYX67N66QHMRXHQTGGSACG8J3E9D"

headers = {"Authorization": "Bearer "+api_key}
#headers["Authorization"] = "Bearer VYX67N66QHMRXHQTGGSACG8J3E9D"

data = """
{
      "emission_factor": {
        "activity_id": "electricity-energy_source_grid_mix_residual_mix_market_based",
        "region": "GB"
       },
      "parameters": {
        "energy": 100,
        "energy_unit": "kWh"
      }
  }
"""


resp = requests.post(url, headers=headers, data=data)
resp = resp.json()
print(resp)


