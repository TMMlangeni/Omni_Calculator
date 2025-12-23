import Omni_Calculator as oc
import pytest

def test_calculate_mean():
    assert oc.calculate_mean([10, 20, 30]) == 20.0
    assert oc.calculate_mean([-1, -2, -3]) == -2.0
    # Testing that it raises an error when given a string
    with pytest.raises(TypeError): 
        oc.calculate_mean(["dog", "cat"])

def test_calculate_mode():
    assert oc.calculate_mode([10, 10, 20, 30]) == 10.0
    assert oc.calculate_mode([2.1, 2.1, -3, 8]) == 2.1

def test_calculate_median():
    assert oc.calculate_median([10, 20, 30]) == 20
    assert oc.calculate_median([2, 4, 6, 8]) == 5.0
    # Simplified error check
    with pytest.raises(TypeError): 
        oc.calculate_median(["dog", "cat"]) 

def test_cond_Prob():
    assert round(oc.con_prob(0.5, 0.7), 2) == 0.71
    # Check that it returns None on zero division
    assert oc.con_prob(0.4, 0) is None

def test_quadratic_eq():
    # FIXED: Removed the space after the comma to match main script
    assert oc.quadratic_eq(2, 4, -3) == "x1 = 0.58, x2 = -2.58"
    assert oc.quadratic_eq(2, 4, 2) == "x = -1.00"
    assert oc.quadratic_eq(1, 2, 5) == "There are no real roots"