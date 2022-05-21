#!/bin/bash

mkdir ./datos

wget "https://dvn-cloud.s3.amazonaws.com/10.7910/DVN/DBW86T/163c862634d-663b42fb343d?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27HAM10000_images_part_1.zip&response-content-type=application%2Fzip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220521T194701Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=AKIAIEJ3NV7UYCSRJC7A%2F20220521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=f8265b98bcbb9928db8d641fd4ab49b2afcc672849eb53e04d4754a2615423af" -O ./datos/HAM10000_images_part_1.zip
wget "https://dvn-cloud.s3.amazonaws.com/10.7910/DVN/DBW86T/163c85dbd0a-b565e4ed4c74?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27HAM10000_images_part_2.zip&response-content-type=application%2Fzip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220521T194721Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=AKIAIEJ3NV7UYCSRJC7A%2F20220521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=034a3abdc43d5a0b4f780c6bcc6142f7fdf31e17b3560fe304b7d5bfb3bdb67a" -O ./datos/HAM10000_images_part_2.zip
wget "https://dvn-cloud.s3.amazonaws.com/10.7910/DVN/DBW86T/1726f776ebd-8bda2eac79bc?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27ISIC2018_Task3_Test_Images.zip&response-content-type=application%2Fzip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220521T194820Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=AKIAIEJ3NV7UYCSRJC7A%2F20220521%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=bbd0010ff90c76d8f224ab64cc71f8ed67e052b3fb15901b6b622501462b450b" -O ./datos/ISIC2018_Task3_Test_Images.zip

unzip -q ./datos/HAM10000_images_part_1.zip -d ./datos/imagenes_train
unzip -q ./datos/HAM10000_images_part_2.zip -d ./datos/imagenes_train
unzip -q ./datos/ISIC2018_Task3_Test_Images.zip -d ./datos/imagenes_test

rm -r ./datos/imagenes_test/__MACOSX
mv ./datos/imagenes_test/ISIC2018_Task3_Test_Images/* ./datos/imagenes_test 
rm -r ./datos/imagenes_test/ISIC2018_Task3_Test_Images

rm ./datos/HAM10000_images_part_1.zip  ./datos/HAM10000_images_part_2.zip ./datos/ISIC2018_Task3_Test_Images.zip

mkdir ./datos/imagenes_train_mod
