# Generated by Django 3.1.1 on 2020-10-31 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('blog', '0004_auto_20201031_0626'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_user_sem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='static/images/profile_pics')),
                ('bio', models.TextField(blank=True)),
                ('sem', models.CharField(choices=[('1', 'first'), ('2', 'second'), ('3', 'third'), ('4', 'fourth'), ('5', 'fifth'), ('6', 'sixth'), ('7', 'seventh'), ('8', 'eigth')], default='first', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
