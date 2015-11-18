import unittest
# Class defination
class Camera(object):
    def __init__(self, position):        
        self.position = position
        
    def right(self):           
        if self.position == 'N':
            self.position = 'E'
            return self.position
        elif self.position == 'E':
            self.position = 'S'
            return self.position
        elif self.position == 'S':
            self.position = 'W'
            return self.position
        elif self.position == 'W':
            self.position = 'N'
            return self.position
                

    def left(self):
        if self.position == 'N':
            self.position = 'W'
            return self.position
        elif self.position == 'W':
            self.position = 'S'
            return self.position
        elif self.position == 'S':
            self.position = 'E'
            return self.position
        elif self.position == 'E':
            self.position = 'N'
            return self.position

        

if __name__ == "__main__":
    c = Camera('N')
    print c.right()



# TestCase
class CameraTestCase(unittest.TestCase):
    def test_direction(self):
	c = Camera('N')
	self.assertEqual(c.right(), 'E')
	self.assertEqual(c.right(), 'S')
	self.assertEqual(c.right(), 'W')
	self.assertEqual(c.right(), 'N')
	self.assertEqual(c.left(), 'W')
	self.assertEqual(c.left(), 'S')
	self.assertEqual(c.left(), 'E')
	self.assertEqual(c.left(), 'N')
	
