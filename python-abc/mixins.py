from datetime import datetime

class TimestampMixin:
    def get_timestamp(self):
        return datetime.now()

# mixin = TimestampMixin()
current_time = TimestampMixin().get_timestamp() # Note: cannot call directly from the object, have to call and create an instance (object) first.
print(current_time)


### if want get_timestamp() to be called without creating an instance, you can turn it into a static method using @staticmethod

class TimestampMixin:
    @staticmethod
    def get_timestamp():
        return datetime.now()

current_time = TimestampMixin.get_timestamp()
print(current_time)
