# Generated by Django 2.1.3 on 2019-01-01 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0019_auto_20190101_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': "Note's categories",
                'verbose_name': "Note's category",
            },
        ),
        migrations.CreateModel(
            name='Student_Notes',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Content')),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_student_note', to=settings.AUTH_USER_MODEL)),
                ('note_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='note_category', to='student.Note_Category')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_have_note', to='student.Student')),
            ],
            options={
                'ordering': ('-created_at', '-updated_at'),
                'verbose_name_plural': 'Student Notes',
                'verbose_name': 'Student Note',
            },
        ),
    ]
