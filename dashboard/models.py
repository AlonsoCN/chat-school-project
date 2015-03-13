# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from s3k_school.config import GRADES
from os import path
from PIL import Image
from s3k_school.settings import MEDIA_ROOT


class UserProfile(models.Model):
    PRIVILEGES = (
        ('0', 'Ningúno'),
        ('1', 'Chat y lectura'),
        ('2', 'Chat, lectura y escritura')
    )
    USER_TYPES = (
        ('0', 'Alumno'),
        ('1', 'Profesor')
    )

    user = models.OneToOneField(User, verbose_name="Usuario")
    address = models.CharField(max_length=120, blank=True,
                               verbose_name="Dirección")
    phone = models.CharField(max_length=12, blank=True,
                             verbose_name="Telefono")
    dni = models.CharField(max_length=8, blank=True, verbose_name="DNI")
    image = models.ImageField(upload_to='profiles_picture', blank=True,
                              null=True, verbose_name="Imagen")
    privilege = models.CharField(max_length=1, choices=PRIVILEGES,
                                 default='1', verbose_name="Privilegios")
    user_type = models.CharField(max_length=1, choices=USER_TYPES,
                                 verbose_name="Tipo de Usuario", default='0')
    is_deleted = models.BooleanField(default=False, verbose_name="Eliminado?")

    # Auditory
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # # Obtiene la dirección absoluta en disco del archivo
    # def get_source_filename(self):
    #     return path.join(MEDIA_ROOT, str(self.image))
    #
    # # Método para hacer el re-dimensión de imagen a 200x200
    # def save(self, size=(200, 200)):
    #     if not self.id and not self.image:
    #         return
    #
    #     super(UserProfile, self).save()
    #
    #     filename = self.get_source_filename()
    #     image = Image.open(filename)
    #
    #     image.thumbnail(size, Image.ANTIALIAS)
    #     image.save(filename)

    def __unicode__(self):
        return '%s, %s' % (self.user.last_name, self.user.first_name)

    class Meta:
        db_table = "user_profile"


class Section(models.Model):
    name = models.CharField(max_length=30)
    grade = models.CharField(max_length=2, choices=GRADES)
    is_deleted = models.BooleanField(default=False, verbose_name="Eliminado?")

    # Auditory
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s, %s' % (self.name, self.grade)

    class Meta:
        db_table = "section"


class Course(models.Model):
    name = models.CharField(max_length=120)
    section = models.ForeignKey(Section)
    description = models.TextField(null=True)
    is_deleted = models.BooleanField(default=False, verbose_name="Eliminado?")

    # Auditory
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        db_table = "course"


class Publication(models.Model):
    PUBLICATION_TYPES = (
        ('0', 'Informativo'),
        ('1', 'Advertencia'),
        ('2', 'Urgente')
    )

    content = models.TextField()
    type = models.CharField(max_length=1, default='0')
    is_deleted = models.BooleanField(default=False, verbose_name="Eliminado?")

    # Auditory
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.content

    class Meta:
        db_table = "publication"


class User_section(models.Model):
    user = models.ForeignKey(User)
    section = models.ForeignKey(Section)
    # Auditory
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s, %s - %s' % (self.user.last_name, self.section.grade, self.section.name)

    class Meta:
        db_table = "user_section"


class Course_publication(models.Model):
    course = models.ForeignKey(Course)
    publication = models.ForeignKey(Publication)
    # Auditory
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s, %s' % (self.course.name, self.publication.id)

    class Meta:
        db_table = "course_publication"


class User_publication(models.Model):
    user = models.ForeignKey(User)
    publication = models.ForeignKey(Publication)
    # Auditory
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s, %s' % (self.user.last_name, self.publication.id)

    class Meta:
        db_table = "user_publication"
