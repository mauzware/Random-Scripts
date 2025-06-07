<?php

$cookie = "pGrU6qDu0epOopGwG.ztylepwopGcL8j47VvjfspGq8.XcQA.qlApGAV0ASgKhWFApGVycaYH81JeApGD9LnfhScOCEpG48br.UgmQKspG4exPb2XH0w6pGI.C1JU8OWH.pGF5mAHUplDk2pG.dmapUrBygkpGjfDmkVJMtlIpGalu8RyY1ZhkpGs76e8wyDHYMpGVCxYiVJW5LkpGY2UMQb3DMpUpGTw2kevRD5f2pGQAb%2Fpmg1Q3YpGXpUplDQe7OspGuSqgUWN6mTEpGbufakrx394kpG3u.Hla%2FHIOMpGVYYoGXWgJ%2FQpG9Mh9dbBWCYcpGAYNH045UIdApGdoCLFXT63LspGfGGplqb3GU.pGEiEEWx2J5y6";


$salt = substr($cookie,0,2);

$text = "guest:Mo";
$guest_part = crypt($text, $salt);

$admin_text = "admin:Mo";
$admin_part = crypt($admin_text, $salt);


$modified_cookie = str_replace($guest_part, $admin_part, $cookie);

print($modified_cookie);

?>
