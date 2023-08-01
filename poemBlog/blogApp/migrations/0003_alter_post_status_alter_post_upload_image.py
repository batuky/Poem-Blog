# Generated by Django 4.2.3 on 2023-07-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_post_upload_image_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='upload_image',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='uploads/'),
        ),
    ]
