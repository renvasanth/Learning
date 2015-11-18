import unittest

from scale import Scale, Vegetable


class ScaleTestCase(unittest.TestCase):

    def setUp(self):
        self.s = Scale()
        self.s2= Scale()
        self.carrot = Vegetable('carrot', 2)
        self.onion = Vegetable('onion', 1)
        self.tomato = Vegetable('tomato', 3)

    def test_add_remove_item(self):
        self.assertEqual(self.s.add_item(self.onion), 1)
        self.assertEqual(self.s.add_item(self.carrot), 3)
        self.assertEqual(self.s.add_item(self.tomato), 6)
        
        self.assertEqual(self.s2.add_item(self.tomato), 3)
      
        # remove item assertions
        self.assertEqual(self.s.remove_item('tomato'),  3)
        self.assertEqual(self.s.remove_item('onion'),  2)
        self.assertEqual(self.s.remove_item('carrot'),  0)

    def test_list_items(self):
        self.assertEqual(self.s.list_items(), [])
        self.s.add_item(self.carrot)
        self.assertEqual(self.s.list_items(), ['carrot'])
        self.s.add_item(self.onion)
        self.assertEqual(self.s.list_items(), ['carrot','onion'])
        self.s.add_item(self.tomato)
        self.assertEqual(self.s.list_items(), ['carrot', 'onion', 'tomato'])

        self.s.remove_item('onion')
        self.assertEqual(self.s.list_items(), ['carrot', 'tomato'])
        self.s.remove_item('carrot')
        self.assertEqual(self.s.list_items(), ['tomato'])
        self.s.remove_item('tomato')
        self.assertEqual(self.s.list_items(), [])
