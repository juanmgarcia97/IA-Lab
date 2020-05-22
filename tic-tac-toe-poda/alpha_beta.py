from math import inf

def is_game_over(node):
    winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for indexes in winning_indexes:
        hit_count = 0
        chosen_symbol = node[indexes[0]]

        for index in indexes:
            if node[index] is not None and node[index] == chosen_symbol:
                hit_count = hit_count + 1

        if hit_count == 3:
            return True, chosen_symbol

    if node.count(None) == 0:
        return True, None

    return False, None

def change_element(node):
    count = 0
    for index in node:
        for i in index:
            if i == True:
                index[count] = None
            count = count + 1
        count = 0
    return node

def generate_children(node, chosen_symbol): # TODO: Create a function to generate the children states for minimax evaluation
    possible_move=list()
    copy_node = node.copy()
    node2 = node.copy()
    count_push = 0
    i = 0
    while node2.count(None) != 0:
        for index in node2:
            if node2[i] is None and count_push == 0:
                copy_node[i] = chosen_symbol
                count_push = count_push + 1
                node2[i] = True
            i = i + 1
        possible_move.append(copy_node)
        copy_node = node2.copy()
        count_push = 0
        i = 0
    return change_element(possible_move)

def alternate_symbol(symbol):
    return 'o' if symbol == 'x' else 'x'

def mini_max_ab(node, is_maximizing_player_turn, chosen_symbol, alpha, beta): # TODO: Modify this minimax in order to turn it into an alpha-beta pruning version with depth cutting
    game_result = is_game_over(node)
    map(lambda x: None if x == True else x, node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node

        return (-1, node) if is_maximizing_player_turn else (1, node)

    #children = generate_children(node, chosen_symbol)

    for child in generate_children(node, chosen_symbol):
        value = mini_max_ab(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol), alpha, beta)
        maximum = -1
        if is_maximizing_player_turn:
            maximum = max(maximum, value[0])
            alpha = max(alpha, value[0])
            if alpha >= beta:
                break
        else:
            maximum = min(maximum, value[0])
            beta = min(beta, value[0])
            if alpha >= beta:
                break
    return maximum, child
        
def mini_max(node, is_maximizing_player_turn, chosen_symbol):
    game_result = is_game_over(node)
    map(lambda x: None if x == True else x, node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node

        return (-1, node) if is_maximizing_player_turn else (1, node)

    children = generate_children(node, chosen_symbol)
    children_results = list(map(
        lambda child: [
            mini_max(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol))[0],
            child
        ],
        children
    ))
    return max(children_results, key=str) if is_maximizing_player_turn else min(children_results, key=str)