<?php
require_once("conf/connection.php");
require_once("app/model/entity/Demande.php");

class DemandeDAO{
	public function delete($demande){
		$connect = new Connect();
		$connection = $connect->connexion();

		$query = $connection->prepare("DELETE FROM demande WHERE id = :id");
		$result = $query->execute(["id"=>$demande->getId()]);

		$query = null;
		$connection = null;	
		return $result;
	}

	public function findAll(){
		$connect = new Connect();
		$connection = $connect->connexion();

		$query = $connection->prepare("SELECT b.id AS 'demande-id', b.objet AS 'demande-objet', b.fichier AS 'demande-fichier', b.jeuneId AS 'demande-jeuneid', b.enseignantId AS 'demande-enseignantid', b.status AS 'demande-status', b.confirmation AS 'demande-confirmation', b.dateAjout AS 'demande-dateajout', a.id AS 'jeune-id', a.nom AS 'jeune-nom', a.prenom AS 'jeune-prenom', a.motdepasse AS 'jeune-motdepasse', a.role AS 'jeune-role', a.email AS 'jeune-email', a.telephone AS 'jeune-telephone', a.derniereConnexion AS 'jeune-derniereconnexion', a.dateAjout AS 'jeune-dateajout' , c.id  AS 'enseignant-id', c.nom AS 'enseignant-nom', c.prenom AS 'enseignant-prenom', c.motdepasse AS 'enseignant-motdepasse', c.role AS 'enseignant-role', c.email AS 'enseignant-email', c.telephone AS 'enseignant-telephone', c.derniereConnexion AS 'enseignant-derniereconnexion', c.dateAjout AS 'enseignant-dateajout' FROM demande b JOIN utilisateur a ON b.jeuneId=a.id JOIN utilisateur c ON b.enseignantId=c.id");
		$query->execute();

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
				$demande['demande-fichier'],
				$jeune,
				$enseignant,
				$demande['demande-status'],
				$demande['demnande-confirmation'],	
				$demande['demande-dateajout']
			);
		}

		$query = null;
		$connection = null;	
		return $demandes;
	}

	public function findBy($option, $value){
		$connect = new Connect();
		$connection = $connect->connexion(); 
		$query;

		$firstpartofquery = "SELECT b.id AS 'demande-id', b.objet AS 'demande-objet', b.fichier AS 'demande-fichier', b.jeuneId AS 'demande-jeuneid', b.enseignantId AS 'demande-enseignantid', b.status AS 'demande-status', b.confirmation AS 'demande-confirmation', b.dateAjout AS 'demande-dateajout', a.id AS 'jeune-id', a.nom AS 'jeune-nom', a.prenom AS 'jeune-prenom', a.motdepasse AS 'jeune-motdepasse', a.role AS 'jeune-role', a.email AS 'jeune-email', a.telephone AS 'jeune-telephone', a.derniereConnexion AS 'jeune-derniereconnexion', a.dateAjout AS 'jeune-dateajout' , c.id  AS 'enseignant-id', c.nom AS 'enseignant-nom', c.prenom AS 'enseignant-prenom', c.motdepasse AS 'enseignant-motdepasse', c.role AS 'enseignant-role', c.email AS 'enseignant-email', c.telephone AS 'enseignant-telephone', c.derniereConnexion AS 'enseignant-derniereconnexion', c.dateAjout AS 'enseignant-dateajout' FROM demande b JOIN utilisateur a ON b.jeuneId=a.id JOIN utilisateur c ON b.enseignantId=c.id";

		switch($option){
			case "id":
				$query = $connection->prepare($firstpartofquery." WHERE b.id = :value");
				break;
			case "objet":
				$query = $connection->prepare($firstpartofquery." WHERE b.objet = :value");
				break;
			case "fichier":
				$query = $connection->prepare($firstpartofquery." WHERE b.fichier = :value");
				break;
			case "jeuneid":
				$query = $connection->prepare($firstpartofquery." WHERE b.jeuneId = :value");
				break;
			case "enseignantid":
				$query = $connection->prepare($firstpartofquery." WHERE b.enseignantId = :value");
				break;
			case "status":
				$query = $connection->prepare($firstpartofquery." WHERE b.status = :value");
				break;
			case "confirmation":
				$query = $connection->prepare($firstpartofquery." WHERE b.confirmation = :value");
				break;
			case "dateajout":
				$query = $connection->prepare($firstpartofquery." WHERE b.dateAjout = :value");
				break;
		}
		$query->execute(array("value" => $value));

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
}
?>