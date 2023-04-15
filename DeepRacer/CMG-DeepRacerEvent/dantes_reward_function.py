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


import math


def reward_function(params):
    """
    Action space parameters are all set to default values
    This sample code is taken from an online source
    TODO: Play with different action space parameters
    TODO: analyze results
    """

    import math

    # unpack parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    direction_stearing = params['steering_angle']
    speed = params['speed']
    steps = params['steps']
    is_offtrack = params['is_offtrack']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    x = params['x']
    y = params['y']

    SPEED_THRESHOLD_1 = 1.8
    SPEED_THRESHOLD_2 = 1.3
    DIRECTION_THRESHOLD = 3.0
    # Read input variables

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    benchmark_time = 11.7
    benchmark_steps = 173
    straight_waypoints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 43, 44, 45, 46, 47, 48, 49, 50, 56, 57, 58, 59,
                          60, 61, 62, 63, 64, 71, 72, 73, 74, 75, 76, 77, 78, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 112, 113, 114, 115, 116, 117]

    # Get reward if completes the lap and more reward if it is faster than benchmark_time
    if progress == 100:
        if round(steps/15, 1) < benchmark_time:
            reward += 100*round(steps/15, 1)/benchmark_time
        else:
            reward += 100
    elif is_offtrack:
        reward -= 50

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(
        next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)

    # Penalize the reward if the difference is too large

    direction_bonus = 1
    if direction_diff > DIRECTION_THRESHOLD or not all_wheels_on_track:
        direction_bonus = 1-(direction_diff/15)
        if direction_bonus < 0 or direction_bonus > 1:
            direction_bonus = 0
        reward *= direction_bonus
    else:
        if next_point in (straight_waypoints):
            if speed >= SPEED_THRESHOLD_1:
                reward += max(speed, SPEED_THRESHOLD_1)
            else:
                reward += 1e-3
        else:
            if speed <= SPEED_THRESHOLD_2:
                reward += max(speed, SPEED_THRESHOLD_2)
            else:
                reward += 1e-3

    # Give additional reward if the car pass every 50 steps faster than expected
    if (steps % 50) == 0 and progress >= (steps / benchmark_steps) * 100:
        reward += 10.0
    # Penalize if the car cannot finish the track in less than benchmark_steps
    elif (steps % 50) == 0 and progress < (steps / benchmark_steps) * 100:
        reward -= 5.0
    return reward

    return float(reward)
