<?php
error_reporting(-1);
ini_set('display_errors', 'On');
$conn = mysqli_connect("localhost", "pse", "pse", "product_data");
$url = 'https://api.sendgrid.com/';
$user = 'username';
$pass = 'password';
$sql = "SELECT url,email,price FROM priceupdate";
$result = mysqli_query($conn, $sql);

while($row = mysqli_fetch_assoc($result)) 
{
$email=$row['email'];
$body="Currunt price of the your product ".$row['url']." is ".$row['price']." ";
$body1="Currunt price of the your product ".$row['url']." is ".$row['price']." ";
$params = array(
    'api_user'  => $user,
    'api_key'   => $pass,
    'to'        => $email,
    'subject'   => 'price update',
    'html'      => $body,
    'text'      => $body1,
    'from'      => 'vishal@vounyse.com',
  );


$request =  $url.'api/mail.send.json';

// Generate curl request
$session = curl_init($request);
// Tell curl to use HTTP POST
curl_setopt ($session, CURLOPT_POST, true);
// Tell curl that this is the body of the POST
curl_setopt ($session, CURLOPT_POSTFIELDS, $params);
// Tell curl not to return headers, but do return the response
curl_setopt($session, CURLOPT_HEADER, false);
// Tell PHP not to use SSLv3 (instead opting for TLS)
curl_setopt($session, CURLOPT_SSLVERSION, CURL_SSLVERSION_TLSv1_2);
curl_setopt($session, CURLOPT_RETURNTRANSFER, true);

// obtain response
$response = curl_exec($session);
curl_close($session);

}
?>
