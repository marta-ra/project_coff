# Generated by Django 3.1.1 on 2020-09-09 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_m', '0006_auto_20200908_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='point_coffemachine',
            options={},
        ),
        migrations.RemoveField(
            model_name='point_coffemachine',
            name='coffemachines',
        ),
        migrations.AddField(
            model_name='coffemachine',
            name='point',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Coffemachines', to='coffe_m.point_coffemachine'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='coffemachine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visits', to='coffe_m.coffemachine'),
        ),
    ]
