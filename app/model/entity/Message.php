<?php
class Message{
	private $id;
	private $utilisateur;
	private $demande;
	private $message;
	private $dateAjout;

	public function __construct($id, $utilisateurId, $demande, $message, $dateAjout){
		$this->id = $id;
		$this->utilisateurId = $utilisateurId;
		$this->demande = $demande;
		$this->message = $message;
		$this->dateAjout = $dateAjout;
	}

	public function getId(){return $this->id;}
	public function getUtilisateurid(){return $this->utilisateurId;}
	public function getDemande(){return $this->demande;}
	public function getMessage(){return $this->message;}
	public function getDateajout(){return $this->dateAjout;}

	public function setId($id){return $this->id = $id;}
	public function setUtilisateur($utilisateur){return $this->utilisateur = $utilisateur;}
	public function setDemande($demande){return $this->demande = $demande;}
	public function setMessage($message){return $this->message = $message;}
	public function setDateajout($dateAjout){return $this->dateAjout = $dateAjout;}
}
?>