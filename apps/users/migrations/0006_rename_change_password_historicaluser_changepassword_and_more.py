# Generated by Django 5.0.7 on 2024-11-11 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_historicaluser_rol_user_rol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='change_password',
            new_name='changePassword',
        ),
        migrations.RenameField(
            model_name='historicaluser',
            old_name='change_password_next_session',
            new_name='changePasswordNextSession',
        ),
        migrations.RenameField(
            model_name='historicaluser',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='change_password',
            new_name='changePassword',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='change_password_next_session',
            new_name='changePasswordNextSession',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstname',
        ),
    ]
