"""main.py"""


import pandas as pd


class Event:
    """Creates an instance of event."""
    def __init__(self, name, category, start_time, end_time, desc = None, people = None):
        """Constructor"""
        assert isinstance(name, str)
        assert isinstance(category, str)
        assert isinstance(start_time, str) # TODO: add checkers for time validity
        assert isinstance(end_time, str) # TODO: add checkers for time validity
        if desc:
            assert isinstance(desc, str)
        if people:
            assert isinstance(people, list) # TODO: add checkers for people validity

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
        
        if not self.desc:
            return f"Event Name:\n  {self.name}\nCategory:\n  {self.category}\nTime:\n  {self.start_time} - {self.end_time}\nPeople:\n  {[person for person in self.people]}" # TODO: make it list people more legibly
        
        if not self.people:
            return f"Event Name:\n  {self.name}\nCategory:\n  {self.category}\nTime:\n  {self.start_time} - {self.end_time}\nEvent Description:\n  '{self.desc}'"
        
        return f"Event Name:\n  {self.name}\nCategory:\n  {self.category}\nTime:\n  {self.start_time} - {self.end_time}\nPeople:\n  {[person for person in self.people]}\nEvent Description:\n  '{self.desc}'"


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
        for event in self.schedule:
            base_string += "\n\n" + event.__repr__()

        return base_string

    def add_event(self, event):
        """
        Adds an instance of Event to DailySchedule.

        Inputs:
            event [Event]: an event
        """
        self.schedule.append(event)

