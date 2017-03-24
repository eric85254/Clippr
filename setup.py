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
    try:
        shutil.rmtree(app + '/migrations')
    except:
        print("No " + app +'/migration')

try:
    os.remove('db.sqlite3')
except:
    print("No sqlite3 database.")

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
    'createDefaultHaircuts',
    'createDefaultShifts'
]

for command in commands:
    subprocess.call('python manage.py ' + command, shell=True)
