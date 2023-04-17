import math

def reward_function(params):
    """
    This reward function is inspired  by a couple of articles online

    poponuts reward function: https://github.com/poponuts/aws-deepracer-model
    """

    # constants
    REWARD = 1
    DIRECTION_THRESHOLD = 10.0
    
    # default reward
    reward = REWARD

    # unpack params
    distance_from_center = params["distance_from_center"]
    track_width = params["track_width"]
    waypoints = params['waypoints']
    closest_waypoints = params["closest_waypoints"]
    heading = params["heading"]

    #calculate the center of tthe center line 
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    center_variance = distance_from_center/track_width

    #calculate track direction in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)

    #direction in the difference between  the track direction and heading of the car
    direction_diff = abs(track_direction - heading)

    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    return float(reward)
