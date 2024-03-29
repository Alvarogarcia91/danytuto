# Generated by Django 2.2.4 on 2019-08-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block_de_espuma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200, verbose_name='tipo de espuma')),
                ('lote', models.CharField(max_length=200)),
                ('maquina', models.CharField(max_length=200)),
                ('figura', models.CharField(choices=[('cilindro', 'cilindro'), ('block', 'block')], max_length=50, verbose_name='cilindro o block')),
                ('diametro', models.DecimalField(blank=True, decimal_places=4, max_digits=8)),
                ('largo', models.DecimalField(decimal_places=4, max_digits=8)),
                ('ancho', models.DecimalField(decimal_places=4, max_digits=8)),
                ('alto', models.DecimalField(decimal_places=4, max_digits=8)),
                ('flujo_de_aire', models.DecimalField(decimal_places=4, max_digits=8)),
                ('peso', models.DecimalField(decimal_places=4, max_digits=8)),
                ('tipo_de_unidad', models.CharField(choices=[('inicio', 'inicio'), ('normal', 'normal'), ('final', 'final'), ('muestra', 'muestra'), ('cambio', 'cambio')], max_length=50)),
                ('defecto', models.CharField(choices=[('pinhole', 'pinhole'), ('grieta', 'grieta'), ('vena', 'vena'), ('mal manejo', 'mal manejo'), ('fuera de medida', 'fuera de medida'), ('algodonozo', 'algodonozo')], max_length=50)),
            ],
        ),
    ]
