from django.db import models

# Create your models here.


class CombinedIDField(models.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return tuple(map(int, value.split('_')))
    

    def to_python(self, value):
        if isinstance(value, (list, tuple)):
            return tuple(map(int, value))
        return value


    def get_prep_value(self, value):
        if value is None:
            return None
        return '_'.join(map(str, value))


class Coords(models.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return tuple(map(float, value.split(',')))
    

    def to_python(self, value):
        if isinstance(value, (list, tuple)):
            return tuple(map(float, value))
        return value        


    def get_prep_value(self, value):
        if value is None:
            return None
        return f"{value[0]:.6f},{value[1]:.6f},{value[2]:.6f}"


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=100)
    team_flag = models.ImageField(upload_to='team_flags/')


class Batter(models.Model):
    batter_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    runs = models.IntegerField()
    balls = models.PositiveSmallIntegerField()
    fours = models.PositiveSmallIntegerField()
    sixes = models.PositiveSmallIntegerField()
    strike_rate = models.FloatField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bowler(models.Model):
    bowler_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    overs_bowled = models.FloatField()
    runs_conceded = models.IntegerField()
    runs_scored = models.IntegerField()
    wickets = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Matches(models.Model):
    match_id = models.IntegerField(primary_key=True)
    match_format = models.PositiveSmallIntegerField()    # Test 0 / ODI 1 / T20i 3 / T20 4
    tournament = models.CharField(max_length=200)
    date = models.DateField()
    ground = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    winner = models.CharField(max_length=100)
    toss_winner = models.CharField(max_length=100)
    win_margin = models.CharField(max_length=100)


class Overs(models.Model):
    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    innings = models.IntegerField()
    maiden = models.BooleanField()
    runs = models.IntegerField()
    bowler_id = models.ForeignKey(Bowler, on_delete=models.CASCADE)
    wickets = models.IntegerField()
    over_number = models.IntegerField()
    batter_id = models.ForeignKey(Batter, on_delete=models.CASCADE)


class Deliveries(models.Model):
    SEAM = 'SM'
    SPIN = 'SE'
    DELIVERY_TYPE_CHOICES = [
        (SEAM, 'Seam'),
        (SPIN, 'Spin'),
        ]
    
    FULL = 'FL'
    GOOD = 'GD'
    SHORT = 'SH'
    YORKER = 'YK'
    HARD = 'HD'
    LENGTH_CATEGORY_CHOICES = [
        (FULL, 'Full'),
        (GOOD, 'Good'),
        (SHORT, 'Short'),
        (YORKER, 'Yorker'),
        (HARD, 'Hard'),
        ]

    OUTSIDE_OFF = 'OO'
    OUTSIDE_LEG = 'OL'
    WICKET_LINE = 'WK'
    WIDE_OFF = 'WO'
    WIDE_LEG = 'WL'
    LINE_CHOICES = [
        (OUTSIDE_OFF, 'Outside Off'),
        (OUTSIDE_LEG, 'Outside Leg'),
        (WICKET_LINE, 'Stumps'),
        (WIDE_OFF, 'Wide Off'),
        (WIDE_LEG, 'Wide Leg'),
        ]
    
    SHOT_DEFENDED = 'DF'
    SHOT_ATTACKED = 'AT'
    SHOT_CHOICES = [
        (SHOT_DEFENDED, 'Defended'),
        (SHOT_ATTACKED, 'Attacked'),
        ]

    SHOT_PLAYED = 'PL'
    SHOT_MISSED = 'MS'
    SHOT_EDGED = 'ED'
    SHOT_LEAVE = 'LV'
    SHOT_CHOICES = [
        (SHOT_PLAYED, 'Played'),
        (SHOT_MISSED, 'Missed'),
        (SHOT_EDGED, 'Edged'),
        (SHOT_LEAVE, 'Leave'),
        ]
    
    OVER_WICKET = 'OV'
    AROUND_WICKET = 'RD'
    SIDE_CHOICES = [
        (OVER_WICKET, 'Over the wicket'),
        (AROUND_WICKET, 'Around the wicket'),
        ]
    

    bowler_id = models.ForeignKey(Bowler, on_delete=models.CASCADE)
    batter_id = models.ForeignKey(Batter, on_delete=models.CASCADE)
    
    combined_id = CombinedIDField(primary_key=True)                 # Innings + Over + Ball
    
    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)

    day = models.PositiveSmallIntegerField()                         # Day of the match (1 for Non Test)
    runs = models.PositiveSmallIntegerField()                        # Runs scored off the ball
    wicket = models.BooleanField()                                  # True if wicket, False if not
    extras = models.PositiveSmallIntegerField()                      # 0 if no extras         
    six_distance = models.PositiveSmallIntegerField()                 # 0 if not six

    delivery_type = models.CharField(                               # Seam / Spin
            max_length=2,
            choices=DELIVERY_TYPE_CHOICES,
    )
    length = models.FloatField()                                    # length in meters
    length_category = models.CharField(
            max_length=2,
            choices=LENGTH_CATEGORY_CHOICES,
    )
    line = models.CharField(
            max_length=2,
            choices=LINE_CHOICES,
    )
    bounce_coordinates = Coords()                            # x, y, z
    bounce_angle = models.FloatField()                              # in degrees
    bounce_height = models.FloatField()
    impact_coordinates = Coords()                            
    release_coordinates = Coords()                           
    drop_angle = models.FloatField()                                
    initial_angle = models.FloatField()                             
    landing_coordinates = Coords()                           
    crease_coordinates = Coords()                            
    stump_coordinates = Coords()                             
    
    pitch_bounce_ratio = models.FloatField()                        # bounce / pitch

    reaction_time_crease = models.FloatField()                      # in seconds
    reaction_time_intercept = models.FloatField()                   # in seconds
    shot_type = models.CharField(
            max_length=2,
            choices=SHOT_CHOICES,
    )
    shot_played = models.CharField(
            max_length=2,
            choices=SHOT_CHOICES,
    )

    wicket_type = models.CharField(max_length=100)                  # does not have in JSON

    cor = models.FloatField()                                       # Coefficient of Restitution
    cof = models.FloatField()                                       # Coefficient of Friction
    deviation = models.FloatField()                                 # RHB : leg - positive, off - negative
    swing = models.FloatField()                                     # RHB : in - positive, out - negative

    line_of_attack = models.CharField(
            max_length=2,
            choices=SIDE_CHOICES,
    )
    delivery_speed = models.FloatField()                            # in kmph
    bowler_spell = models.IntegerField()                            # 1st / 2nd / 3rd / 4th

    bat_partner = models.CharField(max_length=100)                  # name of the batter at the other end
    pavilion_end = models.BooleanField()                            # True if bowling from pavilion end
