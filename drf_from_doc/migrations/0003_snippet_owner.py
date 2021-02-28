# Generated by Django 3.1.3 on 2021-02-28 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drf_from_doc', '0002_snippet_highlighted'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='snippet', to='auth.user'),
            preserve_default=False,
        ),
    ]