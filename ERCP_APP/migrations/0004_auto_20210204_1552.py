# Generated by Django 3.1.6 on 2021-02-04 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERCP_APP', '0003_auto_20210204_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdetail',
            name='journey_from',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source', to='ERCP_APP.carddetail'),
        ),
    ]