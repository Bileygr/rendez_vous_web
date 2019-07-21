<?php
require_once("conf/connection.php");

class UtilisateurDAO{
	public function findAll(){
		$connect = new Connect;
		$bdd = $connect->connexion();
		$requete = $bdd->prepare("SELECT * FROM utilisateur");
		$requete->execute();

		$utilisateurs = array();
		for($i=0; $utilisateur=$requete->fetch(); $i++){
			$utilisateurs[$i] = new Utilisateur(
				$utilisateur['id'],
				$utilisateur['nom'],
				$utilisateur['prenom'],
				$utilisateur['role'],
				$utilisateur['motdepasse'],	
				$utilisateur['telephone'],
				$utilisateur['email'],
				$utilisateur['derniereConnexion'],
				$utilisateur['dateAjout']
			);
		}

		return $utilisateurs;
	}

	public function findBy($option, $value){
		$connect = new Connect();
		$connection = $connect->connexion(); 
		$query;

		switch($option){
			case "id":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE id = :value");
				break;
			case "nom":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE nom = :value");
				break;
			case "prenom":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE prenom = :value");
				break;
			case "motdepasse":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE motdepasse = :value");
				break;
			case "role":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE role = :value");
				break;
			case "telephone":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE telephone = :value");
				break;
			case "email":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE email = :value");
				break;
			case "derniereconnexion":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE derniereConnexion = :value");
				break;
			case"dateajout":
				$query = $connection->prepare("SELECT * FROM utilisateur WHERE dateAjout = :value");
				break;
		}
		$query->execute(array("value" => $value));

		$utilisateurs = array();
		for($i=0; $utilisateur=$query->fetch(); $i++){
			$utilisateurs[$i] = new Utilisateur(
				$utilisateur['id'],
				$utilisateur['nom'],
				$utilisateur['prenom'],
				$utilisateur['role'],
				$utilisateur['motdepasse'],	
				$utilisateur['telephone'],
				$utilisateur['email'],
				$utilisateur['derniereConnexion'],
				$utilisateur['dateAjout']
			);
		}

		$query = null;
		$connection = null;	
		return $utilisateurs;
	}

	public function insert($utilisateur){
		$connect = new Connect();
		$connection = $connect->connexion(); 

		$query = $connection->prepare("INSERT INTO utilisateur(nom, prenom, role, motdepasse, telephone, email, derniereConnexion, dateAjout) 
			VALUES(:nom, :prenom, :role, :motdepasse, :telephone, :email, NOW(), NOW())");
		$result = $query->execute(
			[
				"nom"=>$utilisateur->getNom(), 
				"prenom"=>$utilisateur->getPrenom(), 
				"role"=>$utilisateur->getRole(), 
				"motdepasse"=>$utilisateur->getMotdepasse(), 
				"telephone"=>$utilisateur->getTelephone(), 
				"email"=>$utilisateur->getEmail()
			]
		);

		$query = null;
		$connection = null;	
		return $result;
	}

	public function update($utilisateur){
		$connect = new Connect();
		$connection = $connect->connexion(); 

		$query = $connection->prepare("UPDATE utilisateur SET nom = :nom, prenom = :prenom, role = :role, motdepasse = :motdepasse, telephone = :telephone, email = :email, derniereConnexion = NOW() WHERE id = :id");
		$result = $query->execute(
			[
				"nom"=>$utilisateur->getNom(), 
				"prenom"=>$utilisateur->getPrenom(), 
				"role"=>$utilisateur->getRole(), 
				"motdepasse"=>$utilisateur->getMotdepasse(), 
				"telephone"=>$utilisateur->getTelephone(), 
				"email"=>$utilisateur->getEmail(),
				"id"=>$utilisateur->getId()
			]
		);

		$query = null;
		$connection = null;	
		return $result;
	}
}
?>