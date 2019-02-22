import os
import glob
import datetime
import sys
import argparse

from robot.api import TestData

from templates import JINJA_TEMPLATE

from jinja2 import Template

from git import Repo, Git

from config import envs


def prepare_test_info(env):
    file_content = []
    file_directory = envs[env]['test_dir']
    file_pattern = envs[env]['file_pattern']
    file_type = envs[env]['file_type']
    if file_pattern:
        for pattern in file_pattern:
            file_content.extend(glob.glob(file_directory + pattern))
    else:
        file_content = glob.glob(file_directory + file_type)
    file_content = sorted(file_content)
    test_suites = []
    time_parsed = [datetime.datetime.now().strftime("%a, %d %b %Y"), datetime.datetime.now().strftime("%-I:%M:%S %p")]
    for test_file in file_content:
        suite_location = os.path.abspath(test_file)
        test_steps = TestData(source=suite_location)
        test_suites.append(test_steps)
    return test_suites, time_parsed


def checkout_repo(env, git_ssh_cmd):
    repo = envs[env]['repo']
    directory = env
    try:
        with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
            print('trying to clone...')
            Repo.clone_from(repo, directory)
    except Exception as e:
        print(e.message)
        print( 'repo already cloned, pulling...')
        my_repo = Repo(directory)
        my_repo.remotes.origin.pull()
        print('repo pulled')


def main():
    git_ssh_identity_file = os.path.expanduser('~/.ssh/id_rsa')
    # print git_ssh_identity_file
    git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file
    # print git_ssh_cmd

    parser = argparse.ArgumentParser(description='Process test suites. Uses REMOTE directories by DEFAULT.')
    parser.add_argument('-l', '--location', help='Uses LOCAL repository for processing tests', action='store_true')
    args = parser.parse_args()

    for env in envs.keys():
        if args.location:
            print('Processing LOCAL {} directories.'.format(env))
        else:
            print('Processing REMOTE {} repositories'.format(env))
            checkout_repo(env, git_ssh_cmd=git_ssh_cmd)

        test_suites, time_parsed = prepare_test_info(env)
        image_path = envs[env]['image_path']
        last_execution = ' at '.join(time_parsed)
        test_output = Template(JINJA_TEMPLATE).render(test_suites=test_suites, last_execution=last_execution, image_path=image_path)
        with open('{}_output.html'.format(env.lower()), 'w') as html_output:
            html_output.write(test_output.encode('UTF-8'))


if __name__ == '__main__':
    main()