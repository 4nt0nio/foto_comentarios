from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre


class Foto(models.Model):
	autor = models.ForeignKey('auth.User')
	categoria = models.ForeignKey(Categoria,null=True)
	titulo = models.CharField(max_length=50,default='Sin titulo')
	foto = models.ImageField(upload_to='fotografias/')
	fecha_pulic = models.DateField(auto_now_add = True)
	descripcion = models.TextField()
	favorito = models.BooleanField(default=False)

	def __str__(self):
		return self.titulo


class Cometario(models.Model):
	foto = models.ForeignKey(Foto)
	cometario = models.TextField()

	def __str__(self):
		return self.cometario


@receiver(post_delete,sender=Foto)
def foto_delete(sender, instance, **kwargs):
	instance.foto.delete(False)