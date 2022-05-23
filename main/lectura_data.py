import pandas as pd

from sklearn.preprocessing import LabelEncoder

from constantes import main_dir

metadata = pd.read_csv(main_dir + '/datos/HAM10000_metadata')

le = LabelEncoder()
le.fit(metadata['dx'])
print("Classes:", list(le.classes_))
 
metadata['label'] = le.transform(metadata["dx"]) 
