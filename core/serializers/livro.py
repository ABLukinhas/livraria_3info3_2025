from rest_framework.serializers import ModelSerializer

from core.models import Livro

class LivroSerializer(ModelSerializer):
    class meta:
        model = Livro
        frieds = "__all__"