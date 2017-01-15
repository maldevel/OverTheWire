<?php  

  $cookie = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw');  

  function xorme($plain) {  
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));  
    $cipher = '';  

    for($i=0;$i<strlen($plain);$i++) {  
      $cipher .= $plain[$i] ^ $key[$i % strlen($key)];  
    }  
   
    return $cipher;  
  }  

  print xorme($cookie);

