# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:14:23 2021

@author: ms2674
"""

import json
import sys
import getopt
import os



def transfer_fun(json_path,aps_dir,my_dir,date=''):
    with open(json_path, encoding="utf-16") as f:
        listDir = json.load(f)
    len_DATA = len(listDir['DATA'])
    size_list=[]
    with open('globus_transferDir.ps1', mode='a') as f:
        for i in range(len_DATA):
            size_list.append(listDir['DATA'][i]['size'])      
            fname = os.path.splitext(os.path.basename(listDir['DATA'][i]['name'][:-3]))[0]
            Arguments = ["globus"]               #globus path
            Arguments.append("transfer")         #transfer argument
            Arguments.append('--label "{}"'.format(fname))
            Arguments.append("--deadline {}".format(date))
            Arguments.append('$aps_id":/{}/{}"'.format(aps_dir,listDir['DATA'][i]['name']))
            Arguments.append('$my_id":~/{}/{}"\n'.format(my_dir,listDir['DATA'][i]['name'])) 
            #nTopCL call with arguments
            print(" ".join(Arguments))
            f.write(" ".join(Arguments))
            # output,error = subprocess.Popen(Arguments,stdout = subprocess.PIPE, 
            #            stderr= subprocess.PIPE).communicate()
            #Print the return messages
            # print(output.decode("utf-8"))
    print('Total size:',sum(size_list),'Number of files:', len(size_list))

# globus transfer $aps_id":/2-BM/2021-07/Sobhani/s25_3d_131.h5" $my_id":~/APS Tomography/s25_3d_131.h5"

if __name__ == '__main__':
    Date = ''
    aps_dir = ''
    my_dir = ''
    argv = sys.argv[1:]
    try:
        options, args = getopt.getopt(argv, "d:",["date ="])
    except:
        print('Error: bad input')
    for name, value in options:
        if name in ['-d','--date']:
            Date = value
    json_path = args[0]
    aps_dir = args[1]
    my_dir = args[2]
    transfer_fun(json_path, aps_dir, my_dir,date=Date)
    print(Date)
    print(options)
    print(args)