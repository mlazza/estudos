# Generated by Django 3.1.4 on 2020-12-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201201_0858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-published',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='alterado',
            new_name='altered',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='criado',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publicado',
            new_name='published',
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('rascunho', 'Rascunho'), ('published', 'Published')], default='rascunho', max_length=10),
        ),
    ]
