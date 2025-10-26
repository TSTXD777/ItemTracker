# Descripción:

Módulo Principal que administra el uso del tiempo del dispositivo, maneja las alarmas y el temporizador pomodoro para trabajar de manera óptima en algún proyecto.

# Clases
- [[Clase Alarm|Alarm]]: Representa una alarma individual.
- [[Clase UsageRecord|UsageRecord]]: Almacena información sobre el uso de una aplicación.
- [[Clase ActivityEntry|ActivityEntry]]: Contiene datos sobre una entrada de registro de actividad.
- [[Clase PomodoroSession|PomodoroSession]]: Administra una sesión de Pomodoro Completa.

# Funciones
- alarm_gettime()
- alarm_setTime()
- alarm_getMessage()
- alarm_setMessage()
- alarm_toggleEnable()
- tracking_start()
- tracking_end()
- record_create()
- record_edit()
- record_delete()
- usage_calculateDuration()
- activity_create()
- activity_edit()
- activity_delete()
- pomodoro_start()
- pomodoro_end()
- pomodoro_add()