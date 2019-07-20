<?php 
require_once("app/Engine.php");

class DefaultController{
	public function index(){
		$engine = new Engine();
		$engine->render("index.html");
	}

	public function inscription(){
		$engine = new Engine();
		$engine->render("inscription.html");
	}

	public function connexion(){
		$engine = new Engine();
		$engine->render("connexion.html");
	}
}
?>