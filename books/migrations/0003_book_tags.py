# Generated by Django 4.1 on 2022-08-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0001_initial"),
        ("books", "0002_alter_book_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="tags",
            field=models.ManyToManyField(to="tags.tag"),
        ),
    ]
