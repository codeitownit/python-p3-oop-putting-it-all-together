#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) != int:
            print("size must be an integer")
        else:
            self._size = size
    def cobble(self, condition = "New"):
        print("Your shoe is as good as new!")
        self.condition = condition



    size = property(get_size, set_size,)

stan_smith = Shoe("Adidas", 9)
stan_smith.size
stan_smith.cobble()