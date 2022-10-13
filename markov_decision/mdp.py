right_prob_trans = [ [0.1, 0.1, 0, 0.8, 0, 0],
                    [0.1, 0, 0.1, 0, 0.8, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0.9, 0.1, 0],
                    [0, 0, 0, 0.1, 0.8, 0.1],
                    [0, 0, 0, 0, 0, 0]]

left_prob_trans = [ [0.9, 0.1, 0, 0, 0, 0],
                    [0.1, 0.8, 0.1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0.8, 0, 0, 0.1, 0.1, 0],
                    [0, 0.8, 0, 0.1, 0, 0.1],
                    [0, 0, 0, 0, 0, 0]]

up_prob_trans = [   [0.1, 0.8, 0, 0.1, 0, 0],
                    [0, 0.1, 0.8, 0, 0.1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0.1, 0, 0, 0.1, 0.8, 0],
                    [0, 0.1, 0, 0, 0.1, 0.8],
                    [0, 0, 0, 0, 0, 0]]

down_prob_trans = [ [0.9, 0, 0, 0.1, 0, 0],
                    [0.8, 0.1, 0, 0, 0.1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0.1, 0, 0, 0.9, 0, 0],
                    [0, 0.1, 0, 0.8, 0.1, 0],
                    [0, 0, 0, 0, 0, 0]]


reward = [-0.04, -0.04, -1, -0.04, -0.04, 1]

utility = [0, 0, 0, 0, 0, 0]

policy = ['', '', '', '', '', '']

def update(utility, right, left, up, down, reward): 
    for i in range(len(utility)):
        sum_up = 0
        sum_down = 0
        sum_right = 0
        sum_left = 0
        for j in range(len(utility)):
        # sum up       
            sum_up += up[i][j]*utility[j]
        # sum down
            sum_down += down[i][j]*utility[j]
        # sum left
            sum_left += left[i][j]*utility[j]
        # sum right
            sum_right += right[i][j]*utility[j]

        utility[i] = reward[i] + max(sum_up, sum_down, sum_left, sum_right)
    return utility

if __name__ == '__main__':
    for k in range(0,200):
        utility = update(utility, right_prob_trans, left_prob_trans, up_prob_trans, down_prob_trans, reward)
    
    print(utility)

    for i in range(len(policy)):
        sum_up = 0
        sum_down = 0
        sum_right = 0
        sum_left = 0
        for j in range(len(utility)):
        # sum up       
            sum_up += up_prob_trans[i][j]*utility[j]
        # sum down
            sum_down += down_prob_trans[i][j]*utility[j]
        # sum left
            sum_left += left_prob_trans[i][j]*utility[j]
        # sum right
            sum_right += right_prob_trans[i][j]*utility[j]
        
        movement = max(sum_up, sum_down, sum_right, sum_left)

        if i == 2:
            policy[i] = '-1'
        elif i == 5:
            policy[i] = '+1'

        elif (movement == sum_up):
            policy[i] = 'up'
        elif (movement == sum_down):
            policy[i] = 'down'
        elif (movement == sum_left):
            policy[i] = 'left'
        elif (movement == sum_right):
            policy[i] = 'right'
    
    print(policy)
