class DataBoxModel:
    def set_date(self, date):
        self.date = date

    def set_name(self, name):
        self.name = name

    def set_count(self, count):
        self.count = count

    def set_distance(self, distance):
        self.distance = distance

    def get_date(self):
        return self.date

    def get_name(self):
        return self.name

    def get_count(self):
        return self.count

    def get_distance(self):
        return self.distance


i = 0
l = []
while i < 3:
    l.append(DataBoxModel())
    l[i].set_name(1)
    l[i].set_count('3')
    l[i].set_date('33333')
    i+=1

print(l[2].get_name())