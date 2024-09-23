const url = 'https://example.com/api/users/';  // Remplacer par l'URL de votre API
const userData = {
    username: 'nouvelUtilisateur',
    email: 'nouvelutilisateur@example.com',
    password: 'motdepassefort'
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',  // Spécifie que les données sont envoyées en JSON
    },
    body: JSON.stringify(userData),  // Convertit les données en format JSON
})
.then(response => {
    if (!response.ok) {
        throw new Error('Erreur lors de la création de l\'utilisateur');
    }
    return response.json();  // Traite la réponse en JSON
})
.then(data => {
    console.log('Utilisateur créé avec succès :', data);  // Affiche les données reçues du serveur
})
.catch(error => {
    console.error('Erreur:', error);  // Gère les erreurs
});
