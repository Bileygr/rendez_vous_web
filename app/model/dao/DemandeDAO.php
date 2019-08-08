<?php
require_once("conf/connection.php");
require_once("app/model/entity/Demande.php");

class DemandeDAO{
	public function delete($demande){
		$connect = new Connect();
		$connection = $connect->connexion();

		$query = $connection->prepare("
			DELETE FROM message WHERE demandeId = :id;	
			DELETE FROM demande WHERE id = :id;
		");
		$result = $query->execute(["id"=>$demande->getId()]);

		$query = null;
		$connection = null;	
		return $result;
	}

	public function findBy($option, $value){
		$connect = new Connect();
		$connection = $connect->connexion(); 
		$query;

		$firstpartofquery = "SELECT a.id AS 'demande-id', a.objet AS 'demande-objet', a.date AS 'demande-date', a.fichier AS 'demande-fichier', a.jeuneId AS 'demande-jeuneid', a.enseignantId AS 'demande-enseignantid', a.status AS 'demande-status', a.confirmation AS 'demande-confirmation', a.dateAjout AS 'demande-dateajout', b.id AS 'jeune-id', b.nom AS 'jeune-nom', b.prenom AS 'jeune-prenom', b.motdepasse AS 'jeune-motdepasse', b.role AS 'jeune-role', b.email AS 'jeune-email', b.telephone AS 'jeune-telephone', b.derniereConnexion AS 'jeune-derniereconnexion', b.dateAjout AS 'jeune-dateajout' , c.id  AS 'enseignant-id', c.nom AS 'enseignant-nom', c.prenom AS 'enseignant-prenom', c.motdepasse AS 'enseignant-motdepasse', c.role AS 'enseignant-role', c.email AS 'enseignant-email', c.telephone AS 'enseignant-telephone', c.derniereConnexion AS 'enseignant-derniereconnexion', c.dateAjout AS 'enseignant-dateajout' FROM demande a JOIN utilisateur b ON a.jeuneId=b.id JOIN utilisateur c ON a.enseignantId=c.id";

		switch($option){
			case "":
				$query = $connection->prepare($firstpartofquery);
				$query->execute();
				break;

			case "id":
				$query = $connection->prepare($firstpartofquery." WHERE a.id = :value");
				$query->execute(["value" => $value]);
				break;
			case "objet":
				$query = $connection->prepare($firstpartofquery." WHERE a.objet = :value");
				$query->execute(["value" => $value]);
				break;
			case "fichier":
				$query = $connection->prepare($firstpartofquery." WHERE a.fichier = :value");
				$query->execute(["value" => $value]);
				break;
			case "jeuneid":
				$query = $connection->prepare($firstpartofquery." WHERE a.jeuneId = :value");
				$query->execute(["value" => $value]);
				break;
			case "enseignantid":
				$query = $connection->prepare($firstpartofquery." WHERE a.enseignantId = :value");
				$query->execute(["value" => $value]);
				break;
			case "status":
				$query = $connection->prepare($firstpartofquery." WHERE a.status = :value");
				$query->execute(["value" => $value]);
				break;
			case "confirmation":
				$query = $connection->prepare($firstpartofquery." WHERE a.confirmation = :value");
				$query->execute(["value" => $value]);
				break;
			case "dateajout":
				$query = $connection->prepare($firstpartofquery." WHERE a.dateAjout = :value");
				$query->execute(["value" => $value]);
				break;
			case "latest":
				$query = $connection->prepare($firstpartofquery." WHERE a.jeuneId = :value ORDER BY a.dateAjout DESC LIMIT 1");
				$query->execute(["value" => $value]);
				break;
		}

		$demandes = array();
		for($i=0; $demande=$query->fetch(); $i++){
			$jeune = new Utilisateur(
				$demande['jeune-id'],
				$demande['jeune-nom'],
				$demande['jeune-prenom'],
				$demande['jeune-role'],
				$demande['jeune-motdepasse'],
				$demande['jeune-telephone'],
				$demande['jeune-email'],
				$demande['jeune-derniereconnexion'],
				$demande['jeune-dateajout']
			);

			$enseignant = new Utilisateur(
				$demande['enseignant-id'],
				$demande['enseignant-nom'],
				$demande['enseignant-prenom'],
				$demande['enseignant-role'],
				$demande['enseignant-motdepasse'],
				$demande['enseignant-telephone'],
				$demande['enseignant-email'],
				$demande['enseignant-derniereconnexion'],
				$demande['enseignant-dateajout']
			);

			$demandes[$i] = new Demande(
				$demande['demande-id'],
				$demande['demande-objet'],
				$demande['demande-date'],
				$demande['demande-fichier'],
				$jeune,
				$enseignant,
				$demande['demande-status'],
				$demande['demande-confirmation'],	
				$demande['demande-dateajout']
			);
		}

		$query = null;
		$connection = null;	
		return $demandes;
	}

	public function insert($demande){
		$connect = new Connect();
		$connection = $connect->connexion(); 
		
		$query = $connection->prepare("INSERT INTO demande(objet, date, fichier, jeuneId, enseignantId, status, confirmation, dateAjout) VALUES(:objet, :date, :fichier, :jeuneId, :enseignantId, :status, :confirmation, NOW())");
		$result = $query->execute(
			[
				"objet"=>$demande->getObjet(),
				"date"=>$demande->getDate(),
				"fichier"=>$demande->getFichier(),
				"jeuneId"=>$demande->getJeune()->getId(),
				"enseignantId"=>$demande->getEnseignant()->getId(),
				"status"=>"En attente",
				"confirmation"=>0
			]
		);

		$query = null;
		$connection = null;	
		return $result;
	}
}
?>