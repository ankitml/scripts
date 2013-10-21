#!/bin/sh

##easytar extract none filename_to_be_extracted
#to extract an uncompressed tar
tar -xvf $1

##easytar extract gz filename_to_be_extracted
#To extract a .gz archive:
tar -xzvf $1

##easytar extract bz2 filename_to_be_extracted
#To extract a .bz2 archive:
tar -xjvf $1


##easytar create bz2 filename_to_be_created.tgz file_or_directory_to_be_compressed
#To create a .bz2 archive:
tar -cjvf $1 $2

##easytar create gz filename_to_be_created.tgz file_or_directory_to_be_compressed
#To create a .gz archive:
tar -czvf $1 $2

