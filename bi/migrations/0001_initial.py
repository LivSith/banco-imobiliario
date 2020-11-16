# Generated by Django 2.2.17 on 2020-11-16 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Tabuleiros',
                'verbose_name': 'Tabuleiro',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome da propriedade')),
                ('to_buy', models.DecimalField(decimal_places=2, max_digits=8)),
                ('to_rent', models.DecimalField(decimal_places=2, max_digits=8)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board', to='bi.Board', verbose_name='Tabuleiro')),
            ],
            options={
                'verbose_name_plural': 'Propriedades',
                'verbose_name': 'Propriedade',
            },
        ),
    ]