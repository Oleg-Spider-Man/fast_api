# import pytest
# import pytest_asyncio
# from starlette.testclient import TestClient
#
# from my_app_new.main import app
# from my_app_new.operations.models import Author, Book # noqa
# from my_app_new.auth.models import User # noqa
# #from migrations.env import target_metadata
# from my_app_new.tests.conftest_by import engine_test, metadata
#
#
# @pytest.fixture(scope="session", autouse=True)
# # def setup_bd():
# #     with engine_test.begin():
# #         #target_metadata.create_all(engine_test)
# #         metadata.create_all(engine_test)
# #         yield
# #         #target_metadata.drop_all(engine_test)
# #         #metadata.drop_all(engine_test)
#
#
# async def setup_bd():
#     async with engine_test.begin() as conn:
#         await conn.run_sync(metadata.create_all)
#     yield
