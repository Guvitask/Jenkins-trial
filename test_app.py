import unittest
from app import hello

class TestApp(unittest.Testcase):
   def test_hello(self):
     self.asserEqual(hello(), "Hello, jenkins!" )

if __name__== "__main__":
   unittest.main()
