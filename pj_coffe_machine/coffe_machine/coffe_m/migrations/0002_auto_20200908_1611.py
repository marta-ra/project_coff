# Generated by Django 3.1.1 on 2020-09-08 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffe_m', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, verbose_name='Model')),
                ('client_name', models.CharField(max_length=255, verbose_name='Client name')),
                ('customer_point', models.CharField(max_length=255, null=True, verbose_name='Customer point')),
                ('client_region', models.CharField(max_length=255, verbose_name='Client_region')),
            ],
            options={
                'ordering': ('-client_name',),
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_point', models.CharField(max_length=255, null=True, verbose_name='Customer point')),
                ('visit_date', models.DateField(verbose_name='Date of visit')),
                ('technical_specialist', models.CharField(max_length=255, verbose_name='Technical specialist')),
                ('done', models.CharField(max_length=255, verbose_name='What was done during the visit?')),
                ('renovation', models.BooleanField(verbose_name='Was there a renovation')),
                ('what_renovation', models.CharField(max_length=255, verbose_name='What was the repair?')),
            ],
        ),
        migrations.RenameField(
            model_name='client_address',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='client_address',
            old_name='House',
            new_name='house',
        ),
        migrations.RenameField(
            model_name='client_address',
            old_name='Street',
            new_name='street',
        ),
        migrations.AddField(
            model_name='manager',
            name='customer_point',
            field=models.CharField(max_length=255, null=True, verbose_name='Customer point'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='telephone',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.AddField(
            model_name='client',
            name='client_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_address', to='coffe_m.client_address'),
        ),
        migrations.AddField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Manager', to='coffe_m.manager'),
        ),
        migrations.AddField(
            model_name='client',
            name='visit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Visit', to='coffe_m.visit'),
        ),
    ]
