# import requests
# import pytest
# import pandas as pd
#
#
# class APIMethods:
#
#     def post_api(self, url, headers, payload):
#         resp = requests.post(url, headers, payload)
#         return resp
#
#
# class DataUtilities:
#     def read_excel(self, filename, sheetname):
#         df = pd.read_excel(filename, sheetname)
#         return df
#
#
# class TestAPI:
#     url = "https://xyz.com/user"
#     headers = {"content-type": "application/json", "x-cookie": "fdsflsdf"}
#
#     data_obj = DataUtilities()
#     data = data_obj.to_dict()
#
#     @pytest.parametrize(username, password, email, (data['username'], data['password'], data['email']))
#     def test_user_creation(self):
#         obj = APIMethods()
#         payload = {"username": ", "password":"pwd1", "email":"sai @ gmail.com"}
#                    resp = obj.post_api(self.url, self.headers, self.payload)
#         assert resp.status_code == 201, "user creation post api is failed"
#         resp = resp.json()
#         assert resp["username"] == "user1", "user creation is failed"
#
#         ```
#
# def get_second_large(l):
#
#     for i in range(len(l)):
#         for j in range(0, len(l) - i - 1):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     return l[-2]
#
#
# l = [2, 4, 44, 23, 54, 26]
# print(get_second_large(l))
#
# from abc import ABC, abstractmethod
#
#
# class CandidateSelection(ABC):
#
#     @abstractmethod
#     def interview_level(self):
#         pass
#
#
# class Interview(CandidateSelection):
#     id = 1
#     _cmpy = "asc"
#     __result = None
#
#     def __init__(self, interviewer, candidate):
#         self.interiewer = interviewer
#         self.candidate = candidate
#
#     def interview_level(self):
#         print("interview 1")
#
#
# class Selection(Interview):
#
#     def interview_status(self):
#         print("interview status")
#
#     def interview_level(self):
#         print("interview level from Selection class")
#
#
# obj = Selection('A', 'B')
# obj.interview_level()
# obj.interview_status()
#
# ```