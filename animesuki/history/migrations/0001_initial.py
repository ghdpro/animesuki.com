# Generated by Django 2.2 on 2019-04-15 16:50

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('object_str', models.CharField(blank=True, max_length=250)),
                ('request_type', models.PositiveSmallIntegerField(choices=[(1, 'Add'), (2, 'Modify'), (3, 'Delete'), (4, 'Related')])),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Denied'), (4, 'Withdrawn')], default=1)),
                ('data_revert', django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True)),
                ('data_changed', django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True)),
                ('comment', models.TextField(blank=True)),
                ('user_ip', models.GenericIPAddressField(unpack_ipv4=True)),
                ('mod_ip', models.GenericIPAddressField(blank=True, null=True, unpack_ipv4=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='changerequest_mod', to=settings.AUTH_USER_MODEL)),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='changerequest_object', to='contenttypes.ContentType')),
                ('related_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='changerequest_related', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='changerequest_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'history',
                'permissions': (('self_approve', 'Can self-approve add, modify & related requests'), ('self_delete', 'Can self-approve delete requests'), ('throttle_min', 'Subject to more lenient throttling'), ('throttle_off', 'Not subject to any throttling'), ('mod_approve', 'Can moderate add, modify & related requests'), ('mod_delete', 'Can moderate delete requests')),
                'default_permissions': (),
            },
        ),
    ]
