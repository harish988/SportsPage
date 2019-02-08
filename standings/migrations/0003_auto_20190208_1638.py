# Generated by Django 2.1.4 on 2019-02-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standings', '0002_auto_20190207_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standings',
            name='sport',
            field=models.CharField(choices=[('badmiton', 'Badmiton'), ('ballbadmiton', 'Ball Badmiton'), ('basketball', 'Basketball'), ('cricket', 'Cricket'), ('chess', 'Chess'), ('football', 'Football'), ('handball', 'Handball'), ('hockey', 'Hockey'), ('kabaddi', 'Kabaddi'), ('khokho', 'Kho-Kho'), ('tabletennis', 'Table Tennis')], max_length=20),
        ),
        migrations.AlterField(
            model_name='standings',
            name='team1',
            field=models.CharField(choices=[('coral', 'Coral'), ('emerald', 'Emerald'), ('diamond', 'Diamond'), ('ruby', 'Ruby'), ('pearl', 'Pearl'), ('sapphire', 'Sapphire')], max_length=10),
        ),
        migrations.AlterField(
            model_name='standings',
            name='team2',
            field=models.CharField(choices=[('coral', 'Coral'), ('emerald', 'Emerald'), ('diamond', 'Diamond'), ('ruby', 'Ruby'), ('pearl', 'Pearl'), ('sapphire', 'Sapphire')], max_length=10),
        ),
        migrations.AlterField(
            model_name='standings',
            name='team3',
            field=models.CharField(choices=[('coral', 'Coral'), ('emerald', 'Emerald'), ('diamond', 'Diamond'), ('ruby', 'Ruby'), ('pearl', 'Pearl'), ('sapphire', 'Sapphire')], max_length=10),
        ),
    ]
