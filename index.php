<?php

$temp = shell_exec("curl -G 'http://192.168.9.15:8086/query?pretty=true' --data-urlencode \"db=TempHumid\" --data-urlencode \"q=SELECT last(\"value\") FROM \"temperature\" WHERE \"room\"='outside'\"");
$json_temp = json_decode($temp, true);
$temp = $json_temp["results"][0]["series"][0]["values"][0][1];

header('Content-Type: application/json;');
$now = new DateTime();
$timezone = new DateTimeZone('America/Detroit');
$now->setTimezone($timezone);

$time = $now->format('h:i a');
$just_time = $now->format('h:i');
$am_pm = $now->format('a');
$day = $now->format('D');
$date = $now->format('m-d-Y');
$mysql = $now->format('Y-m-d H:i:s');
$unix =  $now->getTimestamp();

$response = array();
$response[0] = array(
        'outdoor_temp'=> $temp,
        'time'=> $time,
        'just_time'=> $just_time,
        'am_pm'=> $am_pm,
        'day'=> $day,
        'date'=> $date,
        'mysql'=> $mysql,
        'unix'=> $unix
);

echo json_encode($response);
?>
