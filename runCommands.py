import subprocess

subprocess.call('python manage.py makemigrations', shell=True)
subprocess.call('python manage.py migrate', shell=True)

commands = [
    'createDefaultUsers',
    'createGlobalMenuOption',
    'createDefaultAppointment',
    'createDefaultHaircuts'
]

for command in commands:
    subprocess.call('python manage.py ' + command, shell=True)