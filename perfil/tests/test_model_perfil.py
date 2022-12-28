from django.test import TestCase
from perfil.models import Perfil
from ..models import Perfil
from mixer.backend.django import mixer
from django.contrib.auth.models import User

class TestPerfilModels(TestCase):
    def test_model_fields(self):
        mixer.blend(User, id=100, username='Lucas')

        mixer.blend(
            Perfil,
            id=100,
            usuario_id=100,
            idade=26,
            data_nascimento='1996-09-03',
            cpf='10575063629',
            cep="38408136",
            endereco="Rua Tamoios",
            numero="86",
            bairro="Amorim",
            cidade="Araguari",
            estado="MG",
        )

        perfil = Perfil.objects.first()

        self.assertEqual(perfil.id, 100)
        self.assertEqual(perfil.usuario.username, 'Lucas')
        self.assertEqual(perfil.idade, 26)
        self.assertEqual(str(perfil.data_nascimento), '1996-09-03')
        self.assertEqual(perfil.cpf, "10575063629")
        self.assertEqual(perfil.cep, "38408136")
        self.assertEqual(perfil.endereco, "Rua Tamoios")
        self.assertEqual(perfil.numero, "86")
        self.assertEqual(perfil.bairro, "Amorim")
        self.assertEqual(perfil.cidade, "Araguari")
        self.assertEqual(perfil.estado, "MG")
  
