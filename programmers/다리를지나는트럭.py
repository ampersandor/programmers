from queue import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = deque([0] * bridge_length)
    cur_weight = 0
    while on_bridge:
        truck = on_bridge.popleft()
        cur_weight -= truck
        if truck_weights:
            if cur_weight + truck_weights[0] <= weight:
                cur_weight += truck_weights[0]
                on_bridge.append(truck_weights.pop(0))
            else:
                on_bridge.append(0)
        time += 1

    return time


if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))
    bridge_length = 100
    weight = 100
    truck_weights = [10]
    print(solution(bridge_length, weight, truck_weights))
    bridge_length = 100
    weight = 100
    truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    print(solution(bridge_length, weight, truck_weights))