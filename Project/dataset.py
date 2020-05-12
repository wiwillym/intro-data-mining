import pandas as pd
import numpy as np

# Usando pandas, se importa el Dataset
df = pd.read_csv("usableCommentsFull.csv",
                 names = ["text", "subreddit", "meta", "time", "author",
                          "ups", "downs", "authorlinkkarma", "authorcommentkarma", "authorisgold"])

# la cuarta columna contiene los tiempos en formato UNIX, para obtener minimo y máximo hacemos lo siguiente:

 time = df.iloc[:,3]
 mintime = time.min()
 maxtime = time.max()