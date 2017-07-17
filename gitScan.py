#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""A script for scan git leakage"""
import argparse
import sys
import requests

SAVE_RESULT = open("git_domain.txt", "a")

def gitscan(filename):
    """test"""
    with open(filename, "r") as domains:
        for domain in domains.readlines():
            if not domain.startswith('http://'):
                domain = 'http://' +domain
            domain = domain.strip('\n')
            domain = domain + '/.git/config'
            try:
                check = requests.get(domain)
                if 'repositoryformatversion' in check.content:
                    print '[+] %s Githack' % format(domain)
                    SAVE_RESULT.write(domain+'\n')
                else:
                    print  '[-] %s None' % format(domain)
            except RuntimeError:
                pass
        SAVE_RESULT.close()

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description="A script for scan git leakage")
    PARSER.add_argument('-f', '--file', type=str, default=None, help="target domain file")
    ARGS = PARSER.parse_args()

    if ARGS.file is None:
        print '[*]Usage:python %s -f filename' % sys.argv[0]
        exit(0)
    gitscan(ARGS.file)
