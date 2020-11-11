#!/usr/bin/env python

# Test three functions from the random module: 
import random
import unittest

class TestSequenceFunctions(unittest.TestCase): # <1>
    @classmethod
    def setUpClass(cls):  # <2>
        print("Starting all tests")

    def setUp(self):  # <3>
        self.seq = list(range(10))
        print("\n\nHello! : ", self.seq, "\n")

    def testshuffle(self):  # <4>
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        print(self.seq)
        self.seq.sort()
        print(self.seq)
        self.assertEqual(self.seq, list(range(10))) # <5>

    def testchoice(self):
        element = random.choice(self.seq)
        print("Single element ----> ", element)
        self.assertIn(element, self.seq)  # <6>

    def testsample(self):
        self.assertRaises(ValueError, random.sample, self.seq, 11)

        for element in random.sample(self.seq, 10):
            print("random sample: ", element)
            self.assertIn(element, self.seq)

    def tearDown(self):  # <7>
        print("Goodbye!")

    @classmethod
    def tearDownClass(cls):  # <8>
        print("Ending all tests")

if __name__ == '__main__':

    unittest.main()  # <9>
