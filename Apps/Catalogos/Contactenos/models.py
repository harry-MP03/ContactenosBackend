from django.db import models

class Contactos(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=160)
    Apellidos = models.CharField(max_length=160)
    Email = models.EmailField()
    Asunto = models.CharField(max_length=200, blank=True, null=True)
    Mensaje = models.TextField()
    FechaCreacion = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "Contactos"
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f"Mensaje de: {self.Nombres} - {self.Asunto}"