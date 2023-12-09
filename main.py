import subprocess, os, sys, shutil
from xml.etree import ElementTree
from pathlib import Path

if len(sys.argv)<2:
    print('Run this script passing the path to the app\'s "res" folder as the argument.')
    exit()
apk_path=sys.argv[1]
if not os.path.isfile(apk_path):
    print(f'Path "{apk_path}" either does not exist, or is not a dir')
    exit()
apk_name=Path(apk_path).stem
tmp_path=f'./tmp_{apk_name}'

if os.path.exists(tmp_path):
    shutil.rmtree(tmp_path)

subprocess.run(['java', '-jar', './resources/apktool.jar', 'd', apk_path, '--no-src', '-o', tmp_path])
subprocess.run(['python', './resources/wearmodder.py', f'{tmp_path}/res'])
subprocess.run(['java', '-jar', './resources/apktool.jar', 'b', tmp_path, '-o', f'{apk_name}-w.apk'])
subprocess.run(['java', '-jar', './resources/uber-apk-signer.jar', '-a', f'{apk_name}-w.apk', '--overwrite'])

shutil.rmtree(tmp_path)