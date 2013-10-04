#!/bin/bash
target_bkp="/home/bkp/"
tar_name="backup_ipage"
target="/tmp/$tar_name/"
# array of folders to be backup 
source_dir=( /backup_script/archive_03-10-2013)

echo "********************************"
echo "       GRAND BACKUP STARTS"
echo "********************************"
d=$(date +-%Y-%m-%d)
for source_loc in ${source_dir[*]}
do  
    ./ipage_bkp_folder.sh "$source_loc" "$target"
done
cd "/tmp/"
echo "Zipping Folder to: $tar_name$d.tar.gz"   
tar -czf "$tar_name$d.tar.gz" "$tar_name"
echo "Removing Folder: $tar_name" 
rm -r $tar_name
echo "Moving '$tar_name$d.tar.gz' to  '$target_bkp'" 
mv "$tar_name$d.tar.gz" "$target_bkp"
echo "********************************"
echo "       GRAND BACKUP FINISHES"
echo "********************************"


