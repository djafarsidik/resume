# Generated by Django 4.2.1 on 2023-07-09 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postalcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kab_kota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('nama', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('kabupaten', 'Kabuputen'), ('kota', 'Kota')], max_length=10)),
                ('provinsi', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='postalcode.provinsi')),
            ],
        ),
    ]
