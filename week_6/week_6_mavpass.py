def longest_run(numbers):
    current_run = 0
    best_value = 0
    best_run = 0
    current_value = numbers[0]
    for number in numbers:
        if current_value == number:
            current_run += 1
            if current_run > best_run:
                best_run = current_run
                best_value = current_value
        else:
            current_value = number
            current_run = 1
    print(f'({best_value}, {best_run})')

longest_run([1,1,2,2,2,3,3]) #should output (2, 3)
longest_run([5,5,5,4,4,4])
longest_run([2,1,1,1])
longest_run([9])