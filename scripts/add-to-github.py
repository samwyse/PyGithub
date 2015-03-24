'''\
Scan your local github directory for projects that are not in GitHub.
'''

from functools import partial
from os import chdir, getcwd, listdir
from os.path import isdir, isfile, join
from sys import path

chdir(r'C:\Users\dentos\Documents\GitHub')
path.append(join(getcwd(), 'PyGithub'))

from github import Github

put = partial(print, sep='\t')

userid = input('Enter your GitHub user id: ')
passwd = input('And your password: ') if userid else ''
if userid and passwd:
    g = Github(userid, passwd)
    for repo in g.get_user().get_repos():
        put(repo.name)
else:
    put('*** skipping GitHub access')

for dir in listdir('.'):
    if isfile(dir):
        put('file', dir)
    else:
        gitdir = join('.', dir, '.git')
        if isdir(gitdir):
            with open(join(gitdir, 'config')) as config:
                slurp = config.read()
            if '[remote ' in slurp:
                put('OK', dir)
            else:
                put('add', dir)
        else:
            put('miss', dir)
