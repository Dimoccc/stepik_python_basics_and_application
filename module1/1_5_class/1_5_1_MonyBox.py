# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

# Класс должен иметь следующий вид



class MoneyBox:
    def __init__(self, capacity):
        self.count = 0              # количество монет
        self.capacity = capacity    # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if self.count + v <= self.capacity:
            return True
        else:
            return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if self.can_add(v) == True:
            self.count +=v
        # положить v монет в копилку