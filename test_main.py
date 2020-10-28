import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
       for n in range(3,6) :
           for i in range(1,9) :
               p, mean = i*0.1, 0
               for j in range(100) : mean = mean + binomial(n,p)
               mean = mean / 100 
               bar = np.sqrt(n*p*(1-p)/100)*st.norm.ppf( (0.99 + 1) / 2 )
               self.assertTrue( np.fabs( mean - n*p )<bar, "your binomial function does not appear to be sampling from the correct distribution" )
               
