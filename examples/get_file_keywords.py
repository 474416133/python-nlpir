#!/usr/bin/env python
#encoding: utf8

from PyNLPIR import *

if __name__ == '__main__':

    if init('../', Constants.CodeType.GBK_CODE):
        print 'NLPIR initialization succeed.'
    else:
        raise 'NLPIR initialization fail.'

    filename = './resources/text.txt'
    print get_file_keywords(filename)

    exit()
