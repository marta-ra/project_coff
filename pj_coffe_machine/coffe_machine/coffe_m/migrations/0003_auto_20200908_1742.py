# Generated by Django 3.1.1 on 2020-09-08 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_m', '0002_auto_20200908_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffemachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, verbose_name='Model')),
            ],
        ),
        migrations.CreateModel(
            name='Point_coffemachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_point', models.CharField(max_length=255, null=True, verbose_name='Customer point')),
                ('client_name', models.CharField(max_length=255, verbose_name='Client name')),
                ('manager_name', models.CharField(max_length=255)),
                ('manager_telephone', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255, verbose_name='Point region')),
                ('coffemachines', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Coffemachines', to='coffe_m.coffemachine')),
            ],
            options={
                'ordering': ('-client_name',),
            },
        ),
        migrations.RemoveField(
            model_name='visit',
            name='customer_point',
        ),
        migrations.RenameModel(
            old_name='Client_address',
            new_name='Point_address',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.AddField(
            model_name='point_coffemachine',
            name='point_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Pointaddress', to='coffe_m.point_address'),
        ),
        migrations.AddField(
            model_name='coffemachine',
            name='visits',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Visits', to='coffe_m.visit'),
        ),
    ]
