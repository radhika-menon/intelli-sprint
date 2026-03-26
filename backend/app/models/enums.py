from enum import Enum

class WeekDay(str, Enum):
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thu = "Thu"
    Fri = "Fri"
    Sat = "Sat"
    Sun = "Sun"

class ActivityStatus(str, Enum):
    planned = "Planned"
    in_progress = "In Progress"
    achieved = "Achieved"
    on_hold = "On hold"
    dropped = "Dropped"