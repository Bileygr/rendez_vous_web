<?php
class Connect{
	public function connexion(){
		$host = "127.0.0.1";
		$port = "3306";
		$db = "rendez_vous";
		$user = "root";
		$password = "";

		try{
			$database = new PDO("mysql:host=".$host.";port=".$port.";dbname=".$db.";charset=utf8", $user, $password);
		}catch(Exception $e){
			echo "Échec lors de la connexion à la base de données: ".$e->getMessage();
		}
		
		return $database;
	}
}
?>