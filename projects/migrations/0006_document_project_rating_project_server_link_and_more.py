# Generated by Django 5.1 on 2024-09-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='server_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_documents',
        ),
        migrations.AddField(
            model_name='project',
            name='project_documents',
            field=models.ManyToManyField(blank=True, related_name='projects', to='projects.document'),
        ),
    ]
