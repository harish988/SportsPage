# Generated by Django 2.1.4 on 2019-01-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20190123_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='results',
            name='sport',
            field=models.CharField(choices=[('badmiton', 'Badmiton'), ('ballbadmiton', 'Ball Badmiton'), ('basketball', 'Basketball'), ('cricket', 'Cricket'), ('chess', 'Chess'), ('football', 'Football'), ('handball', 'Handball'), ('hockey', 'Hockey'), ('kabaddi', 'Kabaddi'), ('khokho', 'Kho-Kho'), ('tabletennis', 'Table Tennois')], max_length=20),
        ),
        migrations.AlterField(
            model_name='results',
            name='team1',
            field=models.CharField(choices=[('direct', 'Direct'), ('coral', 'Coral'), ('emerald', 'Emerald'), ('diamond', 'Diamond'), ('ruby', 'Ruby'), ('pearl', 'Peark'), ('sapphire', 'Sapphire')], max_length=10),
        ),
        migrations.AlterField(
            model_name='results',
            name='team2',
            field=models.CharField(choices=[('direct', 'Direct'), ('coral', 'Coral'), ('emerald', 'Emerald'), ('diamond', 'Diamond'), ('ruby', 'Ruby'), ('pearl', 'Peark'), ('sapphire', 'Sapphire')], max_length=10),
        ),
        migrations.AlterField(
            model_name='results',
            name='winner',
            field=models.CharField(choices=[('direct', 'Direct'), ('coral', 'Coral'), ('emerald', 'Emerald'), ('diamond', 'Diamond'), ('ruby', 'Ruby'), ('pearl', 'Peark'), ('sapphire', 'Sapphire')], default=models.CharField(choices=[('direct', 'Direct'), ('coral', 'Coral'), ('emerald', 'Emerald'), ('diamond', 'Diamond'), ('ruby', 'Ruby'), ('pearl', 'Peark'), ('sapphire', 'Sapphire')], max_length=10), max_length=10),
        ),
    ]
