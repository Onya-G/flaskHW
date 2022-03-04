import requests

#
# resp = requests.post('http://127.0.0.1:5051/users/',
#                      json={
#                          'username': 'test1',
#                          'password': 'sgdsppo34FET32325',
#                          'email': 'test1@test.test'
#                      }).json()
# print(resp)
#
# resp = requests.get('http://127.0.0.1:5051/users/1').json()
# print(resp)

resp = requests.post('http://127.0.0.1:5051/ads/',
                     json={
                         'title': 'title1',
                         'description': 'des1',
                         'owner': 1
                     }).json()
print(resp)

# resp = requests.get('http://127.0.0.1:5051/ads/1').json()
# # print(resp)
