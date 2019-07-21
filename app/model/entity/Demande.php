<?php
require_once("app/model/entity/utilisateur.php");

class Demande{
	private $id;
	private $objet;
	private $fichier;
	private $jeune;
	private $enseignant;
	private $status;
	private $confirmation;
	private $dateAjout;

	public function __construct($id, $objet, $fichier, $jeune, $enseignant, $status, $confirmation, $dateAjout){
		$this->id = $id;
		$this->objet = $objet;
		$this->fichier = $fichier;
		$this->jeune = $jeune;
		$this->enseignant = $enseignant;
		$this->status = $status;
		$this->confirmation = $confirmation;
		$this->dateAjout = $dateAjout;
	}

	public function getId(){return $this->id;}
	public function getObjet(){return $this->objet;}
	public function getFichier(){return $this->fichier;}
	public function getJeune(){return $this->jeune;}
	public function getEnseignant(){return $this->enseignant;}
	public function getStatus(){return $this->status;}
	public function getConfirmation(){return $this->confirmation;}
	public function getDateajout(){return $this->dateAjout;}

	public function setId($id){return $this->id = $id;}
	public function setObjet($objet){return $this->objet = $objet;}
	public function setFichier($fichier){return $this->fichier = $fichier;}
	public function setJeune($jeune){return $this->jeune = $jeune;}
	public function setEnseignant($enseignant){return $this->enseignant = $enseignant;}
	public function setStatus($status){return $this->status = $status;}
	public function setConfirmation($confirmation){return $this->confirmation = $confirmation;}
	public function setDateajout($dateAjout){return $this->dateAjout = $dateAjout;}
}
?>;
