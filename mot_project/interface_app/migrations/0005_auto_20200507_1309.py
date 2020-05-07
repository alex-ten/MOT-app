# Generated by Django 3.0.4 on 2020-05-07 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0004_auto_20200504_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='score',
        ),
        migrations.AddField(
            model_name='episode',
            name='RSI',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='SRI_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='angle_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='angle_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='episode_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='finished_session',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='episode',
            name='fixation_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='n_distractors',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='n_targets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='nb_distract_retrieved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='nb_target_retrieved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='presentation_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='radius',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='secondary_task',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='episode',
            name='speed_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='speed_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='tracking_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='participantprofile',
            name='screen_params',
            field=models.FloatField(default=39.116),
        ),
        migrations.CreateModel(
            name='SecondaryTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='detection', max_length=20)),
                ('delta_orientation', models.FloatField(default=0)),
                ('success', models.BooleanField(default=False)),
                ('answer_duration', models.FloatField(default=0)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface_app.Episode')),
            ],
        ),
    ]