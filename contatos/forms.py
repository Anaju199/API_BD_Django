from django import forms
from django.core.mail import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    assunto = forms.CharField(label="Assunto", max_length=100)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea())

    def send_email(self):

        nome = self.cleaned_data['nome']
        email = "anajulia99@gmail.com"
        assunto = "Novo Contato"
        mensagem = "Teste email"

        corpo = f"Nome: {nome} \nMensagem: {mensagem}"
        # corpo = f"Novo contato recebido no site."

        mail = EmailMessage(
            subject = assunto,
            from_email = 'contato@gmail.com',
            to = [email,],
            body = corpo,
            headers = {
                'Replay-To' : 'contato@gmail.com'
            }
        )
        mail.send()
