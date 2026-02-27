
import logging 
'''
# changing 
print('program started')
logging.basicConfig(level=logging.INFO)
logging.info("program started")

# msg abt error 

logging.basicConfig(level=logging.ERROR)

age = -5
if age < 0:
    logging.error('age cannot be negative')

# logging into a file 
logging.basicConfig(level=logging.INFO, filename="logfile.log", filemode="w")
    
        
    
logging.info("program start")
logging.warning("not enough memory")
logging.error("connection error")


#log + try/except

logging.basicConfig(level=logging.ERROR)
try:
    x = int("abc")
except ValueError 
    logging.ERROR("cannot transform string into an integer")
'''
import unittest

def square(x):
    return x * x 

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4),16)

if '__name__ == __main__':
    unittest.main()