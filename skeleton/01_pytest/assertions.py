from unitest import TestCase 

class TestAssertions(TestCase):
    
    
    def test_all_assertions(self):
        self.assertEqual(a,b)
        self.assertNotEqual(a,b)
        self.assertTrue(x)
        self.assertFalse(x)
        self.assertIs(a,b)
        self.assertIsNot(a,b)
        self.assertIsNone(x)
        self.assertIsNotNone(x)
        self.assertIn(a,b)
        self.assertNotIn(a,b)
        self.assertIsInstance(a,b)
        self.assertNotIsInstance(a,b)
        self.assertRaises(exc,fun,*args,**kwds)
        self.assertRaisesRegex(exc,r,fun,*args,**kwds)
        self.assertWarns(warn,fun,*args,**kwds)
        self.assertWarnsRegex(warn,r,fun,*args,**kwds)
        self.assertLogs(logger,level)
        self.assertMultiLineEqual(a,b)
        self.assertSequenceEqual(a,b)
        self.assertListEqual(a,b)
        self.assertTupleEqual(a,b)
        self.assertDictEqual(a,b)
        self.assertSetEqual(a,b)
        self.assertAlmostEqual(a,b)
        self.assertNotAlmostEqual(a,b)  
        self.assertGreater(a,b)
        self.assertGreaterEqual(a,b)
        self.assertLess(a,b)
        self.assertLessEqual(a,b)
        self.assertRegex(s,r)
        self.assertNotRegex(s,r)
        self.assertCountEqual(a,b)
   


        