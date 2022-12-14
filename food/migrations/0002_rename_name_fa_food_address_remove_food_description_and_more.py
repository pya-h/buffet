# Generated by Django 4.0.1 on 2022-01-16 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='name_fa',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='food',
            name='description',
        ),
        migrations.RemoveField(
            model_name='food',
            name='price',
        ),
        migrations.RemoveField(
            model_name='food',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='food',
            name='stock',
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='photos/foods'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
