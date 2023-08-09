"""Fixtures module for api predict. This is a configuration file designed
to prepare the tests function arguments on the test_*.py files located in
the same folder.

You can add new fixtures following the next structure:
```py
@pytest.fixture(scope="module", params=[{list of possible arguments}])
def argument_name(request):
    # You can add setup code here for your argument/fixture
    return request.param  # Argument that will be passed to the test
```
The fixture argument `request` includes the parameter generated by the
`params` list. Every test in the folder that uses the fixture will be run
at least once with each of the values inside `params` list unless specified
otherwise. The parameter is stored inside `request.param`.

When multiple fixtures are defined with more than one parameter, every tests
will run multiple times, each with one of all the possible combinations of
the generated parameters unless specified otherwise. For example, in the
following configuration:
```py
@pytest.fixture(scope="module", params=['a','b'])
def my_fixture1(request):
    return request.param

@pytest.fixture(scope="module", params=['x','y'])
def my_fixture2(request):
    return request.param
```
The for the test functions in this folder, the following combinations will
be generated:
    - Tests that use only one my_fixture1: ['a','b']
    - Tests that use only one my_fixture2: ['x','y']
    - Tests that use both: [('a','x'), ('a','y'), ('b','x'), ('b','y')]
    - Tests that use none of the fixtures: []

Be careful when using multiple fixtures with multiple parameters, as the
number of tests generated can grow exponentially.
"""
# pylint: disable=redefined-outer-name
import pytest
from deepaas.model.v2.wrapper import UploadedFile

import api


@pytest.fixture(scope="module", params=["t100-images.npy"])
def input_file(request):
    """Fixture to provide the input_file argument to api.predict."""
    filepath = f"{api.config.DATA_PATH}/external"
    return UploadedFile("", filename=f"{filepath}/{request.param}")


@pytest.fixture(scope="module", params=["test_simplemodel"])
def model_name(request):
    """Fixture to provide the model_name argument to api.predict."""
    return request.param


@pytest.fixture(scope="module", params=["application/json"])
def accept(request):
    """Fixture to provide the accept argument to api.predict."""
    return request.param


# Example of fixture for a batch_size parametrization
# @pytest.fixture(scope="module", params=[None, 20])
# def batch_size(request):
#     """Fixture to provide the batch_size option to api.predict."""
#     return request.param


# Example of fixture for a steps parametrization
# @pytest.fixture(scope="module", params=[None, 2])
# def steps(request):
#     """Fixture to provide the steps option to api.predict."""
#     return request.param
