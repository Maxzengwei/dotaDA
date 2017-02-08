from django.db import models


class Match(models.Model):
    match_id = models.CharField(max_length=200)
    match_seq_num = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    lobby_type = models.CharField(max_length=200)

class Player(models.Model):
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    account_id = models.CharField(max_length=200)
    player_slot = models.CharField(max_length=200)
    hero_id = models.CharField(max_length=200)

class MatchDetail(models.Model):
    season = models.CharField(max_length=200)                  # Season the game was played in
    radiant_win  = models.CharField(max_length=200)            # Win status of game (True for Radiant win, False for Dire win)
    duration  = models.CharField(max_length=200)               # Elapsed match time in seconds
    start_time   = models.CharField(max_length=200)            # Unix timestamp for beginning of match
    match_id  = models.CharField(max_length=200)               # Unique match ID
    match_seq_num  = models.CharField(max_length=200)          # Number indicating position in which this match was recorded
    tower_status_radiant  = models.CharField(max_length=200)   # Status of Radiant towers
    tower_status_dire  = models.CharField(max_length=200)      # Status of Dire towers
    barracks_status_radiant  = models.CharField(max_length=200)# Status of Radiant barracks
    barracks_status_dire  = models.CharField(max_length=200)   # Status of Dire barracks
    cluster  = models.CharField(max_length=200)                # The server cluster the match was played on, used in retrieving replays
    cluster_name  = models.CharField(max_length=200)           # The region the match was played on
    first_blood_time  = models.CharField(max_length=200)       # Time elapsed in seconds since first blood of the match
    lobby_type  = models.CharField(max_length=200)             # See lobby_type table
    lobby_name  = models.CharField(max_length=200)             # See lobby_type table
    human_players  = models.CharField(max_length=200)          # Number of human players in the match
    leagueid   = models.CharField(max_length=200)              # Unique league ID
    positive_votes = models.CharField(max_length=200)          # Number of positive/thumbs up votes
    negative_votes  = models.CharField(max_length=200)         # Number of negative/thumbs down votes
    game_mode    = models.CharField(max_length=200)            # See game_mode table
    game_mode_name   = models.CharField(max_length=200)        # See game_mode table
    radiant_captain  = models.CharField(max_length=200)        # Account ID for Radiant captain
    dire_captain   = models.CharField(max_length=200)          # Account ID for Dire captain

class MatchPlayer(models.Model):
    account_id  = models.CharField(max_length=200)         # Unique account ID
    player_slot  = models.CharField(max_length=200)        # Player's position within the team
    hero_id   = models.CharField(max_length=200)           # Unique hero ID
    hero_name   = models.CharField(max_length=200)         # Hero's name
    item_1    = models.CharField(max_length=200)           # Item ID for item in slot # (0#5)
    item_1_name  = models.CharField(max_length=200)        # Item name for item in slot # (0#5)
    item_2  = models.CharField(max_length=200)             # Item ID for item in slot # (0#5)
    item_2_name   = models.CharField(max_length=200)       # Item name for item in slot # (0#5)
    item_3   = models.CharField(max_length=200)            # Item ID for item in slot # (0#5)
    item_3_name  = models.CharField(max_length=200)        # Item name for item in slot # (0#5)
    item_4     = models.CharField(max_length=200)          # Item ID for item in slot # (0#5)
    item_4_name   = models.CharField(max_length=200)       # Item name for item in slot # (0#5)
    item_5   = models.CharField(max_length=200)            # Item ID for item in slot # (0#5)
    item_5_name  = models.CharField(max_length=200)        # Item name for item in slot # (0#5)
    kills    = models.CharField(max_length=200)            # Number of kills by player
    deaths    = models.CharField(max_length=200)           # Number of player deaths
    assists     = models.CharField(max_length=200)         # Number of player assists
    leaver_status   = models.CharField(max_length=200)     # Connection/leaving status of player
    gold  = models.CharField(max_length=200)               # Gold held by player
    last_hits   = models.CharField(max_length=200)         # Number of last hits by player (creep score)
    denies   = models.CharField(max_length=200)            # Number of denies
    gold_per_min   = models.CharField(max_length=200)      # Average gold per minute
    xp_per_min   = models.CharField(max_length=200)        # Average XP per minute
    gold_spent  = models.CharField(max_length=200)         # Total amount of gold spent
    hero_damage  = models.CharField(max_length=200)        # Amount of hero damage dealt by player
    tower_damage  = models.CharField(max_length=200)       # Amount of tower damage dealt by player
    hero_healing   = models.CharField(max_length=200)      # Amount of healing done by player
    level  = models.CharField(max_length=200)              # Level of player's hero

class PlayerAbility(models.Model):
    ability  = models.CharField(max_length=200)        # Ability chosen
    time  = models.CharField(max_length=200)           # Time in seconds since match start when ability was upgraded
    level   = models.CharField(max_length=200)         # Level of player at time of upgrading