#!/usr/bin/env python3

class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
