
PREPARATION_TIME = 2
expected_bake_time = 40

elapsed_bake_time = 26
layers = 3


def bake_time_remaining():
    return expected_bake_time - elapsed_bake_time


def preparation_time_in_minutes():
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes():
    return layers + elapsed_bake_time

print(bake_time_remaining())
print(preparation_time_in_minutes())
print(elapsed_time_in_minutes())
