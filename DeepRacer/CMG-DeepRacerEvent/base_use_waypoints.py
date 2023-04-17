def reward_function(params):
    """
    Action space parameters are all set to default values
    This sample code is taken from an online source
    TODO: Play with different action space parameters
    TODO: analyze results
    """

    # constants
    REWARD = 30

    # unpack params
    all_wheels_on_track = params["all_wheels_on_track"]
    distance_from_center = params["distance_from_center"]
    track_width = params["track_width"]
    speed = params["speed"]
    steps = params["steps"]
    progress = params["progress"]
    closest_waypoint = params["closest_waypoints"]
    is_left_of_center = params["is_left_of_center"]

    center_variance = distance_from_center/track_width

    # waypoints
    left_lane = [23, 24, 50, 51, 52, 53, 61, 62, 63,
                 64, 65, 66, 67, 68]  # Fill in the waypoints
    center_lane = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28, 35,
                   36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 54, 55, 56, 57, 58, 59, 60, 69, 70]  # Fill in the waypoints
    right_lane = [29, 30, 31, 32, 33, 34]  # Fill in the waypoints

    # speed waypoints
    fast = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 26, 27, 28, 29, 30, 31,
            32, 51, 52, 53, 54, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]  # 3
    moderate = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                45, 46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60]  # 2
    slow = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]  # 1

    # Give a very low reward by default
    reward = REWARD

    front_waypoint = closest_waypoint[1]
    if front_waypoint in left_lane and is_left_of_center:
        reward += 10
    elif front_waypoint in right_lane and not is_left_of_center:
        reward += 10
    elif front_waypoint in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10

    if front_waypoint in fast:
        if speed > 1.5:
            reward += 10
        else:
            reward -= 10
    elif front_waypoint in moderate:
        if speed > 1 and speed <= 1.5:
            reward += 10
        else:
            reward -= 10
    elif front_waypoint in slow:
        if speed <= 1:
            reward += 10
        else:
            reward -= 10

    return float(reward)
