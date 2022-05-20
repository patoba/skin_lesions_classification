import pandas as pd

from sklearn.preprocessing import LabelEncoder

from constantes import main_dir

metadata = pd.read_csv(main_dir + '/HAM10000_metadata.tab', delimiter="\t",
                        names = ["lesion_id", "image_id", "dx", "dx_type",
                        "age", "sex", "localization", "label"])

le = LabelEncoder()
le.fit(metadata['dx'])
print("Classes:", list(le.classes_))
 
metadata['label'] = le.transform(metadata["dx"]) 
