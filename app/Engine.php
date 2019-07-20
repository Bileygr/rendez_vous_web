<?php
class Engine{
	private $vars = array();

	public function assign($parameter, $value){
		$this->vars[$parameter] = $value;
	}

	public function render($view){
		$directory = "app/view/";
		if(file_exists($directory.$view)){
			$content = file_get_contents($directory.$view);
			
			foreach ($this->vars as $parameter => $value){
				$content = preg_replace("/\{\{\s".$parameter."\s\}\}/", $value, $content);
			}
			
			echo $content;
		}else{
			exit('<h1 style="color: red;">Erreur de template.</h1>');
		}
	}
}
?>