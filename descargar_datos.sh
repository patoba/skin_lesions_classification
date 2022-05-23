#!/bin/bash

mkdir ./datos
mkdir ./download

curl -L -J -H "X-Dataverse-key:$DATAVERSE_API_TOKEN" https://dataverse.harvard.edu/api/access/dataset/:persistentId/?persistentId=doi:10.7910/DVN/DBW86T --output ./download/dataverse_files.zip
            
unzip -q ./download/dataverse_files.zip -d ./download

unzip -q ./download/HAM10000_images_part_1.zip -d ./datos/imagenes_train
unzip -q ./download/HAM10000_images_part_2.zip -d ./datos/imagenes_train
unzip -q ./download/ISIC2018_Task3_Test_Images.zip -d ./datos/imagenes_test

mv ./download/HAM10000_metadata ./datos

rm -r ./datos/imagenes_test/__MACOSX
mv ./datos/imagenes_test/ISIC2018_Task3_Test_Images/* ./datos/imagenes_test 
rm -r ./datos/imagenes_test/ISIC2018_Task3_Test_Images

rm -r ./download

mkdir ./datos/imagenes_train_mod
