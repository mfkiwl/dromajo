#******************************************************************************
# Copyright (C) 2018, Esperanto Technologies Inc.
# The copyright to the computer program(s) herein is the
# property of Esperanto Technologies, Inc. All Rights Reserved.
# The program(s) may be used and/or copied only with
# the written permission of Esperanto Technologies and
# in accordance with the terms and conditions stipulated in the
# agreement/contract under which the program(s) have been supplied.
#------------------------------------------------------------------------------

import pytest

def pytest_addoption(parser):
    parser.addoption("--output-dir",
                     required=True,
                     help="Test output folder")
    parser.addoption("--riscvemu",
                     required=True,
                     help="Path to riscvemu")

@pytest.fixture
def output_dir(request):
    return request.config.getoption("--output-dir")

@pytest.fixture
def riscvemu(request):
    return request.config.getoption("--riscvemu")
