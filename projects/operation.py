import unittest
# class definition for Operation
class Operation(object):
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2   
   
    def add(self):
        return self.n1 + self.n2
    def sub(self):
        return self.n1 - self.n2
    def mul(self):
        return self.n1 * self.n2
    def div(self):
        return self.n1  / self.n2
   
if __name__== "__main__":
	op = Operation(100, 20)
	print "Sum: ", op.add()
	print "Difference: ", op.sub()
	print "Product: ", op.mul()
	print "Quotient: ", op.div()

# Test Case
class OperationTestCase(unittest.TestCase):
    def test_both_minus(self):
        op = Operation(-100, -20)
        self.assertEqual(op.add(), -120)
        self.assertEqual(op.sub(), -80)
        self.assertEqual(op.mul(), 2000)
        self.assertEqual(op.div(), 5)
    def test_first_minus(self):
        op = Operation(-100, 20)
        self.assertEqual(op.add(), -80)
        self.assertEqual(op.sub(), -120)
        self.assertEqual(op.mul(), -2000)
        self.assertEqual(op.div(), -5)
