from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

class WeekDays(Enum):
    SUNDAY = "su"
    MONDAY = "m"
    TUESDAY = "t"
    WEDNESDAY = "w"
    THURSDAY = "th"
    FRIDAY = "f"
    SATURDAY = "s"

@dataclass
class ActivityEntry:
    id: Optional[str] # MongoDB genera un ID automáticamente
    timestamp: datetime
    description: str
    usage_list: list[str]

    def create():
        pass
    def edit():
        pass
    def delete():
        pass
    def query():
        pass

@dataclass
class Alarm:
    name: str
    id: Optional[str] # MongoDB genera un ID automáticamente
    time: datetime.time
    days: list[WeekDays]
    message: Optional[str]
    enabled: bool
    sound: Optional[str]

    #TODO: Implementar métodos para la clase Alarm
    def get_time():
        pass
    def set_time():
        pass
    def get_message():
        pass
    def set_message():
        pass
    def toggle_enabled():
        pass

@dataclass
class PomodoroSession:
    start_time: datetime
    end_time: Optional[datetime]
    pomodoro_count: int
    session_notes: Optional[str]

    def start():
        pass
    def end():
        pass
    def add_cycle():
        pass

@dataclass
class UsageRecord:
    app_package: str
    app_name: str
    id: Optional[str] # MongoDB genera un ID automáticamente
    start_time: datetime
    end_time: datetime
    duration_seconds: int

    def create():
        pass
    def edit():
        pass
    def delete():
        pass
    def query():
        pass
    def calculate_duration():
        pass