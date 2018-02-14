# Universidad EAFIT
# Curso Big Data - Postobon, 2018-1
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co

# Laboratorio HDFS

## 1. cluster Hadoop

IP: 192.168.10.80

User/pass del DCA

Ambari: http://192.168.10.80:8080
Web: http://<name>.dis.eafit.edu.co

Monitoreo del cluster hadoop: http://192.168.10.80:8088

## 2. Gestión de archivos en HDFS

Obtener un subconjunto de datos de prueba, de Gutenberg Digital Library

Puede descargar datos directamente del sitio:

Comando:

    user@master$ wget -w 2 -m -H "http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=es"


asi, los descarga en formato .zip, uds los deben descomprimir antes de enviarlos al HDFS

Puede utilizar datos previamente descargados:
[Gutenberg-dataset-txt-es](datasets/gutenberg-txt-es.zip)

## 3. Listar archivos HDFS

Para efectos de esta guia, es equivalente el comando "hadoop fs" y "hdfs dfs". La diferencia es que "hdfs dfs" es solo para sistemas de archivos HDFS, pero "hadoop fs" soporta otros adicionales como S3.

    user@master$ hdfs dfs -ls /
    user@master$ hdfs dfs -ls /user
    user@master$ hdfs dfs -ls /datasets

## 4. Crear tu propio directorio de usuario en HDFS (debe hacerse con el usuario hdfs para crear el /user/<username>)

    user@master$ sudo su – hdfs
    user@master$ hadoop fs -mkdir /user/<username>
    user@master$ hadoop fs -chown <username> /user/<username>

ej:

    user@master$ hadoop fs -mkdir /user/emontoya
    user@master$ hadoop fs -chown emontoya /user/emontoya



    user@master$ hdfs dfs -mkdir /user/<username>
    user@master$ hdfs dfs -mkdir /user/<username>/datasets
    user@master$ hdfs dfs -mkdir /user/<username>/datasets/gutenberg-txt-es

reemplace “<username>” por su usuario en el DCA

## 5. Copiar archivos locales hacia HDFS

Se asume que tiene los datos LOCALES de gutenberg en: /datasets/gutenberg-txt-es o donde los haya descargado.

    user@master$ hdfs dfs -copyFromLocal /datasets/gutenberg-txt-es/*.txt /user/<username>/datasets/gutenberg-txt-es

otro comando para copiar:

    user@master$ hdfs dfs -put /datasets/gutenberg-txt-es/*.txt /user/<username>/datasets/gutenberg-txt-es

    user@master$ hdfs dfs -ls /user/<username>/datasets

## 6. Copiar archivos de HDFS hacia local

    user@master$ hdfs dfs -copyToLocal /user/<username>/data_out1/* ~<username>/data_out1

otro comando para traer:

    user@master$ hdfs dfs -get /user/<username>/data_out1/* ~<username>/data_out1

    user@master$ ls -l data_out1

## 7. Probar otros commandos

Se aplica los siguientes comandos a:

    user@master$ hdfs dfs -<command>

comandos:

    du <path>             uso de disco en bytes
    mv <src> <dest>       mover archive(s)
    cp <src> <dest>       copiar archivo(s)
    rm <path>             borrar archive(s)
    put <localSrc> <dest-hdfs> copiar local a hdfs
    cat <file-name>       mostrar contenido de archivo
    chmod [-R] mode       cambiar los permisos de un archivo
    chown …               cambiar el dueño de un archivo
    chgrp                 cambiar el grupo de un archivo

## 9. Realice todas las operaciones de:

    * creación de directorios
    * copiado de archivos
    * borrado de archivos
    * cambio de permisos
    * descarga de archivos.
    * etc

    Via la interfaz web de Ambari: Files View

## 8. RETO:

Copiar el resto de datasets para el curso, en:

    /user/<username>/datasets
