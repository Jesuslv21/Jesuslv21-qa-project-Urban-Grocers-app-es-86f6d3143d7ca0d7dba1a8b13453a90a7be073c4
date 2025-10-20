# Proyecto Urban Grocers 
Proyecto Spint 7  Urban Grocers (Introduccion a automatización de pruebas)

Descripcion del proyecto:

Este proyecto tiene como finalidad testear el nombre de usuario, en el proceso de creacion de kits para enviar productos alimenticios mediante solicitudes POST siguiendo el protocolo HTTP.

Instalacion de librerias:

Requerimos de las librerias requests y pytest para poder desarrollar correctamente nuestro proyecto.


Organizacion del proyecto y observaciones:

Al crear los archivos se debe tener en cuenta las urls y endpoints en el archivo configuracion.py encontrados en el archivo de documentos API

Las solicitudes POST se realizar en el sender_stand_request.py

los cuerpos de las API se crean en data.gy 

en el archivo create_kit_name_kit_test.py se crean las funciones possitive y negative assert, y una que modifica el json del kit_body

para poder ejecutar las distintas pruebas, tambien se guarda el authToken en el header como valor de la clave authorization

se escriben las respecivas pruebas usando la funcion correspondiente (si es negativa o positiva)

al final 5 tests pasaron las pruebas y otros 4 permitian crear los kits asi no fueran validos

Ejecucion de las pruebas mediante la herramienta pytest:

Se abre la ventana terminal en el IDE PyCharm, haciendo click en la esquina inferior izquierda, en el icono de una ventana con un signo mayor y una barra al piso

Luego aparece la direccion donde esta guardado el proyecto, se procede a ejecutar el comando pytest seguido del nombre del archivo del proyecto

Es importante que el nombre del archivo de los pruebas contenga la palabra test en el. En el caso de este proyecto el archivo se llama create_kit_name_kit_test.py

por lo que se escribe en el shell: pytest create_kit_name_kit_test.py y se ejecutaran todas las funciones que tengas test dentro de su nombre.

pytest