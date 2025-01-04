# Generated by Django 4.2.7 on 2025-01-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_rename_user_transaction_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type_of_transaction',
            field=models.CharField(choices=[('Expense', 'Expense'), ('Income', 'Income')], max_length=10),
        ),
    ]