<?php
class RDV{
	private $id;
	private $demande;
	private $date;
	private $dateAjout;

	public function __construct($id, $demande, $date, $dateAjout){
		$this->id = $id;
		$this->demande = $demande;
		$this->date = $date;
		$this->dateAjout = $dateAjout;
	}

	public function getId(){return $this->id;}
	public function getDemande(){return $this->demande;}
	public function getDate(){return $this->date;}
	public function getDateajout(){return $this->dateAjout;}

	public function setId($id){return $this->id = $id;}
	public function setDemande($demande){return $this->demande = $demande;}
	public function setDate($date){return $this->date = $date;}
	public function setDateajout($dateAjout){return $this->dateAjout = $dateAjout;}
}
?>