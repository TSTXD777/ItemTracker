from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

class HabiticaTaskType(Enum):
    HABIT = "habit"
    DAILY = "daily"
    TO_DO = "todo"
    REWARD = "reward"

class HabiticaTaskDifficulty(Enum):
    TRIVIAL = "trivial"
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class HabiticaTaskFrequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

class WeekDays(Enum):
    SUNDAY = "su"
    MONDAY = "m"
    TUESDAY = "t"
    WEDNESDAY = "w"
    THURSDAY = "th"
    FRIDAY = "f"
    SATURDAY = "s"
    
class KarmaAlignment(Enum):
    UP = "up"
    DOWN = "down"

@dataclass
class HabiticaAPIWeapper:
    api_key: str

@dataclass
class Reward:
    name: str
    value: int

@dataclass
class Task:
    name: str
    type: HabiticaTaskType
    alias: str
    checklist: Optional[list[str]]
    notes: Optional[str]
    deadline: Optional[datetime]
    difficulty: HabiticaTaskDifficulty
    frequency: HabiticaTaskFrequency
    WeekDays: Optional[list[WeekDays]]
    karma: Optional[list[KarmaAlignment]]