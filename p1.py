import pandas as pd
import numpy as n
d=pd.DataFrame(
    {"date":pd.date_range(start="2023-0/9-07",periods=5,freq="b"),
    "temp":n.random.randint(18,36,size=5)}
)
d["f"]=d["temp"].shift(1)
print("shift:\n",d)
dfw=d.resample("M",on="data").mean()
print("\n resampling:\n",dfw)