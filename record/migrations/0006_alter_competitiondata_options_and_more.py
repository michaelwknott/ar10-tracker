# Generated by Django 4.2.12 on 2024-05-07 10:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0005_alter_competitiondata_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="competitiondata",
            options={"ordering": ["date"], "verbose_name_plural": "competition data"},
        ),
        migrations.AlterModelOptions(
            name="trainingdata",
            options={"ordering": ["date"], "verbose_name_plural": "training data"},
        ),
    ]