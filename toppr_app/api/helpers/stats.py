import pandas as pd
import json

def main_stats(input_data):
    """Function for calculating the battle statistics for the whole record.
    :param input_data: Supply the records as a dictionary."""

    data_frame = pd.DataFrame(input_data)

    no_of_battles_by_year = json.loads(data_frame['year'].value_counts().to_json())
    most_attacker = json.loads(data_frame['attacker_king'].value_counts().to_json())
    most_attacked = json.loads(data_frame['defender_king'].value_counts().to_json())
    battle_types = json.loads(data_frame['battle_type'].value_counts().to_json())
    attacker_outcome = json.loads(data_frame['attacker_outcome'].value_counts().to_json())
    major_events = json.loads((data_frame['major_capture'] + \
                        data_frame['major_death']).value_counts().to_json())
    attacker_size = json.loads(data_frame['attacker_size'].describe()[['mean', 'max', 'min']].to_json())
    defender_size = json.loads(data_frame['defender_size'].describe()[['mean', 'max', 'min']].to_json())
    major_region = json.loads(data_frame['region'].value_counts().to_json())

    stats_dict = {}
    stats_dict['no_of_battles_by_year'] = no_of_battles_by_year
    stats_dict['attacker_kings_freq'] = most_attacker
    stats_dict['defender_kings_freq'] = most_attacked
    stats_dict['battle_types'] = battle_types
    stats_dict['attack_size'] = attacker_size
    stats_dict['defender_size'] = defender_size
    stats_dict['major_region'] = major_region
    stats_dict['major_events'] = major_events
    stats_dict['attacker_outcome'] = attacker_outcome

    return stats_dict


def most_active_fn(input_data):
    """Function for calculating the most active statistics.
    :param input_data: Supply the records as a dictionary."""

    data_frame = pd.DataFrame(input_data)
    most_attacker = json.loads(data_frame['attacker_king'].value_counts().to_json())
    most_attacked = json.loads(data_frame['defender_king'].value_counts().to_json())
    major_region = json.loads(data_frame['region'].value_counts().to_json())

    most_active = {}
    most_active['attacker_king'] = max(most_attacker.keys(), \
                                        key=(lambda key: most_attacker[key]))
    most_active['defender_king'] = max(most_attacked.keys(), \
                                        key=(lambda key: most_attacked[key]))
    most_active['region'] = max(major_region.keys(), \
                                        key=(lambda key: major_region[key]))

    return most_active


def largest_army(input_data):
    """Function for calculating the largest army statistics
    :param input_data: Supply the records as a dictionary."""

    data_frame = pd.DataFrame(input_data)

    attacker_size = json.loads(data_frame['attacker_size'].describe()[['mean', 'max', 'min']].to_json())
    defender_size = json.loads(data_frame['defender_size'].describe()[['mean', 'max', 'min']].to_json())

    large_army = {}
    large_army['attacker'] = attacker_size['max']
    large_army['defender'] = defender_size['max']

    return large_army


def year(input_data):
    """Function for calculating the yearly battle distribution.
    :param input_data: Supply the records as a dictionary."""

    data_frame = pd.DataFrame(input_data)

    no_of_battles_by_year = json.loads(data_frame['year'].value_counts().to_json())
    year_list = []
    for key, value in no_of_battles_by_year.items():
        year_list.append({"year":key, "value":value})

    return year_list
