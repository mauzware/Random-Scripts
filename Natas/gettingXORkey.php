<?php

$cookie=base64_decode('HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=');

function xor_encrypt($in) {
	$key = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));
	$text = $in;
	$outText = '';
	
	// Iterate through each character
	for($i=0;$i<strlen($text);$i++) {
	$outText .= $text[$i] ^ $key[$i % strlen($key)];
	}
	
	return $outText;
}

print xor_encrypt($cookie);
print "\n"
?>
	
