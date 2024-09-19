from contextlib import closing
from urllib.request import urlopen

import json
import pandas as pd

with closing(
        urlopen('https://api.meteo-concept.com/api/observations/around?token=1391206501d87f244536af086fddf6fb3849fe0bd325991cb4b477f23dee4aa2&insee=75101')) as f:
    decoded = json.loads(f.read())

data = pd.json_normalize(decoded)
print(data)