# Generated by Django 3.1.1 on 2020-12-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201031_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.AddField(
            model_name='blog',
            name='company_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.ImageField(null=True, upload_to='static/images/blog_img'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image2',
            field=models.ImageField(null=True, upload_to='static/images/blog_img'),
        ),
        migrations.AddField(
            model_name='blog',
            name='pdf',
            field=models.FileField(null=True, upload_to='static/files'),
        ),
        migrations.AddField(
            model_name='blog',
            name='salary',
            field=models.CharField(choices=[('4', '4lakh'), ('6', '6lakh'), ('8', '8lakh'), ('10', '10lakh'), ('12', '12lakh'), ('14', '14lakh'), ('16', '16lakh'), ('20', '20lakh'), ('30', '30lakh'), ('35', '35lakh'), ('40', '40lakh')], max_length=3, null=True),
        ),
    ]
