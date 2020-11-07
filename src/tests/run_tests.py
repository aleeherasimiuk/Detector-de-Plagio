import os
import subprocess

GREEN_TICK = u'\033[92m' + u'\N{check mark}' + u'\033[0m'
RED_CROSS = u'\033[91m' + u'\N{Vector or Cross Product}' + u'\033[0m'


tests_path = 'src/tests/'
test_files = os.listdir(tests_path)
test_files.remove('module_fix.py')
test_files.remove('run_tests.py')
test_files.remove('__pycache__')
test_files.remove('firebase_tests.py')

tests = []
errors = []

for test in test_files:
  command = 'python src/tests/{} -v'.format(test)
  p = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out = p.stderr.read().decode('UTF-8').split('\n')
  
  for line in out:
    test = {}
    if 'test_' in line[:5]:
      splitted_line = line.split(' ')
      test_name = splitted_line[0][5:]
      test['test_name'] = test_name
      status = splitted_line[-1]
      test['status'] = True if 'ok' in status else False
      classname = splitted_line[1].replace('(__main__.', '').replace(')', '')
      test['classname'] = classname
      tests.append(test)

    elif '-' in line:
      continue
    elif 'Ran' in line:
      continue
    elif 'OK' in line:
      continue
    elif 'FAILED' in line:
      continue

    else:
      errors.append(line)

failed = 0
last_classname = ''
for test in sorted(tests, key=lambda k: k['classname']) :
  
  classname = test['classname']
  if classname != last_classname:
    print('\n')
    print(classname + ':')
    last_classname = classname

  status = test['status']
  if not status:
    failed += 1


  print('\t{}: {}'.format(test['test_name'], GREEN_TICK if status else RED_CROSS))


for error in errors:
  if error != r'\n' and error != '':
    print(error)

print('======================================================================')
print('')


print((u'\033[92m' + 'Test passed: {}' + u'\033[0m').format(len(tests) - failed))
print((u'\033[91m' + 'Test failed: {}' + u'\033[0m').format(failed))
    
 


