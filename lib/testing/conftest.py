#!/usr/bin/env python3

import pytest 
@pytest.fixture(scope="session")
def setup():
    print("Setting up the test environment")
    yield
    print("Tearing down the test environment")

    
    

