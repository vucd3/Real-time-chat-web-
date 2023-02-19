# Generated by Django 4.1.6 on 2023-02-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_room_user_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='room',
        ),
    ]
