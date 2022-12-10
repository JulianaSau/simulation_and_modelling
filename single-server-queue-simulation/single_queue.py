#!/usr/bin/python3

# library imports
import math
import random

# constant definitions
QUEUE_LIMIT = 100  # Limit on queue length
BUSY = 1  # Mnemonic for server's being busy
IDLE = 0  # and idle

# variable declarations and initialisation
next_event_type = num_custs_delayed = num_delays_required = num_events = num_in_queue = server_status = 0
area_num_in_queue = area_server_status = mean_interarrival = mean_service = simulation_time = time_last_event = total_of_delays = 0.0
time_next_event = [0] * 3  # initialise event list array of size 3
# initialise time_arrival array of size of queue_limit+1
time_arrival = [0] * (QUEUE_LIMIT + 1)


# Initialization function
def initialize():
    # Initialize the simulation clock, state variables and statistical counters * /
    global simulation_time, server_status, num_in_queue, time_last_event, num_custs_delayed, total_of_delays,\
        area_num_in_queue, area_server_status
    simulation_time = 0.0

    # Initialize the server status to idle
    server_status = IDLE

    # Time for the first arrival, time_next_event[1] is determined by adding an exponential random variate with
    # mean mean_interarrival, namely, expon(mean_interarrival) to the simulation clock.
    # Though sim_time at this point is zero, we are using it to show the general form of a statement
    # to determine the time of a future event.
    time_next_event[1] = simulation_time + expon(mean_interarrival)

    # Initialize event list. Since no customers are present at sim_time=0, the departure
    # (service completion) event is eliminated from consideration.
    # i.e set to to 10e + 30 guaranteeing that the first event will be an arrival
    time_next_event[2] = 1.0 * 10**30


def timing():
    
    ''' A timing function is used to compare time_next_event[1], time_next_event[2] ..., time_next_event[num_events].
    # This means that we are comparing the timing for these consequent events for instance the time for the arrival,
    # followed by a departure followed by an arrival and so of depending on the occurrence of the events.
    # Incase of ties, the lowest-numbered event type is choosen. Then the simualation is advanced to the time of occurrence
    # of the chosen event type, and stored in this varible, min_time_next_event '''

    # Some function global variables.
    global simulation_time, next_event_type, num_events

    main_time_next_event = 1.0 * 10**29
    next_event_type = 0

    # This for loop determines the event type of the next event to occur.
    for i in range(num_events):
        # If the time_next_event at position [i+1] is less that the 
        # main_time_next event then the main_time_next_event
        # is assigned that value.
        if (time_next_event[i+1] < main_time_next_event):
            main_time_next_event = time_next_event[i+1]
            next_event_type = i+1

    # This if statement check to see if the the event list is empty. 
    # If it is the we stop the simulation clock.
    if (next_event_type == 0):
        output_file.write(
            "\nEvent list is empty at time {0}".format(simulation_time))
        exit(1)

    # If the event list is not empty, then we advance the simulation clock.
    # The simulation clock is advanced to the time of occurrence of the 
    # chosen event type.
    simulation_time = main_time_next_event


def update_time_avg_stats():
    # Update area accumulator for time-average statistics.
    # This function is invoked just before processing each event (of any type) and updates the areas under 
    # the two functions needed for the continous-time statistics.
    # This is not an event routine.

    global time_last_event, simulation_time, area_num_in_queue, area_server_status, num_in_queue, server_status
    time_since_last_event = 0.0

    # Defining some global variables.
    time_since_last_event = simulation_time - time_last_event
    time_last_event = simulation_time
    # Updating the area under number-in-queue function.
    area_num_in_queue += num_in_queue * time_since_last_event
    # Updating area under server_status indicator function.area_server_status += server_status * time_since_last_event

    area_server_status += server_status * time_since_last_event


def arrive():
    # global variable initialisation
    global server_status, num_in_queue, total_of_delays, num_custs_delayed, simulation_time, mean_interarrival, time_next_event, QUEUE_LIMIT, time_arrival, mean_service
    # Initializing the a float variable, delay to zero
    delay = 0.0
    # Scheduling the next arrival.
    time_next_event[1] = simulation_time + expon(mean_interarrival)

    # Check if the server is busy
    if (server_status == BUSY):
        # increment the number of people in queue
        num_in_queue += 1
        # if there is an overflow in the queue, stop the simulation
        if (num_in_queue > QUEUE_LIMIT):
            output_file.write("\nOverflow of the array time_interval at")
            output_file.write("time {0}".format(simulation_time))
            exit(2)
            
        # There is still room in the queue, so store the time of arrival of the
        # arriving customer at the (new) end of time_arrival.
        time_arrival[num_in_queue] = simulation_time
    else:
        # Server is idle, so arriving customer has a delay of zero.
        # (The following two statements are for program clarity and
        # do not affect the results of the simulation.)
        delay = 0.0
        total_of_delays += delay
        # increment number of customers delayed and make the server busy
        num_custs_delayed += 1
        server_status = BUSY
        
        # schedule a departure (service completion)
        time_next_event[2] = simulation_time + expon(mean_service)


def depart():
    # variable declarations
    global total_of_delays, num_custs_delayed, num_in_queue, server_status, time_next_event, simulation_time, time_arrival, mean_service
    delay = 0.0

    # Checking to see if the queue is empty.
    if (num_in_queue == 0):
        # If the queue is empty we make the server IDLE and eliminate 
        # the departure(service completion) event from consideration.
        server_status = IDLE
        # We then set the departure time (next event so high such that an 
        # arrival is quarenteed first). Logically speaking we cannot have 
        # a depature if the queue is empty if we assume that the server 
        # is also not busy.
        time_next_event[2] = 1.0 * 10**30
    else:
        # if queuw isnt empty, decrement number of customers in the queue.
        num_in_queue -= 1
        # Compute the delay of the customer who is beginning service and update the total delay accumulator.
        # This is done by taking the time a person waits before joining the queue and the time they came.
        delay = simulation_time - time_arrival[1]
        total_of_delays += delay
        # Increment the number of customers delayed and schedule departure.
        num_custs_delayed += 1
        
        time_next_event[2] = simulation_time + expon(mean_service)
        # Move each customer in queue(if any) up one place, this is because a customer have just left therefore the people
        # in queue have reduced.
        for i in range(num_in_queue):
            time_arrival[i+1] = time_arrival[i + 2]


# report generator function.
def report():
    # global variable declarations
    global total_of_delays, num_custs_delayed, simulation_time, area_num_in_queue, area_server_status

    # Compute and write estimates of desired measures of perfomance.
    output_file.write("\nAverage delay in queue  {0} minutes\n\n".format(
        total_of_delays/num_custs_delayed))
    output_file.write("Average no in queue  {0}\n\n".format(
        area_num_in_queue/simulation_time))
    output_file.write("Server Utilization  {0}\n\n".format(
        area_server_status/simulation_time))
    output_file.write("Time Simulation ended  {0}".format(simulation_time))

# exponential variate generation function
def expon(mean):
    # Return an exponential random variate with mean "mean".
    # We use the random.random() to generate the random numbers.
    rand = random.random()
    return -(float(mean)) * math.log(rand)


if __name__ == '__main__':
    # open input and output files in read and write mode respectively
    input_file = open("infile.txt", "r")
    output_file = open("outfile.txt", "r+")

    # Specify the number of events for the timing function.
    num_events = 2
    # Reading input parameters.
    input_parameters = input_file.readline().split()

    # The three parameters in the infile.txt file i.e, 1.0,0.5,1000.
    mean_interarrival = input_parameters[0]
    mean_service = input_parameters[1]
    num_delays_required = input_parameters[2]

    # Write report heading and input parameters.
    output_file.write("Single-server queueing system\n\n")
    output_file.write(
        "Mean interarrival time {0} \n\n".format(mean_interarrival))
    output_file.write("Mean service time {0} \n\n".format(mean_service))
    output_file.write("No of Cutomers {0} \n".format(num_delays_required))

    # Initialize the simulation.
    initialize()

    # Run the simulation while more delays are still needed.
    # We continously loop until the 1000 stoppage rule given is met.
    while (num_custs_delayed < int(num_delays_required)):
        # Determine the next event
        timing()
        # Update time_average statistical accumulators.
        update_time_avg_stats()
        # Invoke the appropriate event functions
        if (next_event_type == 1):
            arrive()
        elif (next_event_type == 2):
            depart()
     # Invoke the report generator and end the simulation.
    report()
    # Return file pointer back to beginning of file
    output_file.seek(0)

    # Output information from file to screen
    print(output_file.read())
    input_file.close()
    output_file.close()
