class parent (object):
    def altered(self):
        print("parent alterd()")

class child(parent):
    def altered(self):
        print("child, before parent alterd()")
        super(child, self).altered()
        print("child, after paent altered()")
dad = parent()
son = child()

dad.altered()
son.altered()
        