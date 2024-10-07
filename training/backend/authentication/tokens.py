from dajngo.urls import reverse
from dajngo.core.mail import send_mail

def create_activation_link(self, user):
	token = "token_de_verification"
	return reverse('activation_view', kwargs={'token': token}, request=self.request)
	
def send_activation_email(self, email, activation_link):
	subject = 'Activer votre compte'
	message = f'Cliquez sur le lien suivant pour activer votre compte : {activation_link}'
	from_email = 'ponggame@test.com'
	try:
		send_mail(subject, message, from_email, [email])
	except Exception as e:
		print(f"Erreur d'envoi d'email: {str(e)}")