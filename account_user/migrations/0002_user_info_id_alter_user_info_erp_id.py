# Generated by Django 4.2.7 on 2024-03-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_info',
            name='ERP_id',
            field=models.CharField(max_length=255),
        ),
    ]
