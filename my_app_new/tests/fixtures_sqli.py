# import pytest
# from my_app_new.tests.conftest_sqlit import engine_test, metadata
#
#
# @pytest.fixture(scope="session", autouse=True)
# def setup_bd():
#     with engine_test.begin():
#         metadata.create_all(engine_test)
#         yield
#         metadata.drop_all(engine_test)
#


