import os
import datetime
# using kszlim's osrparse https://github.com/kszlim/osu-replay-parser
from osrparse import parse_replay_file

# note: not all replays in the folder are mine
# there are a bunch from downloading other players' replays and opening them

# majority of my online plays during this time was from fl and score/hit farming my mad machine map
online_plays = 0
online_plays_fl = 0
online_mad_machine_count = 0
offline_plays = 0
offline_plays_fl = 0
offline_mad_machine_count = 0
offline_cheated_plays = 0
path = os.getcwd() + "/Jun 23, 2020 - Aug 23, 2020"
mad_machine_md5 = ["33884a1e7dfb3e4936de8b8ffdab04b4", "2f4673d78e3bb726584df5817d5d8445", "47336ea4b998d419c83f5e09c6d7fd3f", "c98b3a535b490a8f6ae18becab0e2d30", "51de7c402232edc7699266760268d62a"]
for filename in os.listdir(path):
    try:
        replay = parse_replay_file(path + "/" + filename)
    except TypeError:
        print(filename)
    if replay.timestamp > datetime.datetime(2020, 6, 23):
        # during this time, I only used the name sometimes when logged in and guest when I wasn't
        # except for when I was testing cheats, where I used specific names that imply what cheat was being used
        if replay.player_name == "sometimes":
            if replay.mod_combination & 1 << 10:
                online_plays_fl += 1
            # I've never reached passed 4000 combo before
            # so it's safe to assume those are from other free combo invisible spinner maps I made
            if replay.beatmap_hash in mad_machine_md5 or replay.max_combo > 4000:
                online_mad_machine_count += 1
            online_plays += 1
        elif replay.player_name == "" or replay.player_name in ["Not relax", "Relax Mod"] or " legit" in replay.player_name:
            if replay.mod_combination & 1 << 10:
                offline_plays_fl += 1
            if replay.beatmap_hash in mad_machine_md5 or replay.max_combo > 4000:
                offline_mad_machine_count += 1
            offline_plays += 1
        elif "Timewarp" in replay.player_name or "95%" in replay.player_name or "90%" in replay.player_name or replay.player_name == "Relax":
            offline_cheated_plays += 1
            offline_plays += 1

print(f"Online plays: {online_plays}\nFL online plays: {online_plays_fl}\nMad machine (and other dumb spinner maps) online plays: {online_mad_machine_count}")
print(f"Offline plays: {offline_plays}\nFL offline plays: {offline_plays_fl}\nMad machine (and other dumb spinner maps) offline plays: {offline_mad_machine_count}")
print(f"\nOnline plays excluding FL and dumb mad machine: {online_plays - online_plays_fl - online_mad_machine_count}")
print(f"Offline plays excluding FL and dumb mad machine and cheated plays: {offline_plays - offline_plays_fl - offline_mad_machine_count - offline_cheated_plays}")
print(f"Offline cheated plays: {offline_cheated_plays}")
