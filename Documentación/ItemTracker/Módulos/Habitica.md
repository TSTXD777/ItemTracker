# Descripción:

Módulo Principal que interactúa con la API de [Habitica](https://habitica.com). Se utiliza pricipalmente para manejar Hábitos, Tareas Diarias, ToDo's e interactuar con Grupos de la App.

# Clases
- [[Clase HabiticaAPIWrapper|HabiticaAPIWrapper]]: Encapsula la interacción con la API de Habitica.
- [[Clase Task|Task]]: Almacena una tarea, este puede ser un hábito, una tarea diaria o una tarea pendiente.
- [[Clase Reward|Reward]]: Almacena las recompensas personalizadas del usuario.
# Funciones
- user_data_get(): Obtiene información sobre el usuario como nivel, experiencia, oro, etc.
- data_sync(): Actualiza la información de la Base de Datos local con la de la plataforma online.
- habit_create(): Crea un nuevo hábito.
- habit_edit(): Modifica un hábito.
- habit_delete(): Elimina un hábito.
- habits_get(): Obtiene la lista de hábitos del usuario.
- habit_mark_complete(): Marca un hábito como completado.
- habit_mark_failed(): Marca un hábito como fallido.
- habit_update(): Actualiza el progreso de un hábito.
- daily_create(): Crea una nueva tarea diaria.
- daily_edit(): Modifica una tarea diaria.
- daily_delete(): Elimina una tarea diaria.
- dailies_get(): Obtiene la lista de tareas diarias del usuario.
- daily_mark_complete(): Marca una tarea diaria como completada.
- daily_update(): Actualiza el progreso de una actividad diaria.
- todo_create(): Crea una tarea pendiente.
- todo_edit(): Modifica una tarea pendiente.
- todo_delete(): Elimina una tarea pendiente.
- todos_get(): Obtiene la lista de tareas pendientes del usuario.
- todo_mark_complete(): Marca la tarea pendiente como completada.
- todo_update(): Actualiza el progreso de una tarea pendiente.
- todos_getCompleted(): Obtiene una lista de las tareas pendientes recientemente completadas.
- reward_create(): Crea una recompensa personalizada.
- reward_edit(): Modifica una recompensa personalizada.
- reward_delete(): Elimina una recompensa personalizada.
- rewards_get(): Obtiene la lista de recompensas del usuario.
- reward_purchase(): Utiliza las monedas del usuario para comprar una recompensa.
- party_getInfo(): Obtiene información sobre el equipo.
- party_getChat(): Obtiene el chat del equipo.
- party_sendMessage(): Envía un mensaje al equipo.

