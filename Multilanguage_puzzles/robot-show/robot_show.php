<?php
fscanf(STDIN, "%d", $L);
fscanf(STDIN, "%d", $N);
$inputs = explode(" ", fgets(STDIN));
$arr = array();
for ($i = 0; $i < $N; $i++)
{
    $b = intval($inputs[$i]);
    $arr[] = $b;
}
error_log(var_export($arr, true));
$left = min($arr);
$right = max($arr);
$time = $L - min($left, $L - $right);
echo((string)$time);
?>