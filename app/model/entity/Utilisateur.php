<?php
class Utilisateur{
	private $id;
	private $nom;
	private $prenom;
	private $role;
	private $motdepasse;
	private $telephone;
	private $email;
	private $derniereConnexion;
	private $dateAjout;

	function __construct($id, $nom, $prenom, $role, $motdepasse, $telephone, $email, $derniereConnexion, $dateAjout){
		$this->id = $id;
		$this->nom = $nom;
		$this->prenom = $prenom;
		$this->role = $role;
		$this->motdepasse = $motdepasse;
		$this->telephone = $telephone;
		$this->email = $email;
		$this->derniereConnexion = $derniereConnexion;
		$this->dateAjout = $dateAjout;
	}

	public function getId(){return $this->id;}
	public function getNom(){return $this->nom;}
	public function getPrenom(){return $this->prenom;}
	public function getRole(){return $this->role;}
	public function getMotdepasse(){return $this->motdepasse;}
	public function getTelephone(){return $this->telephone;}
	public function getEmail(){return $this->email;}
	public function getDerniereconnexion(){return $this->derniereConnexion;}
	public function getDateajout(){return $this->dateAjout;}

	public function setId($id){return $this->id = $id;}
	public function setNom($nom){return $this->nom = $nom;}
	public function setPrenom($prenom){return $this->prenom = $prenom;}
	public function setRole($role){return $this->role = $role;}
	public function setMotdepasse($motdepasse){return $this->motdepasse = $motdepasse;}
	public function setTelephone($telephone){return $this->telephone = $telephone;}
	public function setEmail($email){return $this->email = $email;}
	public function setDerniereconnexion($derniereConnexion){return $this->derniereConnexion = $derniereConnexion;}
	public function setDateajout($dateAjout){return $this->dateAjout = $dateAjout;}
}
?>