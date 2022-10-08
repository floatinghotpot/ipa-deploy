#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys, os, subprocess
from .version import __version__

sys.path.append(os.getcwd())

def exec_cmd(cmd, capture_output= False):
    #print(cmd)
    ret = subprocess.run( cmd, shell=True, capture_output= capture_output )
    return ret.returncode, ret.stdout.decode() if capture_output else ''

def cli_main_help():
    syntax_tips = '''Syntax:
    __argv0__ <path_to_ipa_file>

Example:
    __argv0__ app.ipa
'''.replace('__argv0__',os.path.basename(sys.argv[0]))

    print(syntax_tips)

def parse_params_options(argv):
    params = []
    options = []
    for i in range(1, len(argv)):
        str = argv[i]
        if str[0] == '-':
            options.append(str)
        else:
            params.append(str)

    return params, options

def confirm_installed( bin ):
    status, output = exec_cmd( 'which ' + bin )
    print(status, output)
    pass

def cli_main_params_options(params, options):
    if ('-v' in options) or ('--version' in options):
        print( __version__ )
        return

    if len(params) == 0:
        cli_main_help()
        return

    # confirm the IPA file exists
    ipa_file = os.path.abspath(params[0])
    if not os.path.exists(ipa_file):
        print('Error: ' + ipa_file + ' not exists')
        return

    # confirm the commands installed
    for bin in ['unzip', 'ios-deploy']:
        status, output = exec_cmd( 'which ' + bin, capture_output= True )
        if status != 0:
            print('Error: ' + bin + ' not found')
            if bin == 'ios-deploy':
                print('Please install ios-deploy via Homebrew by running:')
                print('  brew install ios-deploy')
            return

    # exec the commands
    cmds = [
        'rm -rf ./tmp',
        'mkdir ./tmp',
        'unzip "' + ipa_file + '" -d ./tmp',
        'ios-deploy -b ./tmp/Payload/*.app',
        'rm -rf ./tmp',
    ]
    for cmd in cmds:
        status, output = exec_cmd( cmd )
        if status != 0:
            print('Error: failed exec "' + cmd + '"')
            return

def cli_main():
    params, options = parse_params_options(sys.argv)
    cli_main_params_options(params, options)

if __name__ == "__main__":
    cli_main()
