class Counter:
    __count = 0

    def count(self):
        self.__count += 1
        print(self.__count)
    
c = Counter()
c.count()
c.count()
print(c._Counter__count)

