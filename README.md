# Product Catalog

Una aplicación Django para el catálogo de productos y autenticación de usuarios.

## Características:

- Autenticación basada en tokens con `djangorestframework-simplejwt`.
- Documentación API con `drf-yasg`.
- Modelos de `Product`, `User`, y `ProductView`.
- CRUD completo para productos y usuarios.
- Análisis de vistas de productos.

## Instalación:

1. Clona el repositorio.
2. Crea un virtualenv y actívalo.
3. Instala las dependencias con `pip install -r requirements.txt`.
4. Ejecuta las migraciones con `python manage.py migrate`.
5. Para crear un superusuario, ejecute `python manage.py createsuperuser` y siga las instrucciones en pantalla.
6. Ejecuta el servidor de desarrollo con `python manage.py runserver`.

## Uso:

- Accede a `/admin/` para la administración de Django usando las credenciales del superusuario.
- Para explorar y probar los endpoints de la API, visita `/swagger/`.

## Endpoints:

- `/api/login/`: Endpoint para autenticar usuarios.
- `/api/products/`: Endpoint para listar y crear productos.
- `/api/products/<int:id>/`: Endpoint para detalles, actualizar y eliminar un producto específico.
- `/api/users/`: Endpoint para listar y crear usuarios.
- `/api/users/<int:id>/`: Endpoint para detalles, actualizar y eliminar un usuario específico.
- `/api/product-analytics/`: Endpoint para visualizar estadísticas de los productos más visitados. Esta funcionalidad está diseñada para extenderse hacia análisis detallado del comportamiento del cliente con respecto a los productos.

## Product Analytics:

El endpoint `/api/product-analytics/` fue creado para monitorear los productos más visitados y tiene el objetivo de extender funcionalidades a análisis de producto y tipo de cliente. Esto proporciona una visión detallada de qué productos atraen más atención y puede informar decisiones sobre promociones, inventario y estrategias de marketing.

## Tipos de Usuarios y Notificaciones:

Dentro del sistema, se manejan al menos dos tipos de usuarios:

- **Admins:** Los administradores tienen el poder de crear, actualizar y eliminar productos. Además, pueden crear, actualizar y eliminar otros usuarios administradores.
  
- **Usuarios Anónimos:** Estos usuarios solamente pueden obtener información de los productos, pero no tienen permisos para realizar cambios en el sistema.

### Notificaciones para Administradores:

Como requerimiento especial, cada vez que un usuario administrador realice un cambio en un producto (por ejemplo, si ajusta un precio), es esencial notificar a todos los otros administradores sobre dicho cambio. Actualmente, esta notificación se realiza a través de correo electrónico, pero se está considerando la inclusión de otros mecanismos en futuras iteraciones.

Para que las notificaciones funcionen adecuadamente, es esencial tener configurado el servidor SMTP y seguir las instrucciones mencionadas en la sección de [Notificaciones por Correo](#notificaciones-por-correo) de este documento.

## Pruebas:

El proyecto incluye tests escritos usando `pytest` y `pytest-django`. Estos tests garantizan que las funcionalidades principales de la aplicación trabajen como se espera y proporcionan un mecanismo para asegurar que futuros cambios no rompan funcionalidades existentes.

### Uso de tests:

1. Asegúrate de tener todas las dependencias instaladas, incluyendo `pytest` y `pytest-django`.
2. Desde la raíz del proyecto, ejecuta `pytest` para correr todos los tests.
3. Observa los resultados y asegúrate de que todos los tests pasen antes de hacer cambios o desplegar.

## Notificaciones por Correo:

Cuando hay un cambio en algún producto, el sistema tiene la capacidad de enviar notificaciones por correo electrónico. Para que esta funcionalidad funcione correctamente, se necesita:

1. Configurar las variables de entorno o ajustes de Django para el servidor SMTP.
2. Asegurarse de que los correos se envíen en un ambiente que no bloquee solicitudes salientes (por ejemplo, algunos ambientes de desarrollo locales podrían bloquear correos salientes).
3. Monitorizar la cola de correos para asegurarse de que se envíen adecuadamente.

## Deuda Técnica y Próximos Desarrollos:

Mientras se desarrollaba este proyecto, surgieron ideas y funcionalidades que se consideraron importantes, pero que aún no se han implementado. Estas son algunas de las tareas y mejoras pendientes:

- **Dockerización:** Implementar Docker para asegurar que el entorno de desarrollo sea replicable y evitar problemas de dependencias.

- **Tareas Automatizadas con Lambdas de AWS:** Se desea agregar tareas automatizadas que se ejecuten en función de eventos específicos, utilizando Lambdas de AWS.

- **Sistema de Correos con Celery:** Debido al potencial tráfico y demanda, es esencial implementar un sistema que maneje el envío de correos de manera asíncrona. La idea es utilizar Celery para esta tarea y asegurar que, en caso de cambios en productos, se envíen notificaciones por correo sin demoras ni interrupciones en el servicio principal.

- **Makefile:** Con el objetivo de automatizar y simplificar tareas repetitivas en el desarrollo (como tests, migraciones, entre otros), se considera esencial la creación de un `Makefile`.

- **Coverage:** Para asegurar la calidad del código y la correcta funcionalidad de todas las partes del sistema, se desea implementar `coverage` y monitorear el porcentaje de código que está siendo probado.


## Contribuciones:

Las contribuciones son bienvenidas. Por favor, abre un issue antes de enviar un pull request.
