# Generated by Django 3.1.6 on 2021-02-21 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERCP_APP', '0008_auto_20210221_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdetail',
            name='user_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ucard', to='ERCP_APP.carddetail'),
        ),
    ]
