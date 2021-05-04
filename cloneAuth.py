import os

def getRepoAuth(repo_url, login_object):
  '''
  Clones the passed repo to my staging dir
  '''

  path_append = r"/home/usuario/Projects/truckFactor/pruebas/" # Can set this as an arg 
  os.chdir(path_append)

  repo_moddedURL = 'https://' + login_object['username'] + ':' + login_object['password'] + '@' + repo_url[8:]
  os.system('git clone '+ repo_moddedURL)

  print('Cloned!')

getRepoAuth('https://github.com/UserName/RepoYouWant.git', {'username': 'userName', 'password': 'passWord'})