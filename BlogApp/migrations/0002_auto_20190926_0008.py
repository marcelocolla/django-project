# Generated by Django 2.2 on 2019-09-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='mensagem',
            field=models.CharField(max_length=300),
        ),
    ]