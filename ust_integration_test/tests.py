import logging
import os

from ust_integration_test.test_sync import TestSync
from ust_integration_test.utils import init_logger, get_test_name

init_logger(logging.DEBUG)
logger = logging.getLogger()
root_dir = os.getcwd()


def run_test(test_name, test_dir):
    try:
        test = TestSync(test_name, str(test_dir))
        test.run_test()
    finally:
        os.chdir(root_dir)


class TestSetUp(object):

    def test_delete_all_users(self, tmpdir):
        run_test('delete_all_users', tmpdir)


class TestUST(object):

    def test_create_all_users(self, tmpdir):
        run_test(get_test_name(), tmpdir)

    def test_create_all_users_2(self, tmpdir):
        run_test(get_test_name(), tmpdir)