#!/bin/bash
source_loc=$1
target=$2

echo "-------- Backing up folder: $source_loc ---------"
echo "To Location: $target"


target_loc=${source_loc////_}
output=$target$target_loc
lftp -u sanchitml,Kickass19*\( -e "mirror -c -e $source_loc $output && exit" ftp://sanchitml.ipage.com/    
cd $target 
echo "Zipping Folder to: $target_loc.tar.gz"   
tar -czf "$target_loc.tar.gz" "$target_loc"
echo "Removing Folder: $target_loc"    
rm -r $target_loc    

echo "-------- Backup Complete: $source_loc ---------"