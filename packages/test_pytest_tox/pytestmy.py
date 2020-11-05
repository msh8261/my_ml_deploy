import pytest 

from my_module import squre_my


@pytest.fixture
def input_val():
	return 4

def test_pytest(input_val):
	sub = squre_my(input_val)
	assert sub==16

def test():
	sub = squre_my(4)
	assert sub==16

@pytest.mark.parametrize('inputs', [2,3,4])

def test_pytest(inputs):
	sub = squre_my(inputs)
	assert isinstance(sub, int)
