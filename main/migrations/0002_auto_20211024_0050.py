# Generated by Django 3.2.8 on 2021-10-24 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreasMedicasabs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('jefe_area', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('especialidad', models.CharField(max_length=50)),
                ('area', models.ManyToManyField(to='main.AreasMedicasabs')),
            ],
        ),
        migrations.CreateModel(
            name='Pasiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_registro', models.DateField()),
                ('fecha_alta', models.DateField()),
                ('diacnostico', models.TextField()),
                ('peso', models.IntegerField()),
                ('estatura_cm', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('Pasiente', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main.pasiente')),
                ('medico', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main.medico')),
            ],
        ),
        migrations.AddField(
            model_name='medico',
            name='pasientes',
            field=models.ManyToManyField(to='main.Pasiente'),
        ),
    ]