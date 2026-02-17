def youtube(picks):
    answer = ''
    for element in picks:
        if element == 'like':
            if answer == '' or answer == 'dislike':
                answer = element
            elif answer == element:
                answer = 'nothing'
        elif element == 'dislike':
            if answer == '' or answer == 'like':
                answer = element
            elif answer == element:
                answer = 'nothing'
    print(answer)

youtube(['dislike'])
youtube(['like','like'])
youtube(['dislike','like'])