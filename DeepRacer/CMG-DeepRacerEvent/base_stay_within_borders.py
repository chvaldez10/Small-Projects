def reward_function(params):
    """
    Action space parameters are all set to default values
    This sample code is taken from an online source
    TODO: Play with different action space parameters
    TODO: analyze results
    """

    # unpack params
    all_wheels_on_track = params["all_wheels_on_track"]
    speed = params["speed"]
    steps = params["steps"]
    progress = params["progress"]

    # constants
    REWARD = ((progress/steps)*100) + speed**2
    MIN_REWARD = 0.01
    # Give a very low reward by default
    reward = MIN_REWARD

    if all_wheels_on_track and steps > 0:
        reward = REWARD
    else:
        reward = MIN_REWARD

    return float(reward)
