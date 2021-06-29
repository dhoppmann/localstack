import logging
import os

from tests.persistence.conftest import WithPersistence

LOG = logging.getLogger(__name__)


def test_dynamodb_persistence(localstack_runtime: WithPersistence):
    assert os.path.isdir(localstack_runtime.data_dir)
