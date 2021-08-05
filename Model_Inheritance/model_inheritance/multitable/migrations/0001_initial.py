# Generated by Django 3.2.6 on 2021-08-05 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept_name', models.CharField(max_length=20)),
                ('Dept_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('dept_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multitable.dept')),
                ('stu_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=16)),
            ],
            bases=('multitable.dept',),
        ),
    ]
