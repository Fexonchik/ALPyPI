from os import system as oscomm
from sys import argv
check_pip = oscomm('pip')
check_pip3 = oscomm('pip3')
dir_here = argv[0]
if check_pip == 0:
  python_ver = '3'
else:
  python_ver = ''
def main():
  if check_pip == 0:
    oscomm('pip install setuptools twine')
  else:
    oscomm('pip3 install setuptools twine')
  
  oscomm('cd ' + dir +' && python' + python_ver + ' setup.py sdist && \
  python' + python_ver + ' -m twine upload dist/*')
  
main()
  
  





