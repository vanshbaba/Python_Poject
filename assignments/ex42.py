## Animal is-a object (yes, sort of confusing) look at the extra credit.
class animal(object):
    pass
## dog is a obect of aninmal
class dog(animal):
    def __inti__(self,name):
        ## name is a atribute of dog
        self.name = name

## cat is object of animal
class cat(animal):
    ##name is a atribute of cat
    def __init__(self,name):
        self.name  = name


## person is a boject
class person(object):
    def __init__(self, name):
        ## name is atribute of person
        self.name = name
        ## person has-a pet of some kind
        self.pet = None

## employee is a object of person
class employee (person):
    def __init__(self, name, salary):
        ## name and salary is a atribute of a employee ? hummm what is thsi strange magic?
        super(employee,self).__init__(name)
        ##salary is a atribute of employee
        self.salary = salary

## fish ia a object
class fish(object):
    pass
## salmon is a object of fish
class salmon(fish):
    pass
## habibut is a object of fish
class habibut(fish):
    pass
## rover is-a dog
rover = dog()
## satan is a cat
satan = cat("satan")

##mary is a person
mary = person("mary")

##mary is a instance of a pet and that has a satan

mary.pet = satan
## frank is a person who is employee has a name frank and salay 1290000
frank = employee("frank", 1290000)
## frank is a owner of per it has a name of rover
frank.pet = rover
## fish is a object has a flipper instance
flipper = fish()
## crouse is a atribute of salmon
crouse = salmon()
## harry is fish name and it is a instance of habibut atribute.
harry = habibut()