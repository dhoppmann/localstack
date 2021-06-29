import os
import shutil
import time

import pytest

import localstack.config
from tests import runtime

TIMEOUT = 30


class WithPersistence:
    data_dir: str

    def __init__(self, runtime, data_dir) -> None:
        super().__init__()
        self.runtime = runtime
        self.data_dir = data_dir


@pytest.fixture
def localstack_runtime(tmpdir):
    try:
        os.environ['DATA_DIR'] = str(tmpdir.realpath())
        localstack.config.DATA_DIR = str(tmpdir.realpath())
        if not runtime.start(timeout=TIMEOUT):
            raise IOError('did not startup localstack in time')
        time.sleep(0.5)
        yield WithPersistence(runtime, tmpdir)
    finally:
        runtime.reset()
        shutil.rmtree(localstack.config.DATA_DIR, ignore_errors=True)
