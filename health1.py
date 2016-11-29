import requests
import pandas as pd

addr=
resp = requests.get(addr)
j = resp.json()
df = pd.DataFrame(j["data"], columns = j["keys"])
writer = pd.ExcelWriter('ALGO.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()

import requests
import pandas as pd

addr="https://vizhub.healthdata.org/gbd-compare/api/metadata"
resp = requests.get(addr)
j = resp.json()
df = pd.DataFrame(j["data"]["cause"])
writer = pd.ExcelWriter('ALGO.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
