# import os
# import tempfile
#
# import pytest
#
# from myapp import app
# from configmodule import TestingConfig
#
# @pytest.fixture
# def client():
#     app.config.from_object(TestingConfig)
#
#     with app.test_client() as client:
#         with app.app_context():
#             app.db.create_all()
#         yield client
#     app.db.delete()
