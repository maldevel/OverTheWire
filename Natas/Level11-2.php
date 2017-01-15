<?php  

  function xorme() {  
    $plain = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));  
    $key = 'qw8J';
    $cipher = '';  

    for($i=0;$i<strlen($plain);$i++) {  
      $cipher .= $plain[$i] ^ $key[$i % strlen($key)];  
    }  
   
    return base64_encode($cipher);  
  }  

  print xorme();

