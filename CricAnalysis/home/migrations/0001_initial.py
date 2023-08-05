# Generated by Django 4.2.3 on 2023-08-05 07:18

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batter',
            fields=[
                ('batter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('runs', models.IntegerField()),
                ('balls', models.PositiveSmallIntegerField()),
                ('fours', models.PositiveSmallIntegerField()),
                ('sixes', models.PositiveSmallIntegerField()),
                ('strike_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bowler',
            fields=[
                ('bowler_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('overs_bowled', models.FloatField()),
                ('runs_conceded', models.IntegerField()),
                ('runs_scored', models.IntegerField()),
                ('wickets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('match_format', models.PositiveSmallIntegerField()),
                ('tournament', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('ground', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('winner', models.CharField(max_length=100)),
                ('toss_winner', models.CharField(max_length=100)),
                ('win_margin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('team_flag', models.ImageField(upload_to='team_flags/')),
            ],
        ),
        migrations.CreateModel(
            name='Overs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('innings', models.IntegerField()),
                ('maiden', models.BooleanField()),
                ('runs', models.IntegerField()),
                ('wickets', models.IntegerField()),
                ('over_number', models.IntegerField()),
                ('batter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.batter')),
                ('bowler_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bowler')),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.matches')),
            ],
        ),
        migrations.AddField(
            model_name='matches',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='home.team'),
        ),
        migrations.AddField(
            model_name='matches',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='home.team'),
        ),
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('combined_id', home.models.CombinedIDField(primary_key=True, serialize=False)),
                ('runs', models.PositiveSmallIntegerField()),
                ('wicket', models.BooleanField()),
                ('extras', models.PositiveSmallIntegerField()),
                ('six_distance', models.PositiveSmallIntegerField()),
                ('delivery_type', models.CharField(choices=[('SM', 'Seam'), ('SE', 'Spin')], max_length=2)),
                ('length', models.FloatField()),
                ('length_category', models.CharField(choices=[('FL', 'Full'), ('GD', 'Good'), ('SH', 'Short'), ('YK', 'Yorker'), ('HD', 'Hard')], max_length=2)),
                ('line', models.CharField(choices=[('OO', 'Outside Off'), ('OL', 'Outside Leg'), ('WK', 'Stumps'), ('WO', 'Wide Off'), ('WL', 'Wide Leg')], max_length=2)),
                ('bounce_coordinates', home.models.Coords()),
                ('bounce_angle', models.FloatField()),
                ('bounce_height', models.FloatField()),
                ('impact_coordinates', home.models.Coords()),
                ('release_coordinates', home.models.Coords()),
                ('drop_angle', models.FloatField()),
                ('initial_angle', models.FloatField()),
                ('landing_coordinates', home.models.Coords()),
                ('crease_coordinates', home.models.Coords()),
                ('stump_coordinates', home.models.Coords()),
                ('pitch_bounce_ratio', models.FloatField()),
                ('reaction_time_crease', models.FloatField()),
                ('reaction_time_intercept', models.FloatField()),
                ('shot_type', models.CharField(choices=[('PL', 'Played'), ('MS', 'Missed'), ('ED', 'Edged'), ('LV', 'Leave')], max_length=2)),
                ('shot_played', models.CharField(choices=[('PL', 'Played'), ('MS', 'Missed'), ('ED', 'Edged'), ('LV', 'Leave')], max_length=2)),
                ('wicket_type', models.CharField(max_length=100)),
                ('cor', models.FloatField()),
                ('cof', models.FloatField()),
                ('deviation', models.FloatField()),
                ('swing', models.FloatField()),
                ('line_of_attack', models.CharField(choices=[('OV', 'Over the wicket'), ('RD', 'Around the wicket')], max_length=2)),
                ('delivery_speed', models.FloatField()),
                ('bowler_spell', models.IntegerField()),
                ('bat_partner', models.CharField(max_length=100)),
                ('pavilion_end', models.BooleanField()),
                ('batter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.batter')),
                ('bowler_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bowler')),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.matches')),
            ],
        ),
        migrations.AddField(
            model_name='bowler',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.team'),
        ),
        migrations.AddField(
            model_name='batter',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.team'),
        ),
    ]
