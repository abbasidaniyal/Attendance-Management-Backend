# Generated by Django 2.2 on 2019-04-23 21:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.AutoField(primary_key=True, serialize=False)),
                ('batch_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_name', models.CharField(max_length=30)),
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_live', models.CharField(choices=[('L', 'L'), ('NL', 'NL')], default='NL', max_length=5)),
                ('subject_batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Batch')),
                ('subject_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('student_id', models.BigIntegerField(unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('date_joined', models.DateField(auto_now=True)),
                ('student_batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Batch')),
                ('student_subject', models.ManyToManyField(to='students.Subject', verbose_name='Student studies the subject')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendence_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=2)),
                ('date', models.DateField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Subject')),
            ],
        ),
    ]
