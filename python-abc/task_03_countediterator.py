#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        next_item = next(self.iterator)
        self.count += 1
        return next_item

    def get_count(self):
        return self.count
