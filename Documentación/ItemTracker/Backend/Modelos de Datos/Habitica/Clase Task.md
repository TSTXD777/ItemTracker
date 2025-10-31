Atributos:
- name: el título de la tarea.
- type: el tipo de tarea.
	- opción única: "habit", "daily", "todo".
- alias: el alias interno de la tarea.
- checklist: una lista de items de la tarea.
- notes: una nota o descripción en la tarea.
- deadline: fecha límite para una tarea.
	- validez: solo para tipo "todo".
- difficulty: la dificultad de una tarea.
	- opción única: "trivial", "easy", "medium", "hard".
- frequency: la frecuencia con la cual la tarea se repite.
	- validez: solo para tipo "daily".
	- opción única: "daily", "weekly", "monthly", "yearly".
- week_days: días de la semana en la cual la tarea se repite.
	- validez: solo para tipo "daily".
	- opción múltiple: "su", "m", "t", "w", "th", "f", "s".
- karma: menciona si la actividad está configurada como negativa, positiva o ambas.
	- validez: solo para tipo "habit".
	- opción múltiple: "up", "down".

---
Perteneciente al Módulo [[Habitica]].