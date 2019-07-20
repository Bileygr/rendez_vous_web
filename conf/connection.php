<?php
class Connect{
	public function connexion(){
		$settings = parse_ini_file("settings.ini", true);

		try{
			$database = new PDO("mysql:host=".$settings["database"]["host"].";port=".$settings["database"]["port"].";dbname=".$settings["database"]["database"].";charset=utf8", $settings["database"]["user"], $settings["database"]["password"]);
		}catch(Exception $e){
			echo "Échec lors de la connexion à la base de données: ".$e->getMessage();
		}
		
		return $database;
	}
}
?>