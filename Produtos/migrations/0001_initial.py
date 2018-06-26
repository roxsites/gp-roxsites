# Generated by Django 2.0.6 on 2018-06-23 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_nome', models.CharField(max_length=40)),
                ('produto_marca', models.CharField(max_length=30)),
                ('Quantidade', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='produtos_fotos')),
            ],
        ),
    ]