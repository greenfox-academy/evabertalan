import unittest
import function

class TestFunc(unittest.TestCase):

    def setUp(self):
        self._c1=function.Character(health=10, armor=5)
        self._c2=function.Character(health=50, armor=30)

        self._eventlist=[
            {'character': self._c1, 'type': 'damage', 'size': 50},
            {'character': self._c2, 'type': 'damage', 'size': 50},
            {'character': self._c2, 'type': 'heal', 'size': 50},
        ]

    def test_should_handle_the_damage_events(self):
            function.handleEvents(self._eventlist)
            self.assertFalse(self._c1.isAlive())
            self.assertTrue(self._c2.isAlive())

    def test_should_heal_a_character(self):
        function.handleEvents(self._eventlist)
        self.assertEqual(self._c2.getHealth(), 100)



    def test_should_apply_func(self):
           array = [1,2,3]
           self.assertEqual(function.adder(array), [2,3,4])

    def test_filter_array(self):
            array=[0,1,2,3,4,5,6,7,8,9]
            self.assertEqual(function.filterArray(array),[0,3,6,9])


unittest.main()
