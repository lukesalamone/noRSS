<?php

	$to = "YOUR EMAIL ADDRESS HERE";

	$website = $argv[1];
	$from = "noRSS@test.com";
	$subject = 'test subject';
	$message = "Update detected on $website";
	$headers = "From: $from" . "\r\n" .
		"Reply-To: $from" . "\r\n" .
		'X-Mailer: PHP/' . phpversion();

	mail($to, $subject, $message, $headers);
?> 
