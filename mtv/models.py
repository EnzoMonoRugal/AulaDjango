from django.db import models


class Topic(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return f"{self.name}"

class Page(models.Model):
    name = models.TextField(unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Access(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page}"

class Usuario(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]

    nome = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)