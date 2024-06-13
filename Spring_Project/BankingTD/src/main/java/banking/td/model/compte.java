package banking.td.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;

@AllArgsConstructor
@Entity
public class compte {
	@Id
	Long numCompte;
	double solde;
	

//}
//import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.RestController;
//
//@RestController
//public class TestController {
//@GetMapping("accueil")
//public String accueil() {
//	return "Accueil";
//}
//@GetMapping("admin")
//public String admin() {
//	return "Espace d'Admin";
//}
//@GetMapping("user")
//public String user() {
//	return "Espace d'User";
//}
//}