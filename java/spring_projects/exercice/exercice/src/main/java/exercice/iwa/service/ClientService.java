package exercice.iwa.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import exercice.iwa.model.Client;
import exercice.iwa.repository.ClientRepository;
import jakarta.persistence.EntityNotFoundException;

@Service
public class ClientService {
@Autowired
private ClientRepository clientRepository;

	public Client addClient(Client client) {
		// TODO Auto-generated method stub
		return clientRepository.save(client);
	}

	public Object getClientByCode(Long code) {
		 return clientRepository.findById(code)
	                .orElseThrow(() -> new EntityNotFoundException("Client not found with code: " + code));
	}

	public List<Client> getAllClients() {
		
		return clientRepository.findAll();
	}

	public void deleteClient(Long code) {
		clientRepository.deleteById(code);
		
	}

}
