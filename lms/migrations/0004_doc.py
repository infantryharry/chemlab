# Generated by Django 2.2 on 2022-03-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_auto_20220228_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50, verbose_name='文件名字')),
                ('file_path', models.CharField(max_length=100, verbose_name='文件路径')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='借用时间')),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件',
            },
        ),
    ]