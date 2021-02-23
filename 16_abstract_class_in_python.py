# This is useful for template method

from abc import ABC, abstractmethod


# need to extend Abstract Base Class
class AbstractRecipe(ABC):

    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dish(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class Recipe1(AbstractRecipe):
    def get_ready(self):
        print('get raw materials')

    def do_the_dish(self):
        print('do the dish')

    def cleanup(self):
        print('cleaning')


class Recipe2(AbstractRecipe):
    def get_ready(self):
        print('get raw materials 2')

    def do_the_dish(self):
        print('do the dish 2')

    def cleanup(self):
        print('cleaning 2')


recipe1 = Recipe1()
recipe1.execute()
