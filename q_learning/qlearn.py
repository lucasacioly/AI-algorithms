import trajectories as traj

Q = [
    [],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [10, 10, 10, 10, 10, 10]
]

rewards = {
    '1':{'1':-10, '2':-1, '3':-1},
    '2':{'1':-1, '2':-10, '4':-1},
    '3':{'1':-1, '3':-10, '4':-1, '5':-1},
    '4':{'2':-1, '3':-1, '4':-10, '6':10},
    '5':{'3':-1, '5':-10, '6':10},
    '6':{'5':-1, '4':-1, '6':10}
}

alpha = 0.5
gamma = 1.0

def get_num_action(action : str) -> int :
    if (action == 'UP'):
        action = 0
    elif (action == 'DW'):
        action = 1
    elif (action == 'LF'):
        action = 2
    elif (action == 'RG'):
        action = 3
    
    return action

def update(state : int, action: str, next_state: int, rewards : dict, Q : list, alpha : float, gamma : float):
    
    print(state)    
    estimate_q = rewards[str(state)][str(next_state)] + gamma * max(Q[next_state])
    q_value = Q[state][action] + alpha*(estimate_q - Q[state][action])
    
    return q_value



if __name__ == "__main__":
    num_traj = int(input('trajectory number: '))

    trajectory : list = traj.trajs[num_traj - 1]
    
    for i in range(0, len(trajectory)):

        state = trajectory[i]['state']
        next_state = trajectory[i]['next_state']
        action = get_num_action(trajectory[i]['action'])
        
        Q[state][action] = update(state, action, next_state, rewards, Q, alpha, gamma)

    print("\n-------------------------------\n")
    for i in range(len(Q)):
        print(Q[i])

