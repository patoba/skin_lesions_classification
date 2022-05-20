# skin_lesions_classification

# Instrucciones

## 1. Crear Ambiente

Ejecutar `crear_ambiente.sh` para crear un ambiente de python 3 que tendra todo lo necesario para trabajar.

```
skin_lesions_classification$ ./crear_ambiente.sh
```

En caso de que la instalacion por version falle, se encuentran los comandos `requirements_mano.sh` que facilita la instalacion

## 2. Descargar los datos

Descargar los datos de [https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T#](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T#) 

Una vez descargado ejecutar el script `descargar_datos.sh` para poder descomprimir y armar bien la estructura de carpetas

## 3. Acomodar las imagenes

Por temas de ImageFolder de pytorch hay que acomodar los datos de una forma especifica esto se logra mediante el programa `acomodar_imagenes.py` que se encuentra en `main.py`

## 4. Entrenamiento

Para entrenar basta con correr el `entrenamiento.py`. Por defecto se entrena en gpu, se puede observar las metricas mediante tensorboard mediante el comando: 

```
skin_lesions_classification$ tensorboard --logdir=logs/
```


# Extras

## Conexion ssh escuela 

```
ssh -p 2244 usuario01_lcd@132.248.51.117
```

password: `Alumno01$%1725`