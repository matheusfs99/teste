# Generated by Django 3.0.2 on 2020-05-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ache_medico', '0003_auto_20200522_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
