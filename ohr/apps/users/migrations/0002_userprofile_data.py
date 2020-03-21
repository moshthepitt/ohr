# Generated by Django 3.0.2 on 2020-03-21 08:16
# pylint: disable=invalid-name,missing-module-docstring,missing-class-docstring
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("ohr.users", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="data",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=dict,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                verbose_name="Data",
            ),
        )
    ]
