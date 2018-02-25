# Universidad EAFIT
# Curso Big Data - Postobon, 2018-1
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co

## 1. CONECTARSE AL CLUSTER CLOUDERA:

### Conectarse a la VPN

### Desde la estación Cliente Windows desde Internet:

* Descargar putty.exe y colocarlo en el Escritorio.
* Ejecutar putty.exe

      Host Name (or IP address):
      192.168.10.115

      Port: 22 (dejarlo asi):

      Click en "Open"

      login as: postobon##      (usuario asignado)
      password: ********        (password asignado)

### Desde una estación Linux o Mac desde Internet:

* Abrir una terminal
      user@hostname$ ssh postobon##@192.168.10.115
      Passoword: ***** (password asignado a cada usuario)

### Por Web:

* Desde un browser: http://192.168.10.115:8888 (por la Intranet via VPN)
* Desde un browser: http://cloudera.dis.eafit.edu.co (por la Internet)


## 2. DATASETS

* [datasets](datasets)

## 3. SISTEMA DE ARCHIVOS HDFS

* [HDFS](01-hdfs)

## 4. PROCESAMIENTO - MAP/REDUCE

* [MapReduce](02-mapreduce)
