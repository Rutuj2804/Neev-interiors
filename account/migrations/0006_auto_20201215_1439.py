# Generated by Django 3.1.4 on 2020-12-15 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='image',
            new_name='category_image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='display')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.categorie')),
            ],
        ),
    ]
