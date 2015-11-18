       
        
class Route(object):

    def __init__(self):
        self.person = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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
            
            for per in self.person:
                for man in self.a:
                    if man == per:
                        print "%s is in a" % man
                
                for man in self.b:
                    if man == per:
                        print "%s is in b" % man
                        
                for man in self.c:
                    if man == per:
                        print "%s is in c" % man


if __name__ == "__main__":
    r = Route()
    r.trip(3)

