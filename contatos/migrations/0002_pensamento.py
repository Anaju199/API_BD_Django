# Generated by Django 5.0.3 on 2024-03-27 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contatos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pensamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("conteudo", models.CharField(max_length=50)),
                ("autoria", models.CharField(max_length=50)),
                ("modelo", models.CharField(max_length=50)),
            ],
        ),
    ]
