from os import system, getcwd
from sys import argv

class ArgumentNotFound(Exception):
  pass

try:
  argv[2]
except IndexError:
  build_wheel = False
else:
  if argv[2] == '--build-wheel':
    build_wheel = True
  elif argv[2] == '':
    build_wheel = False
  else:
    raise ArgumentNotFound('this argument is not present or it is not in this version')

check_pip = oscomm('pip')
check_pip3 = oscomm('pip3')
dir = getcwd()
if check_pip == 0:
  python_ver = ''
else:
  python_ver = '3'
def main():
  try:
    argv[2]
  except IndexError:
    build_wheel = False
  else:
    if argv[2] == '--build-wheel':
      build_wheel = True
    elif argv[2] == '':
      build_wheel = False
    else:
      raise ArgumentNotFound('this argument is not present or it is not in this version')
  
  oscomm('pip' + python_ver + ' install setuptools twine')
  if build_wheel:
    oscomm('cd ' + dir +' && python' + python_ver + ' setup.py sdist bdist_wheel && \
    python' + python_ver + ' -m twine upload dist/*')
  else:
    oscomm('cd ' + dir +' && python' + python_ver + ' setup.py sdist && \
    python' + python_ver + ' -m twine upload dist/*')

if __name__ == '__main__':
  main()
  
  





