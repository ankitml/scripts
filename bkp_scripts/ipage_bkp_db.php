<?php

$Date = 'bkp_'.date('d-m-Y');//. '@'.date('h.i.s');
// Define the name of the backup directory
define('BACKUP_DIR', $Date) ; 


// Define  Database Credentials
define('HOST', 'sanchitml.ipagemysql.com' ) ; 
define('USER', 'bkp1' ) ; 
define('PASSWORD', 'bkp1' ) ; 


if (!file_exists(BACKUP_DIR)) mkdir(BACKUP_DIR , 0777) ;
if (!is_writable(BACKUP_DIR)) chmod(BACKUP_DIR , 0777) ; 


$nextLine = <<<msg
<br /> 
msg;

$DB_NAME = array(array('beta.fourtraxlifestyles','wrd_4b72nf253n'),
array('blog.rigvee','wrd_16onhol3g1'),
array('wiki.rigvee','mdw_nniolj3m7h'),
array('khetiking','wrd_kaibco4o7d'),
array('iank.it','wrd_4ji7kcncji'),
array('iank.it_jim','wrd_m5ilm3bmbd'));

// array('1.beta.fourtraxlifestyles','wrd_bb6bm17olg'),
// array('1fourtraxlifestyles','wrd_chdffch7o7'),
// array('2fourtraxlifestyles','wrd_onn5j24252'),
// array('3fourtraxlifestyles','wrd_ji45ngn3d2'),

echo "Number of Databases to be backup :-" .count($DB_NAME);
echo $nextLine ; 

echo "*****************************************************";
echo "<pre>                    BackUp started              </pre>";
echo "*****************************************************<br>";

for($index=0; $index<count($DB_NAME); $index++)
{
     /*
     Define the filename for the sql file
      If you plan to upload the  file to Amazon's S3 service , use only lower-case letters 
     */
      echo "..........Processing Db of ".$DB_NAME[$index][0]." that is ".$DB_NAME[$index][1]."...............<br>";
     
      $fileName = $DB_NAME[$index][0].'.sql' ; 
      // Set execution time limit . '@'.date('h.i.s').'
      /*  if(function_exists('max_execution_time')) 
      {
          if( ini_get('max_execution_time') > 0 )   set_time_limit(0) ;
      }
     */

     //echo "file name created"."\n";


     // Check if directory is already created and has the proper permissions


      $mysqli = new mysqli(HOST , USER , PASSWORD , $DB_NAME[$index][1]);
      if (mysqli_connect_errno())
      {
       echo "Can't not connect to database of ".$DB_NAME[$index][0]." that is ".$DB_NAME[$index][1];
       printf("Connect failed: %s", mysqli_connect_error());
       exit();
     }
     else
     {
      echo "Connected successfully to database  of :-".$DB_NAME[$index][0]." that is ".$DB_NAME[$index][1];
    }
    echo $nextLine ; 

       // Introduction information

    $return .= "--\n";
    $return .= "-- Database of : ".$DB_NAME[$index][0]." that is ".$DB_NAME[$index][1]."\n";
    $return .= "--\n";
    $return .= "--\n";
    $return .= "-- A Mysql Backup System \n";
    $return .= "--\n";
    $return .= '-- Export created: ' . date("Y/m/d") . ' on ' . date("h:i") . "\n\n\n";
    $return .= "-- --------------------------------------------------\n";
    $return .= "-- ---------------------------------------------------\n";
    $return .= 'SET AUTOCOMMIT = 0 ;' ."\n" ;
    $return .= 'SET FOREIGN_KEY_CHECKS=0 ;' ."\n" ;
    $tables = array() ; 
     // Exploring what tables this database has
    $result = $mysqli->query('SHOW TABLES' ) ; 
     // Cycle through "$result" and put content into an array

    while ($row = $result->fetch_row()) 
    {
      $tables[] = $row[0] ;
    }
     // Cycle through each  table
    foreach($tables as $table)
    {  

      $result = $mysqli->query('SELECT * FROM '. $table) ; 
      echo " Processing table - ".$table."(".mysqli_num_rows($result)." rows)\n\n";
      echo $nextLine ; 

    // Get number of fields (columns) of each table
      $num_fields = $mysqli->field_count;
    // Add table information
      $return .= "--\n" ;
      $return .= '-- Tabel structure for table `' . $table . '`' . "\n" ;
      $return .= "--\n" ;
      $return.= 'DROP TABLE  IF EXISTS `'.$table.'`;' . "\n" ; 
    // Get the table-shema
      $shema = $mysqli->query('SHOW CREATE TABLE '.$table) ;
    // Extract table shema 
      $tableshema = $shema->fetch_row() ; 
    // Append table-shema into code
      $return.= $tableshema[1].";" . "\n\n" ; 
    // Cycle through each table-row
      while($rowdata = $result->fetch_row()) 
      { 
             // Prepare code that will insert data into table 
        $return .= 'INSERT INTO `'.$table .'`  VALUES ( '  ;
            // Extract data of each row 
                // echo serialize($rowdata);
                // echo $nextLine;
         for($i=0; $i<$num_fields; $i++)
         {
          $return .= '"'.$rowdata[$i] . "\"," ;
            // echo '"'.$rowdata[$i] . "\",";
        }
            // Let's remove the last comma 
        $return = substr("$return", 0, -1) ; 
        $return .= ");" ."\n" ;
} 
$return .= "\n\n" ; 
}
          // Close the connection
$mysqli->close() ;
$return .= 'SET FOREIGN_KEY_CHECKS = 1 ; '  . "\n" ; 
$return .= 'COMMIT ; '  . "\n" ;
$return .= 'SET AUTOCOMMIT = 1 ; ' . "\n"  ; 
//$file = file_put_contents($fileName , $return) ; 
$zip = new ZipArchive() ;
$resOpen = $zip->open(BACKUP_DIR .'/' .$fileName.".zip" , ZIPARCHIVE::CREATE) ;
if( $resOpen )
{
 $zip->addFromString( $fileName , "$return" ) ;
}
$zip->close() ;

echo "..........Database with file name : ".$fileName."-has been generated..........";
echo $nextLine ; 
echo $nextLine ; 
}
