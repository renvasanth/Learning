import unittest
"""
greater_smaller(l)
------------------
    Function that gives the biggest and smallest numbers from the input list
    
    l --> input list
        
    [big, small] --> output answer list
"""
def greater_smaller(l):    
    for number in l:        
        big = max(l)
        small = min(l)
        answer = [big, small]
        return answer

print "The big and small numbers are: ", greater_smaller([5, 3, 20, 8, 10, 95, 9, 2, 15, 6])


class GreatsmallTestCase(unittest.TestCase):
    def test_begining_and_ending(self):
        l = [78, 35, 25, 72, 5, 46, 3]
        self.assertEqual(greater_smaller(l), [78, 3])        
    def test_ending_and_begining(self):
        l = [2, 35, 25, 72, 5, 46, 83]
        self.assertEqual(greater_smaller(l), [83, 2])
    def test_middle_order(self):
        l = [12, 35, 25, 98, 3, 5, 46, 83]
        self.assertEqual(greater_smaller(l), [98, 3])
    def test_ordered(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(greater_smaller(l), [12, 1])
    def test_reversed(self):
        l = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(greater_smaller(l), [12, 0])
    def test_single(self):
        l = [4]
        self.assertEqual(greater_smaller(l), [4, 4])
    def test_same_two(self):
        l = [3, 3]
        self.assertEqual(greater_smaller(l), [3, 3])
    def test_two_answer(self):
        l = [78, 35, 25, 72, 3, 5, 78, 46, 3]
        self.assertEqual(greater_smaller(l), [78, 3])
    def test_minus(self):
        l =  [78, 35, 25, 72, 3, 5, -80, 46, -5]       
        self.assertEqual(greater_smaller(l), [78, -80])
