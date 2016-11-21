<?php
if(isset($_GET['id'])) {
    $id = $_GET["id"];
    $myfile = fopen("/var/www/html/voz_a_texto_v1.0/socket", "w") or die("No pude abrir el archivo!");
    fwrite($myfile, $id);
    fclose($myfile);
    header("Location: http://192.168.2.102/voz_a_texto_v1.0");
  die();
}
?>