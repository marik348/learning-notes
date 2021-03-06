# Using Generating function + Euler's Pentagonal theorem
def pentagonal_number(k):
    return int(k * (3 * k-1) / 2)


def compute_partitions(x):
    partitions = [1]

    for n in range(1, x+1):
        partitions.append(0)

        for k in range(1, n+1):
            coeff = (-1)**(k + 1)

            for t in [pentagonal_number(k), pentagonal_number(-k)]:
                if (n-t) >= 0:
                    partitions[n] = partitions[n] + coeff*partitions[n-t]

    return partitions


print(compute_partitions(100)[-1] - 1)