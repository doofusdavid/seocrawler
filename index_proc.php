<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
if($_POST["login"]==="david" && $_POST["password"]==="oH5*kkokk!HqXV2D")
{
    $command = escapeshellcmd("/usr/bin/python3 ./bin/scraper.py --url " . $_POST["url"]);
    shell_exec($command);
    header("Location: results.php");
    exit();
}

