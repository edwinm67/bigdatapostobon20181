# Universidad EAFIT
# Curso Big Data - Postobon, 2018-1
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co

## 0. CONECTARSE AL CLUSTER CLOUDERA:

### Desde la estación Cliente Windows desde Internet:

* Descargar putty.exe y colocar en el Escritorio.
* Ejecutar putty.exe
* Hostname o IP: 200.12.180.67
* login as: cectmp
* Password: ******

* Una vez contectado en el servidor 200.12.180.67, ejecute:

        cectmp@urania$ ssh postobon##@192.168.10.115
        Password: ******** (password asignado a cada usuario)

### Desde una estación Linux o Mac desde Internet:

* Abrir una terminal
      user@hostname$ ssh cectmp@200.12.180.67
      Passoword: ***** (password asignado a cectmp)

* Una vez contectado en el servidor 200.12.180.67, ejecute:

              cectmp@urania$ ssh postobon##@192.168.10.115
              Password: ******** (password asignado a cada usuario)

### Desde la estación Cliente Windows desde VPN:

      Host Name (or IP address):
      192.168.10.115

      Port: 22 (dejarlo asi):

      Click en "Open"

      login as: postobon##      (usuario asignado)
      password: ********        (password asignado)

### Desde una estación Linux o Mac desde VPN:

      $ ssh postobon##@192.168.10.115
      Password: ******** (password asignado)

### Por Web:

* Desde un browser: http://192.168.10.115:8888 (por la Intranet via VPN)
* Desde un browser: http://cloudera.dis.eafit.edu.co (por la Internet)


## 1. DATASETS

* [datasets](datasets)

## 2. SISTEMA DE ARCHIVOS HDFS

* [HDFS](01-hdfs)

## 3. PROCESAMIENTO - MAP/REDUCE

* [MapReduce](02-mapreduce)
