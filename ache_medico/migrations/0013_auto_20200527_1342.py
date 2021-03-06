# Generated by Django 3.0.2 on 2020-05-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ache_medico', '0012_auto_20200525_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='planos_aceitos',
            field=models.CharField(blank=True, choices=[('Bradesco Saúde', 'Bradesco Saúde'), ('Amil', 'Amil'), ('NotreDame Intermédica (GNDI)', 'NotreDame Intermédica (GNDI)'), ('Porto Seguro', 'Porto Seguro'), ('SulAmérica Saúde', 'SulAmérica Saúde'), ('Care Plus', 'Care Plus'), ('Prevent Senior', 'Prevent Senior'), ('Allianz Saúde', 'Allianz Saúde'), ('Hapvida', 'Hapvida'), ('Sompo Saúde', 'Sompo Saúde'), ('Omint', 'Omint'), ('AMEPE CAMPE', 'AMEPE CAMPE'), ('BANCO CENTRAL (Bancen)', 'BANCO CENTRAL (Bancen)'), ('CASSI (Banco do Brasil)', 'CASSI (Banco do Brasil)'), ('CONAB', 'CONAB'), ('EMBRATEL', 'EMBRATEL'), ('FACHESF', 'FACHESF'), ('FUNCEF (Saúde Caixa)', 'FUNCEF (Saúde Caixa)'), ('GAMA SAÚDE', 'GAMA SAÚDE'), ('MEDIAL SAÚDE', 'MEDIAL SAÚDE'), ('PLANASSIST MINIST.PUB. TRABALHO', 'PLANASSIST MINIST.PUB. TRABALHO'), ('PLANASSIST MINIST.PUB. MILITAR', 'PLANASSIST MINIST.PUB. MILITAR'), ('PETROBRAS DISTRIBUIDORA', 'PETROBRAS DISTRIBUIDORA'), ('PROASA', 'PROASA'), ('UNAFISCO SAÚDE', 'UNAFISCO SAÚDE'), ('UNIMED', 'UNIMED'), ('AERONÁUTICA', 'AERONÁUTICA'), ('CAMED SAÚDE', 'CAMED SAÚDE'), ('COMPESASAUDE', 'COMPESASAUDE'), ('POSTAL SAÚDE (Correios)', 'POSTAL SAÚDE (Correios)'), ('ESTALEIRO ATLÂNTICO SUL (EAS)', 'ESTALEIRO ATLÂNTICO SUL (EAS)'), ('FIO SAÚDE', 'FIO SAÚDE'), ('FUSEX', 'FUSEX'), ('GEAP', 'GEAP'), ('MEDISERVICE', 'MEDISERVICE'), ('PLANASSIST MINIST. PUB. FEDERAL', 'PLANASSIST MINIST. PUB. FEDERAL'), ('OMIINT/SKILL', 'OMIINT/SKILL'), ('PETROB. PETROLEO', 'PETROB. PETROLEO')], max_length=300, null=True),
        ),
    ]
