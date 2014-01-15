<html>
<head>

  <style type="text/css">
    table {
      border-collapse: collapse;
    }        
    td {
      border: 1px solid black;
      padding: 0 0.5em;
    }        
  </style>  

  <?php

  if (isset($_POST["submit"])){ 
    $values = $_POST['result'];
    foreach($values as $v)
      echo $v."<br>";
  }

  elseif (isset($_POST["upl_file"])){
    $target_path = "/var/www/excel_reader/uploads/";
    $target_path = $target_path .$_FILES['uploadedfile']['name'];

    if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path))
      echo "The file ".  basename( $_FILES['uploadedfile']['name'])." has been uploaded.<br>";
    else
      echo "There was an error uploading the file, please try again!";
    

    include 'reader.php';
    $excel = new Spreadsheet_Excel_Reader();
    $excel->read($_FILES['uploadedfile']['name']);  
    echo "file content";
    echo "<form method='POST'><table>";

    $x=1;
    $a = array();
    while($x<=$excel->sheets[0]['numRows']) {
      $order = isset($excel->sheets[0]['cells'][$x][1]) ? $excel->sheets[0]['cells'][$x][1] : '';
      $track = isset($excel->sheets[0]['cells'][$x][2]) ? $excel->sheets[0]['cells'][$x][2] : '';

      echo "\t<tr>\n<td>".$order."</td><td>".$track."</td></tr>";
      if($x!=1)
        echo '<input type="hidden" name="result[]" value="'.$order."|".$track.'">';
      $x++;
    }
    echo '</table><br/><input type="submit" value="confirm" name="submit" />';   
  }  

  else {
    ?>
    <h3>File Upload:</h3>
    Select a file to upload: <br />
    <form action="file_uploader.php" method="post"
    enctype="multipart/form-data">
    <input type="file" name="uploadedfile" size="50" />
    <br />
    <input type="submit" value="Upload File" name ="upl_file"/>
  </form>
  <?php
}

?>
</form>
</body>
</html>


