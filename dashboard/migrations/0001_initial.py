# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(null=True)),
                ('is_deleted', models.BooleanField(default=False, verbose_name=b'Eliminado?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'course',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course_publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(to='dashboard.Course')),
            ],
            options={
                'db_table': 'course_publication',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('type', models.CharField(default=b'0', max_length=1)),
                ('is_deleted', models.BooleanField(default=False, verbose_name=b'Eliminado?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'publication',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('grade', models.CharField(max_length=2, choices=[(b'11', b'PRIMARIA - 1ro'), (b'12', b'PRIMARIA - 2do'), (b'13', b'PRIMARIA - 3ro'), (b'14', b'PRIMARIA - 4to'), (b'15', b'PRIMARIA - 5to'), (b'16', b'PRIMARIA - 6to'), (b'11', b'SECUNDARIA - 1ro'), (b'22', b'SECUNDARIA - 2do'), (b'23', b'SECUNDARIA - 3ro'), (b'24', b'SECUNDARIA - 4to'), (b'25', b'SECUNDARIA - 5to')])),
                ('is_deleted', models.BooleanField(default=False, verbose_name=b'Eliminado?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'section',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publication', models.ForeignKey(to='dashboard.Publication')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_publication',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(to='dashboard.Section')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_section',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=120, verbose_name=b'Direcci\xc3\xb3n', blank=True)),
                ('phone', models.CharField(max_length=12, verbose_name=b'Telefono', blank=True)),
                ('dni', models.CharField(max_length=8, verbose_name=b'DNI', blank=True)),
                ('image', models.ImageField(upload_to=b'profiles_picture', null=True, verbose_name=b'Imagen', blank=True)),
                ('privilege', models.CharField(default=b'1', max_length=1, verbose_name=b'Privilegios', choices=[(b'0', b'Ning\xc3\xbano'), (b'1', b'Chat y lectura'), (b'2', b'Chat, lectura y escritura')])),
                ('user_type', models.CharField(default=b'0', max_length=1, verbose_name=b'Tipo de Usuario', choices=[(b'0', b'Alumno'), (b'1', b'Profesor')])),
                ('is_deleted', models.BooleanField(default=False, verbose_name=b'Eliminado?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course_publication',
            name='publication',
            field=models.ForeignKey(to='dashboard.Publication'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='section',
            field=models.ForeignKey(to='dashboard.Section'),
            preserve_default=True,
        ),
    ]
