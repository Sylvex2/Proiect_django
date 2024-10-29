from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    # Crearea grupurilor
    operator_group, created = Group.objects.get_or_create(name='Operator')
    admin_group, created = Group.objects.get_or_create(name='Administrator')

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]