       
        
class Route(object):

    def __init__(self):
        self.person = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.a = [1, 2, 3, 4, 5]
        self.b = [6, 7]
        self.c = [8, 9, 10]
        
    def trip(self, number):    
        self.trip = number
        trip_no = 0
        while trip_no < self.trip:
            new = []
            new = self.a
            self.a = self.c
            self.c = self.b
            self.b = new
            trip_no += 1
        
        if trip_no == self.trip:
            print "a = ", self.a
            print "b = ", self.b
            print "c = ", self.c 
            
            for man in self.person:
                if man in self.a:
                    print "%s is in a" % man
                
                elif man in self.b:
                    print "%s is in b" % man
                        
                elif man in self.c:
                    print "%s is in c" % man


if __name__ == "__main__":
    r = Route()
    r.trip(5)

