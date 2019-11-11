# Generated by Django 2.2.7 on 2019-11-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(max_length=30, verbose_name='음식이름')),
                ('pic', models.ImageField(default='media/default_image.jpeg', upload_to='', verbose_name='사진')),
                ('GPS', models.CharField(blank=True, max_length=300, verbose_name='위치')),
                ('taste', models.TextField(blank=True, max_length=300, verbose_name='음식평')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='작성한시간')),
                ('fix', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
        ),
        migrations.CreateModel(
            name='LOGIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]