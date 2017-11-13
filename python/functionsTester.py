import unittest, functions

class functionsTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_addition(self):
        self.assertEqual(functions.addition(0,0), 0)
        self.assertEqual(functions.addition(1,0), 1)
        self.assertEqual(functions.addition(10,1), 11)
        self.assertEqual(functions.addition(20,20), 40)  

    def test_getElementInList(self):
        testList = [1, 2, 3, 8, 6, 9, 4, 5, 0, 10]
        self.assertEqual(functions.getElementInList(0,testList), 1)
        self.assertEqual(functions.getElementInList(1,testList), 2)
        self.assertEqual(functions.getElementInList(9,testList), 10)
        self.assertEqual(functions.getElementInList(2,testList), 3)  

    def test_slightlyBrokenDivider(self):
        self.assertEqual(functions.slightlyBrokenDivider(0,0), None)
        self.assertEqual(functions.slightlyBrokenDivider(1,1), 1)
        self.assertEqual(functions.slightlyBrokenDivider(10, 2), 5)
        self.assertEqual(functions.slightlyBrokenDivider(20,20), 1) 
        self.assertEqual(functions.slightlyBrokenDivider(10, 3), 10/3) 


if __name__ == "__main__": 
    unittest.main()