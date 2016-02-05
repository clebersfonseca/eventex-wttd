# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations


def copy_src_to_dst(Source, Destination):
    for src in Source.objects.all():
        dst = Destination(
            title=src.title,
            start=src.start,
            description=src.description,
            slots=src.slots
        )
        dst.save()
        dst.speakers.set(src.speakers.all())
        src.delete()


def forward_course_src_to_dst(apps, schema_editor):
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course')
    )


def backward_course_src_to_dst(apps, schema_editor):
    copy_src_to_dst(
        apps.get_model('core', 'Course'),
        apps.get_model('core', 'CourseOld')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_course'),
    ]

    operations = [
        migrations.RunPython(forward_course_src_to_dst, backward_course_src_to_dst)
    ]
