""" 
    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
    "x": float,                            # agent"s x-coordinate in meters
    "y": float,                            # agent"s y-coordinate in meters
    "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent"s current position of (x, y).
    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    "distance_from_center": float,         # distance in meters from the track center 
    "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
    "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,                      # agent"s yaw in degrees
    "objects_distance": [float, ],         # list of the objects" distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [float, ],          # list of the objects" headings in degrees between -180 and 180.
    "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements" objects are left of the center (True) or not (False).
    "objects_location": [(float, float),], # list of object locations [(x,y), ...].
    "objects_speed": [float, ],            # list of the objects" speeds in meters per second.
    "progress": float,                     # percentage of track completed
    "speed": float,                        # agent"s speed in meters per second (m/s)
    "steering_angle": float,               # agent"s steering angle in degrees
    "steps": int,                          # number steps completed
    "track_length": float,                 # track length in meters.
    "track_width": float,                  # width of the track
    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center
"""


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
