package project.iwa.model;



import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
@Entity @AllArgsConstructor @NoArgsConstructor @Data
public class Student {
	@Id
	Long id;
	int age;
	String nom;
	

}
