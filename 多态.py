"""
需求：
警务人和警犬一起工作，警犬分2种：追击敌人和追查毒品，携带不同的警犬，执行不同分工作。
"""


class Dog(object):
    def work(self):
        pass


class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DrugDog(Dog):
    def work(self):
        print('追查毒品')


class Person(object):
    def work_with_dog(self, dog):
        dog.work()


ad = ArmyDog()
dd = DrugDog()


daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)
