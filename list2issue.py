#!/usr/bin/python

import os

import argparse as ap

from mailman.interfaces.messages import IMessageStore
from github3 import login

def main():
    description = """Turn a mailing list discussion into a Github issue"""
    parser = ap.ArgumentParser(description=description)

    disc = 'the url of the list discussion'
    parser.add_argument('disc', help=disc)

    repo = 'the url of the github repository'
    parser.add_argument('repo', help=repo)

    ghcred = 'the github credential file'
    parser.add_argument('--ghcred', default=os.path.expanduser('~/.ghcred'), 
                        help=ghcred)

    parser.parse_args()

if __name__ == "__main__":
    main()
