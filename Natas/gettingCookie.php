<?php

$data = array("showpassword"=>"yes", "bgcolor"=>"#ffffff"); //defines an array

function xor_encrypt($in) {
	$key = 'eDWo';
	$text = $in;
	$outText = '';
	
	// Iterate through each character
	for($i=0;$i<strlen($text);$i++) {
	$outText .= $text[$i] ^ $key[$i % strlen($key)];
	}
	
	return $outText;
}

echo base64_encode(xor_encrypt(json_encode($data)));
echo "\n";
?>
