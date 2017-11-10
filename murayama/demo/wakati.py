# -*- coding: utf-8 -*-

import MeCab
import sys

tagger = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n')
#tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
#tagger = MeCab.Tagger('-d /opt/local/var/macports/sources/rsync.macports.org/macports/release/tarballs/ports/textproc/mecab-ipadic-neologd') 
#tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/ipadic')

fi = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'w')

line = fi.readline()
while line:
    result = tagger.parse(line)
    fo.write(result[1:]) # skip first \s
    line = fi.readline()

fi.close()
fo.close()
