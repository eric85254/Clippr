import os
import shutil
import subprocess

apps_with_migrations = [
    'core',
    'stylist'
]

'''
    DELETE OLD MIGRATIONS && DATABASE
'''

for app in apps_with_migrations:
    shutil.rmtree(app + '/migrations')

os.remove('db.sqlite3')

'''
    RECREATE MIGRATIONS FOLDERS + DATABASE
'''

for app in apps_with_migrations:
    os.makedirs(app + '/migrations')
    open(app + '/migrations/__init__.py', 'w')

subprocess.call('python manage.py makemigrations', shell=True)
subprocess.call('python manage.py migrate', shell=True)

'''
    RUN ALL THE COMMANDS TO CREATE DEFAULT USERS AND ETC.
'''

commands = [
    'createDefaultUsers',
    'createGlobalMenuOption',
    'createDefaultAppointment',
    'createDefaultHaircuts'
]

for command in commands:
    subprocess.call('python manage.py ' + command, shell=True)
