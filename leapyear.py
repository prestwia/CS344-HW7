class leapyear:
    def leapyear(self, year):
        isLeap = False

        if year % 4 == 0:
            isLeap = True
        if year % 100 == 0:
            isLeap = False
        if year % 400 == 0:
            isLeap = True

        return isLeap