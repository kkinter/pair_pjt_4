# Generated by Django 3.2.13 on 2022-10-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(blank=True, default='background_image/dafault.png', upload_to='accounts/background/'),
        ),
    ]