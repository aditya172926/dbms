# Generated by Django 3.1.2 on 2020-12-01 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='Course',
        ),
        migrations.AddField(
            model_name='course',
            name='Department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.department'),
        ),
    ]