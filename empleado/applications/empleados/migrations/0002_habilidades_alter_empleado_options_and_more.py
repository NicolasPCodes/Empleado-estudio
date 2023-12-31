# Generated by Django 4.2.1 on 2023-07-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_options_and_more'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-first_name', 'last_name'], 'verbose_name': 'Mi empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'departamento')},
        ),
    ]
