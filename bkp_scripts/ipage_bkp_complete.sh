#!/bin/bash
target_bkp="/home/bkp/"
tar_name="backup_ipage"
target="/tmp/$tar_name/"
# array of folders to be backup 
source_dir=( /backup_script  /fl /hky /iank.it /rigvee)
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


# source_dir=(/192.241.234.155 /agrinnovate /apps.sanch.it-redirect /backup_script /cgi-bin /contctus /dewacademy /endoillu /energyshire /epinx /fl /forfreelancers /hky /iank.it /jhinga /rigvee /rs /saanp /saanpnew /sanchit /ssl /stats /try.sanch.it-redirect /way2l /wayl /wayl2 /waylalpha /.htaccess /404.html /Home.html /index.html /rs.zip)
