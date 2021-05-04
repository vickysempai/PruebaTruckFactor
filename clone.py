# https://stackoverflow.com/a/54992194
import os

def getRepo(repo_url, login_object):
  '''
  Clones the passed repo to my staging dir
  '''

  path_append = r"C:/TEC/VII Semestre/Proyecto/PythonGitData/Original" # Can set this as an arg 
  os.chdir(path_append)

  repo_moddedURL = 'https://' + repo_url[8:]
  os.system('git clone '+ repo_moddedURL)

  print('Cloned!')

getRepo('https://github.com/vickysempai/PruebaTruckFactor.git', {'username': 'sebassegurasoto', 'password': 'password'})