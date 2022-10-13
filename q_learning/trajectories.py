#trajectories

trajs = [ 
    [
        {'state':1, 'action': 'UP', 'next_state':2},
        {'state':2, 'action': 'DW', 'next_state':2},
        {'state':2, 'action': 'RG', 'next_state':2},
        {'state':2, 'action': 'LF', 'next_state':1},
        {'state':1, 'action': 'RG', 'next_state':3},
        {'state':3, 'action': 'LF', 'next_state':3},
        {'state':3, 'action': 'LF', 'next_state':3},
        {'state':3, 'action': 'UP', 'next_state':5},
        {'state':5, 'action': 'RG', 'next_state':6}
    ],

    [
        {'state':1, 'action': 'UP', 'next_state':3},
        {'state':3, 'action': 'UP', 'next_state':5},
        {'state':5, 'action': 'LF', 'next_state':3},
        {'state':3, 'action': 'LF', 'next_state':3},
        {'state':3, 'action': 'LF', 'next_state':5},
        {'state':5, 'action': 'RG', 'next_state':6}
    ],

    [
        {'state':1, 'action': 'DW', 'next_state':1},
        {'state':1, 'action': 'UP', 'next_state':3},
        {'state':3, 'action': 'RG', 'next_state':5},
        {'state':5, 'action': 'UP', 'next_state':5},
        {'state':5, 'action': 'DW', 'next_state':5},
        {'state':5, 'action': 'LF', 'next_state':5},
        {'state':5, 'action': 'DW', 'next_state':3},
        {'state':3, 'action': 'UP', 'next_state':5},
        {'state':5, 'action': 'RG', 'next_state':5},
        {'state':5, 'action': 'RG', 'next_state':6}
    ],

    [
        {'state':1, 'action': 'UP', 'next_state':3},
        {'state':3, 'action': 'RG', 'next_state':4},
        {'state':4, 'action': 'UP', 'next_state':6}
    ],

    [
        {'state':1, 'action': 'LF', 'next_state':1},
        {'state':1, 'action': 'UP', 'next_state':1},
        {'state':1, 'action': 'UP', 'next_state':3},
        {'state':3, 'action': 'UP', 'next_state':5},
        {'state':5, 'action': 'LF', 'next_state':5},
        {'state':5, 'action': 'DW', 'next_state':3},
        {'state':3, 'action': 'UP', 'next_state':5},
        {'state':5, 'action': 'UP', 'next_state':5},
        {'state':5, 'action': 'UP', 'next_state':5},
        {'state':5, 'action': 'DW', 'next_state':3},
        {'state':3, 'action': 'UP', 'next_state':3},
        {'state':3, 'action': 'LF', 'next_state':3},
        {'state':3, 'action': 'RG', 'next_state':4},
        {'state':4, 'action': 'UP', 'next_state':6}
    ]
]