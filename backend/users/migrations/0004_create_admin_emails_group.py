# Generated by Django 2.2.10 on 2020-02-14 11:21

from django.db import migrations


def create_group(apps, schema_editor):
  Group = apps.get_model('auth', 'Group')
  Permission = apps.get_model('auth', 'Permission')
  ContentType = apps.get_model('contenttypes', 'ContentType')
  User = apps.get_model('users', 'User')
  perm, _ = Permission.objects.get_or_create(
    codename="receive_admin_emails",
    name="The user will receive admin emails",
    content_type=ContentType.objects.get_for_model(User)
  )
  group, _ = Group.objects.get_or_create(name="admin_emails")
  group.permissions.add(perm)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_magiclink'),
    ]

    operations = [
        migrations.RunPython(create_group, migrations.RunPython.noop)
    ]