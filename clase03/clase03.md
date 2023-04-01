## Clase 03

# Tipos de formatos para datos para comunicarnos en sistemas
    1.csv 
    2.json (evolucion del xml) => comunicacion web con api rest
    3.parquet => formato orientado a columnas para grandes volumenes de informacion
# python modulos pandas
        link ->https://pandas.pydata.org/docs/user_guide/index.html
        pandas nos permite leer o cargar un fuente y poder manipularlo para analizar o modificar la informacion
        cambiarlo de formato con los metodos de read_{format} y to_{format}
# repasar s3
    -como cargar datos al s3 => crear usuario , desde consola , desde un script python, desde la interfaz

# repoaso lambda
    -funciones en basse a eventos que me permiten dispararse luego de que se hace el evento(subir archivo de un s3 )
    nos muestra log(registros) , tambien lo podemos usar luego del outpu de un procesamiento

## AWS Glue
    data catalog
        servicio que centraliza los metadatos y/o schemas
        |id|name|mobil|email|
    centraliza informacion de varias fuentes

    crawler => nos permiten correr desde data sources para poblar y/o mapear nuestra data catalog
    job=> tarea en especifico respecto a un ambito de mi data source(base de datos ,s3,etc)
    workflow=>
## api

