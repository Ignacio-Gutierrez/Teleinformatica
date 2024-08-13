# Casos Prácticos

## Caso-1: Direccionamiento IP y routing interno

Este proyecto utiliza Mininet para crear una red virtual. A continuación se detallan los pasos necesarios para configurar y ejecutar el entorno.

### Requisitos

- **Python 3.10.12**
- **Mininet**:

### Pasos para ejecutar el código

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Ignacio-Gutierrez/Teleinformatica.git
   cd Teleinformatica/Caso1

2. Ejecutar el script:
   sudo python3 TP_Tele_Caso1.py

3. Utilizar la CLI de Mininet para interactuar con la red.

## Caso-2: Cloud Computing Classic (Despliegue desde Openstack)

Este proyecto consiste en el despliegue de una infraestructura en OpenStack, incluye instancia para aplicación, balanceo de carga, base de datos y un bastión de seguridad.

### Descripción de las Instancias

#### 1. app-priv
- **Imagen:** Ubuntu 22.04
- **IP Interna:** 172.19.0.135
- **Flavor:** m1.medium
- **Descripción:** Esta instancia aloja la aplicación principal.

#### 2. bastion-priv
- **Imagen:** Ubuntu Minimal 22.04
- **IP Interna:** 172.19.0.168
- **IP Externa:** 192.168.3.141
- **Flavor:** m1.small
- **Descripción:** Esta instancia actúa como el bastión de seguridad, permitiendo acceso SSH seguro a las demás instancias, para su configuración.

#### 3. lb-priv
- **Imagen:** NGINX en Ubuntu 18.04
- **IP Interna:** 172.19.0.155
- **IP Externa:** 192.168.3.183
- **Flavor:** m1.small
- **Descripción:** Esta instancia se utiliza como balanceador de carga para distribuir el tráfico hacia las aplicaciones.

#### 4. db-priv
- **Imagen:** MySQL en Ubuntu 18.04
- **IP Interna:** 172.19.0.12
- **Flavor:** m1.small
- **Descripción:** Instancia dedicada para la base de datos MySQL.

![Instancias desplegadas](https://github.com/Ignacio-Gutierrez/Teleinformatica/blob/main/Caso2/IntanciasCaso2.png)

### Grupos de Seguridad

#### 1. sg_App
- **Captura de Pantalla:**
![Reglas de Grupo de Seguridad Metabase](https://github.com/Ignacio-Gutierrez/Teleinformatica/blob/main/Caso2/ReglasDeGrupoDeSeguridadApp.png)

#### 2. sg_bastion
- **Captura de Pantalla:**
![Reglas de Grupo de Seguridad Bastion](https://github.com/Ignacio-Gutierrez/Teleinformatica/blob/main/Caso2/ReglasDeGrupoDeSeguridadBastion.png)

#### 3. sg_lb
- **Captura de Pantalla:**
![Reglas de Grupo de Seguridad Loead Balancer](https://github.com/Ignacio-Gutierrez/Teleinformatica/blob/main/Caso2/ReglasDeGrupoDeSeguridadLoadBalancer.png)

#### 4. sg_db
- **Captura de Pantalla:**
![Reglas de Grupo de Seguridad Base de Datos](https://github.com/Ignacio-Gutierrez/Teleinformatica/blob/main/Caso2/ReglasDeGrupoDeSeguridadBaseDeDatos.png)