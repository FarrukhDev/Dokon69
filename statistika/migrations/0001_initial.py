# Generated by Django 4.0.5 on 2022-06-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('umumiy_foyda', models.CharField(blank=True, max_length=45, null=True)),
                ('bugungi_savdo', models.CharField(blank=True, max_length=45, null=True)),
                ('bugungi_foyda', models.CharField(blank=True, max_length=45, null=True)),
                ('bugungi_zarar', models.CharField(blank=True, max_length=45, null=True)),
                ('soni', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]