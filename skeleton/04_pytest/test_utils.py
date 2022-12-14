from utils import str_to_bool
import pytest

class TestStrToBool :
    
    
    @pytest.mark.parametrize('user_input',['y','Y','yes','YES','1','','   '])
    def test_true_vals(self,user_input):
        assert str_to_bool(user_input) is True
        
    @pytest.mark.parametrize('user_input',['no','0','N','No','nO','no  '])
    def test_false_vals(self,user_input):
        assert str_to_bool(user_input) is False

'''      
    def test_y_is_true(self) :
        assert str_to_bool('y') is True
        
    def test_1_is_true(self) :
        assert str_to_bool('1') is True
        
    def test_Y_is_true(self) :
        assert str_to_bool('Y') is True
    
    def test_yes_is_true(self) :
        assert str_to_bool('yes') is True

    def test_YES_is_true(self) :
        assert str_to_bool('YES') is True


    def test_empty_is_true(self) :
        assert str_to_bool('') is True
'''