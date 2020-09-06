class DateIterator:
    def __init__(self, start_date, end_date, delta):
        self.start_date = start_date
        self.current_date = start_date
        self.end_date = end_date
        self.delta = delta

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_date > self.end_date:
            raise StopIteration
        return_date = self.current_date
        self.current_date = self.current_date + self.delta
        return return_date
