# Generated by Django 3.1.1 on 2020-09-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('images', models.ImageField(upload_to='static/images/blog_img')),
            ],
        ),
    ]
