import matplotlib.pyplot as plt
import numpy as np

def boring_stats(group_25_song_database, song_name, genre):
    """
        Show a scatter plot for 'Total Beats' vs 'Boringness' for the entered genre.

        Parameters
        =======================
        song_database (pd.DataFrame) : pandas DataFrame of song features
        song_name (str) : user chosen song
        song_genre (str) : user chosen genre

        No return value.
    """
    #Create a sub array based on user entered genre
    sub_genre_df = group_25_song_database.loc[group_25_song_database["genre"] == genre]
   
    #Sort data based on total beats
    sub_genre_df.sort_values("total_beats")

    #Single entry from data just the entered song
    song_values = sub_genre_df.loc[song_name][:]

    #Create scatter plot of boringness vs total beats
    plt.scatter(sub_genre_df.boringness, sub_genre_df.total_beats , s=5, c="#1db954", marker="o", label ="All Data")
    plt.scatter(song_values.boringness, song_values.total_beats, s=10, c="#cf0a2c", marker="s", label = song_name)
    plt.title("Total Beats vs Boringness", fontweight="bold", fontsize=20)
    plt.xlabel("Boringness")
    plt.ylabel("Total Beats")
    plt.legend(loc="upper left")
    plt.legend()
    plt.show()


def find_closest_target_value(boringness_arr, target_value):
    """
        From the numpy array, find the closest to the target value (that is not the same value).

        Parameters
        =======================
        boringness (numpy.ndarray) : list of boringsness statistics
        target_value (float) : user boringness value

        Returns (float) : closest value to target/user value
    """
    # absolute difference between each elements
    absolute_difference = np.abs(boringness_arr-target_value)

    #set the absolute difference to a large number
    absolute_difference[absolute_difference == 0] = np.inf
    closest_index = np.argmin(absolute_difference)
    closest_value = boringness_arr[closest_index]
    return closest_value


def suggest_song(group_25_song_database, song_name, genre):
    """
        Suggests a song based on the closeness of boringness value compared to other songs in the same genre.

        Parameters
        =======================
        song_database (pd.DataFrame) : pandas DataFrame of song features
        song_name (str) : user chosen song
        song_genre (str) : user chosen genre

        Returns (str) : song suggestion
    """
    sub_genre_df = group_25_song_database.loc[group_25_song_database["genre"] == genre]
    tmp_df = sub_genre_df.loc[:, ["boringness"]]
    boringness_arr = tmp_df["boringness"].values
    
    user_df = group_25_song_database.loc[song_name]
    user_df = user_df[user_df.genre == genre]

    closest_boringness_value = find_closest_target_value(boringness_arr, user_df.boringness.values[0])
    suggested_df = sub_genre_df[sub_genre_df.boringness == closest_boringness_value]

    song_name = suggested_df.index.get_level_values(0).to_list()
    
    if song_name:
        return song_name[0]
    else:
        return "No song suggestion found."