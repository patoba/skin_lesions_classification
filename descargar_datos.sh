#!/bin/bash

mkdir -p datos

unzip ./datos/dataverse_files.zip -d ./datos
rm ./datos/dataverse_files.zip

unzip ./datos/HAM10000_images_part_1.zip -d ./datos/imagenes_train
unzip ./datos/HAM10000_images_part_2.zip -d ./datos/imagenes_train
unzip ./datos/ISIC2018_Task3_Test_Images.zip -d ./datos/imagenes_test

rm -r ./datos/imagenes_test/__MACOSX
mv ./datos/imagenes_test/ISIC2018_Task3_Test_Images/* ./datos/imagenes_test 
rm -r ./datos/imagenes_test/ISIC2018_Task3_Test_Images

rm ./datos/HAM10000_images_part_1.zip  ./datos/HAM10000_images_part_2.zip ./datos/ISIC2018_Task3_Test_Images.zip

mkdir ./datos/imagenes_train_mod