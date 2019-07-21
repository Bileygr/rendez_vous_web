<?php 
require_once("app/Engine.php");
require_once("app/model/dao/DemandeDAO.php");
require_once("app/model/dao/UtilisateurDAO.php");
require_once("app/model/entity/Demande.php");
require_once("app/model/entity/Utilisateur.php");

class DefaultController{
	public function accueil(){
		$engine = new Engine();

		session_start();

		if(isset($_SESSION["utilisateur"])){
			$utilisateur = $_SESSION["utilisateur"];

			if($utilisateur->getRole() == "Élève"){
				$engine->render("accueil-jeune.html");
			}elseif ($utilisateur->getRole() == "Enseignant"){
				$engine->render("accueil-enseignant.html");
			}
		}else{
			$engine->render("accueil.html");
		}
	}

	public function connexion(){
		$engine = new Engine();
		$engine->render("connexion.html");

		if(isset($_POST["connexion"])){
			if(!empty($_POST["email"]) && !empty($_POST["motdepasse"])){
				$email = $_POST["email"];
				$motdepasse = $_POST["motdepasse"];

				$utilisateurDAO = new UtilisateurDAO;
				$utilisateurs = $utilisateurDAO->findBy("email", $email);

				if(password_verify($motdepasse, $utilisateurs[0]->getMotdepasse())){
					session_start();
					$_SESSION["utilisateur"] = $utilisateurs[0];

					header("Location: http://127.0.0.1/rendez_vous_web/accueil.php");
				}
			}
		}
	}

	public function deconnexion(){
		if(!isset($_SESSION)){
			session_start();
		}
		session_destroy();
		header("Location: http://127.0.0.1/rendez_vous_web/accueil.php");
	}

	public function inscription(){
		$engine = new Engine();
		$engine->render("inscription.html");

		if(isset($_POST["inscription"])){
			if(!empty($_POST["nom"]) && !empty($_POST["prenom"]) && !empty($_POST["motdepasse"]) && !empty($_POST["confirmationmotdepasse"]) && !empty($_POST["email"]) && !empty($_POST["telephone"]) && !empty($_POST["role"])){
				$nom = $_POST["nom"];
				$prenom = $_POST["prenom"];
				$motdepasse = $_POST["motdepasse"];
				$confirmationmotdepasse = $_POST["confirmationmotdepasse"];
				$email = $_POST["email"];
				$telephone = $_POST["telephone"];
				$role = $_POST["role"];

				if($motdepasse == $confirmationmotdepasse){
					if(filter_var($email, FILTER_VALIDATE_EMAIL)){
						if(strlen($telephone) == 10){
							$utilisateurDAO = new UtilisateurDAO;
							$utilisateur = new Utilisateur(null, $nom, $prenom, $role, null, $telephone, $email, null, null);
							$utilisateur->setMotdepasse($motdepasse);
							$userinsertion = $utilisateurDAO->insert($utilisateur);

							if($userinsertion){
								header("Location: http://127.0.0.1/rendez_vous_web/accueil.php");
							}else{
								echo "L'insertion de l'utilisateur dans la base de donnees a echoue.";
							}
						}else{
							echo "Le numero de telephone est trop court ou trop long.";
						}
					}else{
						echo "Le format de l'email est incorrecte.";
					}
				}else{
					echo "Les mots de passe ne correspondent pas.";
				}
			}else{
				echo "L'un des champs du formulaire est vide.";
			}
		}
	}

	public function liste_des_enseignants(){
		$engine = new Engine();

		$utilisateurDAO = new UtilisateurDAO;
		$utilisateurs = $utilisateurDAO->findBy("role", "Enseignant");

		$listedesenseignants = "";

		foreach ($utilisateurs as $utilisateur) {
			$listedesenseignants .= 
				"
					<tr>
            			<th>".$utilisateur->getId()."</th>
            			<td>".$utilisateur->getNom()."</td>
            			<td>".$utilisateur->getPrenom()."</td>
            			<td>".$utilisateur->getRole()."</td>
            			<td>".$utilisateur->getTelephone()."</td>
            			<td>".$utilisateur->getEmail()."</td>
            			<td>".$utilisateur->getDerniereconnexion()."</td>
            			<td>".$utilisateur->getDateajout()."</td>
          			</tr>
				";
		}

		$engine->assign("liste", $listedesenseignants);
		$engine->render("liste-des-enseignants.html");
	}

	public function liste_des_rendez_vous(){
		session_start();
		$utilisateur = $_SESSION["utilisateur"];
		$engine = new Engine();

		$demandeDAO = new DemandeDAO;
		$demandes = $demandeDAO->findBy("jeuneid", $utilisateur->getId());

		$listedesdemandes = "";

		foreach ($demandes as $demande) {
			$confirmation = "";

			if ($demande->getConfirmation() == 0){
				$confirmation = "Non";
			}elseif ($demande->getConfirmation() == 1) {
				$confirmation = "Oui";
			}

			$listedesdemandes .= 
				"
					<tr>
            			<th>".$demande->getId()."</th>
            			<td>".$demande->getObjet()."</td>
            			<td>".$demande->getFichier()."</td>
            			<td>".$demande->getEnseignant()->getNom()." ".$demande->getEnseignant()->getPrenom()."</td>
            			<td>".$demande->getStatus()."</td>
            			<td>".$confirmation."</td>
            			<td>".$demande->getDateajout()."</td>
          			</tr>
				";
		}

		$engine->assign("liste", $listedesdemandes);
		$engine->render("liste-des-rendez-vous.html");
	}

	public function modification_de_vos_informations(){
		session_start();
		$utilisateur = $_SESSION["utilisateur"];
		$engine = new Engine();
		$engine->assign("nom", $utilisateur->getNom());
		$engine->assign("prenom", $utilisateur->getPrenom());
		$engine->assign("email", $utilisateur->getEmail());
		$engine->assign("telephone", $utilisateur->getTelephone());
		$engine->render("modification-de-vos-informations.html");

		if(isset($_POST["modification"])){
			if(!empty($_POST["nom"]) && !empty($_POST["prenom"]) && !empty($_POST["email"]) && !empty($_POST["telephone"])){
				$nom = $_POST["nom"];
				$prenom = $_POST["prenom"];
				$email = $_POST["email"];
				$telephone = $_POST["telephone"];

				if(filter_var($email, FILTER_VALIDATE_EMAIL)){
					if(strlen($telephone) == 10){
						$utilisateur->setNom($nom);
						$utilisateur->setPrenom($prenom);
						$utilisateur->setEmail($email);
						$utilisateur->setTelephone($telephone);

						$utilisateurDAO = new UtilisateurDAO;
						
						if($utilisateurDAO->update($utilisateur)){
							$defaultcontroller = new DefaultController;
							$defaultcontroller->deconnexion();
						}else{
							echo "La mise a jour a echouee.";
						}
					}else{
						echo "La longeur du numero de telephone est incorrecte.";
					}
				}else{	
					echo "Le format de l'emaile est incorrecte.";
				}
			}
		}
	}
}
?>