from requests import post
from yaml import load, Loader
from os.path import exists, isdir, normpath
from os import listdir
from sys import argv
from glob import glob
from datetime import datetime
from zipfile import ZipFile

if '--nocolor' in argv:
    RED = ''
    BLUE = ''
    GREEN = ''
    RESET = ''
else:
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    RESET = '\033[0m'

if not exists('submit.yml'):
    print(f'{RED}"submit.yml" do not exists{RESET}')
    exit(1)

with open('submit.yml', mode='r', encoding='utf8') as f:
    config = load(f, Loader=Loader)

rel_files = []
for each in config['upload_files']:
    rel_files += [normpath(f) for f in glob(each)]
rel_files = list(set(rel_files))

print(f'{GREEN}Creating zip file{RESET}')

with ZipFile('upload.zip', mode='w') as zf:
    for file in rel_files:
        if file == 'upload.zip':
            continue
        if isdir(file):
            for dir_file in listdir(file):
                print(f'- {file}/{dir_file}')
                zf.write(f'{file}/{dir_file}')
        print(f'- {file}')
        zf.write(file)

now = datetime.now().strftime("%Y-%m-%d %T")
print(f'{GREEN}Uploading...{RESET}')
resp = post(config['url'], files={'file': open('upload.zip', mode='rb')}, data={
    'key': config['key'], 'lesson': config['lesson_id']
})
resp.raise_for_status()
jd = resp.json()
if jd['code']:
    print(f'{RED}Error({jd["code"]}): {jd["msg"]}{RESET}')
else:
    print(f'{GREEN}Submit successfully{RESET}')
