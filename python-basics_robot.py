#!/usr/bin/python3

import robot_api

go_down_program = ['DOWN']
go_up_program = ['UP']
go_right_program = ['RIGHT']
go_left_program = ['LEFT']

go_full_down = (
    go_down_program * 5 
    + go_right_program
    )
    
go_full_up = (
    go_up_program * 5 
    + go_right_program
    )

go_1st_room_program = (
    (
    go_full_down 
    + go_full_up
    ) * 2  
    + go_right_program
    )
    
go_2nd_room_program = (
    go_full_down
    + go_full_up
    + go_full_down
    + go_right_program
    )
    
go_3th_room_program = (
    (
    go_right_program
    + go_up_program
    + go_left_program
    + go_up_program
    ) * 2
    + go_right_program * 3
    )

go_4th_room_program = (
    go_full_down
    + go_right_program
    )

go_5th_room_program = (
    go_full_up
    + go_full_down
    + go_up_program * 5
    )

go_all_rooms = (
    go_1st_room_program
    + go_2nd_room_program 
    + go_3th_room_program 
    + go_4th_room_program
    + go_5th_room_program
    )

def run_robot(commands, room_map):
    command_deltas = {
        'DOWN': (1, 0),
        'LEFT': (0, -1),
        'UP': (-1, 0),
        'RIGHT': (0, 1),
    }
    current_position = robot_api.get_robot_position()
    movement_history = [current_position]
    for command in commands:  
        delta = command_deltas[command]
        new_position = (current_position[0] + delta[0], current_position[1] + delta[1])
        if is_wall(new_position, room_map):
            continue  # Из-за этой команды мы врежемся в стенку. Проигнорируем её.

        movement_history.append(new_position)
        robot_api.send_delta_to_engine(delta)
        current_position = new_position
    return movement_history

def is_wall(position, ascii_map):
    map_array = turn_ascii_map_into_array(ascii_map)
    return map_array[position[0]][position[1]] == '█'

def print_map(movement_history, room_map):
    if not movement_history:
        print(room_map)
        return
    footprint_positions = movement_history[:-1]
    robot_position = movement_history[-1]
    map_with_footprints = get_map_with_footprints(footprint_positions, room_map)
    map_with_footprints_and_robot = get_map_with_robot(robot_position, map_with_footprints)
    print(map_with_footprints_and_robot)

def get_map_with_footprints(movement_history, room_map):
    footprint_mark = '·'
    return add_symbol_to_ascii_map(ascii_map=room_map, symbol=footprint_mark, points=movement_history)

def get_map_with_robot(robot_position, room_map):
    robot_mark = '◆'
    return add_symbol_to_ascii_map(ascii_map=room_map, symbol=robot_mark, points=[robot_position])

def add_symbol_to_ascii_map(ascii_map, symbol, points):
    map_array = turn_ascii_map_into_array(ascii_map)
    for point_x, point_y in points:
        map_array[point_x][point_y] = symbol
    return turn_array_into_ascii_map(map_array)

def turn_ascii_map_into_array(ascii_map):
    return [list(map_line) for map_line in ascii_map.split('\n') if map_line.strip()]

def turn_array_into_ascii_map(map_array):
    return '\n'.join([''.join(map_line) for map_line in map_array])

def main():
    room = robot_api.get_room_map()
    movement_history = run_robot(commands=go_all_rooms, room_map=room)
    print_map(movement_history, room)

if __name__ == '__main__':
    main()
