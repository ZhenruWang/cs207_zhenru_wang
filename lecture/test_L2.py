import L2_nodoc
import doctest
import pytest
import numpy as np

def test_L2_result():
    assert L2_nodoc.L2([1,1]) == np.sqrt(2)
    
def test_L2_weight_result():
    assert L2_nodoc.L2([1,1],[1,1]) == np.sqrt(2)
    
def test_L2_weight1_result():
    assert L2_nodoc.L2([1,1],[2,1]) == np.sqrt(5)