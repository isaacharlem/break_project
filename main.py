"""main.py"""


import pandas as pd


def check_event_validity(name, start_time, end_time, category = "Event", desc = None, people = None):
    """Checks the validity of an instance of Event."""
    if not isinstance(name, str):
        raise TypeError("Event name must be a string.")
    if not isinstance(category, str):
        raise TypeError("Event category must be a string.")
    if not isinstance(start_time, str):
        raise TypeError("Event start time must be a string.")
    if len(start_time) != 4:
        raise ValueError("Event start time must be in the format 'HHMM'.")
    if not 0 <= int(start_time[:2]) < 24 or not 0 <= int(start_time[2:4]) < 60:
        raise ValueError("Event start time must be a valid time.")
    if not isinstance(end_time, str):
        raise TypeError("Event end time must be a string.")
    if len(end_time) != 4:
        raise ValueError("Event end time must be in the format 'HHMM'.")
    if not 0 <= int(end_time[:2]) < 24 or not 0 <= int(end_time[2:4]) < 60:
        raise ValueError("Event end time must be a valid time.")
    if start_time > end_time:
        raise ValueError("Event start time must occur before end time.")
    if desc and not isinstance(desc, str):
        raise TypeError("Event description must be a string.")
    if people and not isinstance(people, list):
        raise TypeError("Event people must be a list of strings.")
    for person in people:
        if not isinstance(person, str):
            raise TypeError("Event people must be a list of strings.")

class Event:
    """Creates an instance of event."""
    def __init__(self, name, start_time, end_time, category = "Event", desc = None, people = None):
        """Constructor"""
        check_event_validity(name, start_time, end_time, category, desc, people)

        self.name = name
        self.category = category
        self.start_time = start_time
        self.end_time = end_time
        self.desc = desc
        self.people = people

    def __repr__(self):
        """Returns a string representation of Event."""
        if not self.desc and not self.people:
            return f"Event Name:\n  {self.name}\nCategory:\n  {self.category}\nTime:\n  {self.start_time} - {self.end_time}"
        
        if not self.people:
            return f"Event Name:\n  {self.name}\nCategory:\n  {self.category}\nTime:\n  {self.start_time} - {self.end_time}\nEvent Description:\n  '{self.desc}'"
        
        base_string = f"Event Name:\n  {self.name}\nCategory:\n  {self.category}\nTime:\n  {self.start_time} - {self.end_time}\nPeople:\n "
        for person in self.people[:len(self.people) - 1]:
            base_string += " " + person + ","
        base_string += " " + self.people[-1]
    
        if not self.desc:
            return base_string
        
        return base_string + f"\nEvent Description:\n  '{self.desc}'"


class DailySchedule:
    """Creates an instance of DailySchedule."""
    def __init__(self, date):
        """Constructor"""
        assert isinstance(date, str)

        self.schedule = []
        self.date = date

    def __repr__(self):
        """Returns a string representation of DailySchedule."""
        day_of_week = pd.to_datetime(self.date).day_name()
        if len(self.schedule) == 1:
            base_string = f"On {day_of_week}, {self.date}, you have 1 event:"
            event = "\n\n" + self.schedule[0].__repr__()
            return base_string + event
        
        base_string = f"On {day_of_week}, {self.date}, you have {len(self.schedule)} events:"
        events = sorted(self.schedule, key=lambda x: x.start_time)
        for event in events:
            base_string += "\n\n" + event.__repr__()

        return base_string

    def add_event(self, event):
        """
        Adds an instance of Event to DailySchedule.

        Inputs:
            event [Event]: an event
        """
        self.schedule.append(event)
