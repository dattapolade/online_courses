# Generated by Django 4.2.2 on 2024-08-22 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='courses.choice')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.RemoveField(
            model_name='examquestion',
            name='course',
        ),
        migrations.RemoveField(
            model_name='examsubmission',
            name='course',
        ),
        migrations.RemoveField(
            model_name='examsubmission',
            name='user',
        ),
        migrations.DeleteModel(
            name='ExamChoice',
        ),
        migrations.DeleteModel(
            name='ExamQuestion',
        ),
        migrations.DeleteModel(
            name='ExamSubmission',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='courses.question'),
        ),
    ]
