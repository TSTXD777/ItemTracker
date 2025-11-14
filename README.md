# ItemTracker

**Descripción**  
ItemTracker es una aplicación de escritorio diseñada para mejorar la productividad personal, ofreciendo herramientas avanzadas para organizar tareas, hábitos y recompensas de manera eficiente.

## Características Principales  
1. **Integración con API**: Se integra con APIs de terceros como Habitica para enriquecer la experiencia del usuario.  
2. **Organización Personalizada**: Permite gestionar tareas, hábitos y recompensas según las necesidades individuales.  
3. **Interfaz Intuitiva**: Cuenta con una interfaz de usuario fácil de usar para mejorar la experiencia.  
4. **Sincronización de Datos**: Actualiza automáticamente la base de datos local para mantenerla sincronizada con la plataforma online.  
5. **Gestión de Tareas y Hábitos**: Incluye opciones avanzadas para crear, editar y gestionar tareas diarias y hábitos.  
6. **Monitoreo del Uso**: Registra detalles como duración de sesiones y horarios de inicio y finalización.  
7. **Atributos para Mejora Continua**: Almacena datos como fechas de creación/modificación para optimizar futuras actualizaciones.  

## Módulos en Desarrollo  
- **Habitica**: Integra funcionalidades con la API de Habitica, incluyendo clases como `HabiticaAPIWrapper`, `Reward` y `Task`.  
- **ItemListManager**: Gestiona elementos y listas mediante clases como `Item`, `ItemList` y `Tag`.  
- **TimeTracker**: Monitorea el tiempo con componentes como `PomodoroSession`, `ActivityEntry`, `Alarm` y `UsageRecord`.  

## Estructura del Directorio  
```
/Backend/
  /Modelos de Datos/
    /Habitica/
      Clase HabiticaAPIWrapper
      Clase Reward
      Clase Task
    /ItemListManager/
      Clase Item
      Clase ItemList
      Clase Tag
    /TimeTracker/
      Clase ActivityEntry
      Clase Alarm
      Clase PomodoroSession
      Clase UsageRecord
/Frontend/
  Godot
  Interfaz de usuario
/Inicio/
  Descripción Proyecto
  Lista de Módulos
/Instrucciones para desarrolladores/
  Etapas de Desarrollo
  Inicio de Workspace
  Patrones de Diseño
/Módulos/
  Habitica
  ItemListManager
  TimeTracker
```  

## Patrones de Diseño  
El proyecto implementa patrones de diseño documentados en las instrucciones para desarrolladores.

## Configuración del Entorno  
Sigue las instrucciones en `Instrucciones para desarrolladores/Inicio de Workspace` para configurar el entorno de desarrollo.