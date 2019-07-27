<?php
require_once("conf/connection.php");
require_once("app/model/entity/Demande.php");
require_once("app/model/entity/RDV.php");

class RDVDAO{
	public function insert($rdv){
		$connect = new Connect;
		$connection = $connect->connexion();

		$query = $connection->prepare("INSERT INTO rdv(demandeId, date, dateAjout) VALUES(:demandeId, :date, NOW())");
		$result = $query->execute(["demandeId"=>$rdv->getDemande()->getId(), "date"=>$rdv->getDate()]);

		$query = null;
		$connection = null;
		return $result;
	}
}
?>