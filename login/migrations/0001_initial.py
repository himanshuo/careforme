# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compliment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compliment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('fb_id', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='compliment',
            name='compliment_by',
            field=models.ForeignKey(related_name='compliment_by', to='login.User', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compliment',
            name='compliment_for',
            field=models.ForeignKey(related_name='compliment_for', to='login.User', null=True),
            preserve_default=True,
        ),
    ]
