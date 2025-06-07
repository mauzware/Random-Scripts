<?php
//$url = "CHANGE_THIS";
$url ="http://[IP]/";

$ENC_SECRET_KEY = "";
$payload = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~";
$parts_payload = str_split($payload,1);
//GET REQUEST FOR COOKIE
function get_cookie_from_url($url , $user_agent){
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch,CURLOPT_HEADER,true);
    curl_setopt($ch, CURLOPT_NOBODY,  true); 
    curl_setopt($ch, CURLOPT_USERAGENT,$user_agent);
    $response = curl_exec($ch);
    curl_close($ch);
    preg_match_all('/^Set-Cookie:\s*(.*)$/mi', $response, $matches);
    $cookie_array = [];
    if (!empty($matches[1])) {
        foreach ($matches[1] as $cookie) {
            $cookieParts = explode('=', $cookie, 2);
            $cookieValue = explode(';', $cookieParts[1])[0];
            $cookie_array[trim($cookieParts[0])] = trim($cookieValue) ;
        }
        return $cookie_array;
    } 
    return ;
}
//FLAG BRUTE FORCE
//$i = CHANGE_THIS;
for ($i=176 ; $i>0; $i--){
    if (substr($ENC_SECRET_KEY, -1) == "}" ){
        break;
    }
    $user_agent = str_repeat("i", $i );
    $cookie_array=get_cookie_from_url($url, $user_agent);
    $s_cookie= $cookie_array['secure_cookie'] ;
    $username = $cookie_array['user'];
    $c_string = $username.":".$user_agent.":".$ENC_SECRET_KEY;
    $c_octet_len = count(str_split($c_string,8));
    $parts_of_scookie = str_split(urldecode($s_cookie),13);
    $hash= $s_cookie[0]. $s_cookie[1];
    if(strlen($c_string) %8 == 7){
        $last7 = substr($c_string, -7);
    }
    foreach($parts_payload as $p){
        if ($parts_of_scookie[$c_octet_len - 1] == crypt($last7.$p, $hash)){
            echo "found: ". $p."\n";
            $ENC_SECRET_KEY .= $p;
            break; 
        }
    }
}
echo $ENC_SECRET_KEY ;
?>
