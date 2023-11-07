# Generated by Django 4.2.5 on 2023-09-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='FAQ images/')),
                ('summary', models.TextField()),
                ('main_part', models.TextField()),
            ],
        ),
    ]
