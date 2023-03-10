# Generated by Django 4.1.6 on 2023-02-05 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('exist', 'exist'), ('need', 'need')], max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
