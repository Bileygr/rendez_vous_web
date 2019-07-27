<?php
require_once("conf/connection.php");
require_once("app/model/entity/Message.php");

class MessageDAO{
	public function insert($message){
		$connect = new Connect();
		$connection = $connect->connexion();

		$query = $connection->prepare("INSERT INTO message(utilisateurId, demandeId, message, dateAjout) VALUES(:utilisateurId, :demandeId, :message, NOW())");
		$result = $query->execute([
			"utilisateurId"=>$message->getUtilisateur()->getId(),
			"demandeId"=>$message->getDemande()->getId(),
			"message"=>$message->getMessage()
		]);

		$query = null;
		$connection = null;	
		return $result;
	}
}
?>