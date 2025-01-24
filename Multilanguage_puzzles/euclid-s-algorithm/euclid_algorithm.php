<?php
fscanf(STDIN, "%d %d", $a, $b);

function gcd($a, $b){
    if ($b === 0){
        return $a;
    }
    $d = floor($a / $b);
    $r = $a % $b;
    echo("{$a}={$b}*{$d}+{$r}\n");
    return gcd($b, $a % $b);
}

$gcd = gcd($a, $b);
echo("GCD({$a},{$b})={$gcd}\n");
?>