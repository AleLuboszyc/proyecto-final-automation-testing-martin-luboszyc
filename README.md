# proyecto-final-automation-testing-martin-luboszyc
Proyecto Final Integrador de Talento Tech Automatizacion QA
# Proyecto Final Integrador

Este proyecto es la entrega final del curso de Testing QA de Talento Lab.
El framework implementa una estrategia de prueba de dos capas, abarcando la interfaz de usuario (UI) y la capa de servicios (API), utilizando el patrón de diseño Page Object Model (POM) para garantizar la escalabilidad y reusabilidad del código.

## Tecnologías y Dependencias

| Rol | Tecnología | Propósito |
| **Lenguaje** | Python 3.x | Lenguaje principal de programación. |
| **Framework** | Pytest | Motor de ejecución y aserciones. |
| **Automatización UI** | Selenium WebDriver | Interacción con la interfaz web (SauceDemo). |
| **Automatización API** | Biblioteca Requests | Pruebas de los Endpoints de servicios (JSONPlaceholder). |
| **Manejo de Driver** | WebDriver Manager | Gestión automática del ChromeDriver. |
| **Datos** | CSV (Data-Driven) | Parametrización de tests de Login. |
| **Reportes** | pytest-html | Generación de reportes visuales. |

## Estructura del Proyecto (Page Object Model)

La estructura sigue el patrón Page Object Model para asegurar la separación de responsabilidades.
