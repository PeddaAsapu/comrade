# Generated by Django 4.1.2 on 2022-11-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUsers',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_bot', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
