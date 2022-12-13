import util # import module contains function to test

# First Test
# def test_util():
    
#     result = util.str_to_int('3.87')
#     assert result == 3

# Second Test
# def test_float_rounds_down():
    
#     result = util.str_to_int('3.99')
#     assert result == 3

# Third Test
# def test_float_round_down_lesser_half():
    
#     result = util.str_to_int('3.2')
#     assert result == 3
    
# Convention Testing Using OOP

class TestFloats:
    
    def setup(self):
        print('\nthis is setup')
        
    def teardown(self):
        print('\nthis is teardown')
        
    # Define some class methods
    def setup_class(cls):
        print('\nthis is setup class')
    def teardown_class(cls):
        print('\nthis is teardown class')
    
    # Second Test Inside Class
    def test_rounds_down(self):

        result = util.str_to_int('3.99')
        assert result == 3
        
    # Third Test Inside Class
    def test_round_down_lesser_half(self):
    
        result = util.str_to_int('3.2')
        assert result == 3