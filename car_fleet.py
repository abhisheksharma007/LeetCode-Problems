
def car_fleet(target, position, speed):
    res_stack = []
    for p, s in sorted([[p, s] for p, s in zip(position, speed)], ley=lambda x: x[0], reverse=True):
        res_stack.append((target-p)/s)
        if len(res_stack) >= 2 and res_stack[-1] <= res_stack[-2]:
            res_stack.pop()
    return len(res_stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(car_fleet(target, position, speed))

expected = 3
print("expected {}".format(expected))