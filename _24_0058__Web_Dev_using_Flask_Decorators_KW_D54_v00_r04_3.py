import time

current_time = time.time()
print(f"\nNow in seconds is: {current_time}")  # seconds since 12:00am on Jan 1st, 1970

# write your code below 👇
def outter_function(main_function):
    def speed_calc_decorator():

        start_time_processing = time.time()
        print(f"\nStarting time for {main_function.__name__} is: {start_time_processing}")

        executes_main_function_and_stores_result = main_function()

        end_time_processing = time.time()
        print(f"Ending time for {main_function.__name__} is: {end_time_processing}")

        # calculates the time difference to get the timer for each function:
        time_duration = end_time_processing - start_time_processing
        print(f"The total execution time for {main_function.__name__} is: {time_duration} seconds")

        # accesses the final value of `i` stored in the function attribute:
        final_i_value = getattr(main_function, 'last_i', 'No value set')  # updated to use getattr for safe access
        print(f"The final value of i in {main_function.__name__} is: {final_i_value}")

        return executes_main_function_and_stores_result

        # time_difference = current_time - __name__[0]
        # print(f"__name__ = {__name__}")
        # return time_difference()
    return speed_calc_decorator

@outter_function
def fast_function():
    for i in range(1000000):
        i * i
    fast_function.last_i = i  # added to store the final value of i

@outter_function
def slow_function():
    for i in range(10000000):
        i * i
    slow_function.last_i = i  # this line was already correctly set

fast_function()
slow_function()
