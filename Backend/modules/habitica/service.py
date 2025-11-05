from modules.habitica.models import Task

class HabiticaService: #TODO: Implementar métodos para interactuar con la API de Habitica
    def user_data_get():
        pass
    def data_sync():
        pass

class Habit(Task): #TODO: Implementar métodos específicos para tareas de tipo Habit
    def create():
        pass
    def edit():
        pass
    def delete():
        pass
    def get_all():
        pass

    def mark_complete():
        pass
    def mark_failed():
        pass
    def update_progress():
        pass

class Daily(Task): #TODO: Implementar métodos específicos para tareas de tipo Daily
    def create():
        pass
    def edit():
        pass
    def delete():
        pass
    def get_all():
        pass
    def mark_complete():
        pass
    def update_progress():
        pass

class ToDo(Task): #TODO: Implementar métodos específicos para tareas de tipo To-Do
    def create():
        pass
    def edit():
        pass
    def delete():
        pass
    def get_all():
        pass
    def mark_complete():
        pass
    def update_progress():
        pass
    def get_all_completed():
        pass

class Reward(Task):
    def create():
        pass
    def edit():
        pass
    def delete():
        pass
    def get_all():
        pass
    def purchase():
        pass

class Party:
    def get_info():
        pass
    def get_chat():
        pass
    def send_message():
        pass