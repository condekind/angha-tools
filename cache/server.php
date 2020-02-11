<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json; charset=utf-8');

$input = file_get_contents('php://input');

$descriptorspec = array(
	0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
	1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
	2 => array("pipe", "w")   // stderr
);

$cwd = '/tmp';
$env = array();

$process = proc_open('python3 ./ncodesearch.py', $descriptorspec, $pipes, $cwd, $env);
if (is_resource($process)) {
	fwrite($pipes[0], $input);
	fclose($pipes[0]);
	$stdout = stream_get_contents($pipes[1]);
	$stderr = stream_get_contents($pipes[2]);
	fclose($pipes[1]);
	fclose($pipes[2]);

	// It is important that you close any pipes before calling
	// proc_close in order to avoid a deadlock
	$return_value = proc_close($process);

	if($return_value == 0) {
		echo $stdout;
	} else {
		http_response_code(500);
		echo $stderr;
	}
}

?>
