from django.db import models

# Create your models here.

class Block_de_espuma(models.Model):

    modelo = models.CharField('tipo de espuma',max_length=200)
    lote = models.CharField(max_length=200)
    maquina = models.CharField(max_length=200)
    FIGURAS = (
        ('cilindro','cilindro'),
        ('block', 'block')
    )
    figura = models.CharField('cilindro o block',max_length=50, choices=FIGURAS)
    diametro = models.DecimalField(max_digits=8, decimal_places=4, blank= True)
    largo = models.DecimalField(max_digits=8, decimal_places=4)
    ancho = models.DecimalField(max_digits=8, decimal_places=4)
    alto = models.DecimalField(max_digits=8, decimal_places=4)
    flujo_de_aire = models.DecimalField(max_digits=8,decimal_places=4)
    peso = models.DecimalField(max_digits=8,decimal_places=4)
    TIPOS_DE_UNIDAD = (
        ('inicio','inicio'),
        ('normal','normal'),
        ('final','final'),
        ('muestra','muestra'),
        ('cambio','cambio')
    )
    tipo_de_unidad = models.CharField(max_length=50, choices=TIPOS_DE_UNIDAD)
    DEFECTOS = (
        ('pinhole','pinhole'),
        ('grieta', 'grieta'),
        ('vena', 'vena'),
        ('mal manejo','mal manejo'),
        ('fuera de medida', 'fuera de medida'),
        ('algodonozo', 'algodonozo')
    )
    defecto = models.CharField(max_length=50, choices=DEFECTOS)
