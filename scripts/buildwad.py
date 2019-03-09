#!/usr/bin/python

import argparse
import datetime
import sys
import os
import zipfile, zlib

def zipdir(inpath, outpath):
    zipf = zipfile.ZipFile(outpath, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(inpath):
        for file in files:
            currFile = os.path.join(root, file)
            relpath = os.path.relpath(currFile, inpath)
            print(currFile, relpath)
            zipf.write(currFile, relpath)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build a pk3 file out of an archive directory.')
    parser.add_argument('directory', metavar='directory', type=str, help='directory to build')
    parser.add_argument('-o', '--output', metavar='output', type=str, help='output filename (default: generate directory based on timestamp)', default=argparse.SUPPRESS)

    args = parser.parse_args()

    indirname = os.path.dirname(args.directory)

    if not os.path.isdir(args.directory):
        sys.exit("Target directory {} does not exist".format(args.directory))


    if not hasattr('args', 'output'):
        # autogenerate output file 
        odir = os.path.join('.','output/')
        if not os.path.isdir(odir):
            os.makedirs(odir)
        currentDT = datetime.datetime.now()
        DTformat = currentDT.strftime("%Y%m%d_%H%M%S")
        ofile = indirname + '_' + DTformat + '_rls.pk3'
        args.output = os.path.join(odir, ofile)

    print("Input dir set to " + args.directory)
    print("Output file set to " + args.output)

    print("Zipping directory {}...".format(args.directory))
    zipdir(args.directory, args.output)
