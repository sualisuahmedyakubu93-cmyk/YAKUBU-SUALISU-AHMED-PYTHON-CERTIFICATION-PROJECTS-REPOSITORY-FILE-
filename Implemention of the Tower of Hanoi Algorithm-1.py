def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = []

    def record_state():
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move(num_disks, source, auxiliary, target):
        if num_disks == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()
        else:
            move(num_disks - 1, source, target, auxiliary)

            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()

            move(num_disks - 1, auxiliary, source, target)

    record_state()
    move(n, 0, 1, 2)

    return "\n".join(states)