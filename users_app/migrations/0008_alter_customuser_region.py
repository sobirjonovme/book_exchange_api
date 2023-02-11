# Generated by Django 4.1.6 on 2023-02-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0007_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='region',
            field=models.CharField(choices=[("Qoraqalpog'iston", "Qoraqalpog'iston"), ('Andijon', 'Andijon'), ('Buxoro', 'Buxoro'), ('Jizzax', 'Jizzax'), ('Qashqadaryo', 'Qashqadaryo'), ('Navoiy', 'Navoiy'), ('Namangan', 'Namangan'), ('Samarqand', 'Samarqand'), ('Surxondaryo', 'Surxondaryo'), ('Sirdaryo', 'Sirdaryo'), ('Toshkent shahri', 'Toshkent shahri'), ('Toshkent viloyati', 'Toshkent viloyati'), ("Farg'ona", "Farg'ona"), ('Xorazm', 'Xorazm')], default='Toshkent shahri', max_length=30),
        ),
    ]