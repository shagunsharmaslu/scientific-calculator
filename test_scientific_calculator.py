import unittest
from scientific_calculator import sin,cos,tan,log,exp,sqrt

class Test_Scientific_Calculator(unittest.TestCase):
 # test for sin function
 def test_sin_positive(self):
     result = sin(90)
     self.assertAlmostEqual(result, 1, places=5)
     
 def test_sin_negative(self):
     result = sin(-90)
     self.assertAlmostEqual(result, - 1, places=5)
     
 def test_sin_zero(self):
     result = sin(0)
     self.assertAlmostEqual(result, 0, places=5)
     
 def test_sin_non_numeric(self):
     with self.assertRaises(TypeError):
        sin("hello")
        
# test for cos function
 def test_cos_positive(self):
     result = cos(180)
     self.assertAlmostEqual(result, -1, places=5)
     
 def test_cos_negative(self):
     result = cos(-180)
     self.assertAlmostEqual(result, -1, places=5)
     
 def test_cos_zero(self):
     result = cos(0)
     self.assertAlmostEqual(result, 1, places=5)
     
 def test_cos_non_numeric(self):
     with self.assertRaises(TypeError):
        cos("hello")
        
 # test for tan function
 def test_tan_positive(self):
     result = tan(45)
     self.assertAlmostEqual(result, 1, places=5)
     
 def test_tan_negative(self):
     result = tan(-45)
     self.assertAlmostEqual(result, - 1, places=5)
     
 def test_tan_zero(self):
     result = tan(0)
     self.assertAlmostEqual(result, 0, places=5)
     
 def test_tan_non_numeric(self):
     with self.assertRaises(TypeError):
        tan("hello")
        
 # test for sqrt function
 def test_sqrt_positive(self):
     result = sqrt(4)
     self.assertEqual(result, 2)
     
 def test_sqrt_negative(self):
     with self.assertRaises(ValueError):
         sqrt(-4)
     
 def test_sqrt_zero(self):
     result = sqrt(0)
     self.assertEqual(result, 0)
     
 def test_sqrt_non_numeric(self):
     with self.assertRaises(TypeError):
        sqrt("hello")
        
 # test for log function
 def test_log_positive(self):
     result = log(1)
     self.assertEqual(result, 0)
       
 def test_log_zero(self):
     with self.assertRaises(ValueError):
        log(0)
     
 def test_log_non_numeric(self):
     with self.assertRaises(TypeError):
        log("hello")
        
 def test_log_invalid(self):
     with self.assertRaises(ValueError):
         log(-1)

 # test for exp function
 def test_exp_positive(self):
     result = exp(1)
     expected = 2.71828
     self.assertAlmostEqual(result, expected, places=5)
    
 def test_exp_negative(self):
     result = exp(-1)
     expected = 0.36788
     self.assertAlmostEqual(result, expected, places=5)
    
 def test_exp_zero(self):
     result = exp(0)
     self.assertEqual(result, 1)
    
 def test_exp_non_numeric(self):
     with self.assertRaises(TypeError):
         exp("hello")

if __name__ == '__main__':
 unittest.main()