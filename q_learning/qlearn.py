import trajectories as traj
from random import choice

Q = [
    [],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [10, 10, 10, 10]
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

politica = [0, 0, 0, 0, 0, 0]

def rand_next_state(state : int):
    if (state == 1):
        return choice([1,2,3])
    elif (state == 2):
        return choice([1,2,4])
    elif (state == 3):
        return choice([1,3,4,5])
    elif (state == 4):
        return choice([2,3,4,6])
    elif (state == 5):
        return choice([3,5,6])

def rand_action():
    return choice(['UP', 'DW', 'LF', 'RG'])
    

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

def print_q(Q : list):
    print("\n-------------------------------\n")
    for i in range(1, len(Q)):
        print(Q[i])

def update_policy(Q  : list[list], policy : list):
    actions = ["UP", "DW", "LF", "RG"]
    for i in range(1, len(Q)):
        print(i)
        estado = Q[i]
        policy[i-1] = actions[estado.index(max(estado))]
    
    print(policy)

    print(f'''\nPolitica:  
{policy[4]} 1
{policy[2]} {policy[3]}
{policy[0]} {policy[1]}
        ''')

if __name__ == "__main__":

    rand = int(input('Random trajectory? '))

    if (not rand):
        num_traj = int(input('trajectory number: '))

        trajectory : list = traj.trajs[num_traj - 1]
        
        for i in range(0, len(trajectory)):

            state = trajectory[i]['state']
            next_state = trajectory[i]['next_state']
            action = get_num_action(trajectory[i]['action'])
            
            Q[state][action] = update(state, action, next_state, rewards, Q, alpha, gamma)

        print_q(Q)
        update_policy(Q, politica)

    elif (rand):
        
        state = 1 # initial state
        while state !=6 :

            next_state = rand_next_state(state)
            action = get_num_action(rand_action())
            
            Q[state][action] = update(state, action, next_state, rewards, Q, alpha, gamma)

            state = next_state
            

        print_q(Q)
        update_policy(Q, politica)