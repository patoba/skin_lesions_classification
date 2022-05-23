import os
import shutil

from constantes import data_dir, dest_dir
from lectura_data import metadata

label = metadata["label"].unique()

for i in label:
    os.mkdir(dest_dir + "/" + str(i))
    imagenes = metadata.loc[metadata['label'] == i, 'image_id']
    for id in imagenes:
        shutil.copyfile((data_dir + "/" + id + ".jpg"), 
                        (dest_dir + "/" + str(i) + "/" + id + ".jpg"))
