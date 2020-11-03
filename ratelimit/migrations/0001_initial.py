# Generated by Django 2.2 on 2020-11-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExceededLimitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255, verbose_name='User Agent')),
                ('ip_address', models.GenericIPAddressField(db_index=True, null=True, verbose_name='IP Address')),
                ('username', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Username')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('blocked_at', models.DateTimeField(auto_now_add=True, verbose_name='Blocked At')),
                ('access_attempt_failures', models.PositiveIntegerField(verbose_name='Access Attempt Failure Count')),
            ],
            options={
                'verbose_name': 'exceeded limit record',
                'verbose_name_plural': 'exceeded limit records',
            },
        ),
    ]