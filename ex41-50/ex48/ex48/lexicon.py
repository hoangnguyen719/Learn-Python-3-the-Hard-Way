def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def scan(string):
    accepted_words = {'direction': ['north', 'east', 'south', 'west',
                                    'down', 'up', 'left', 'right', 'back'],
                      'verb': ['go', 'eat', 'kill', 'stop', 'hit'],
                      'stop': ['the', 'in', 'of', 'and', 'from', 'at', 'it'],
                      'noun': ['bear', 'princess', 'door', 'cabinet']}
    strings = string.split()
    result = []
    # This 1st method respects the input string's order
    for string in strings:
        if is_number(string):
            result.append(('number', float(string)))
        else:
            for key in accepted_words:
                if string.lower() in accepted_words[key]:
                    result.append((key, string.lower()))
                    break
                elif key == list(accepted_words.keys())[-1]:
                    result.append(('error', string))
                else:
                    continue
    # # This 2nd method respects the order of accepted_words's key
    # all_accepted_words = [word for key in accepted_words for word in accepted_words[key]]
    # for accepted_key in accepted_words:
    #     result.extend([(accepted_key, accepted.lower()) for accepted in strings
    #                    if accepted.lower() in accepted_words[accepted_key]])
    # numbers = [('number', int(number)) for number in strings if number.isdigit()]
    # errors = [('error', error) for error in strings 
    #           if (error.lower() not in all_accepted_words) and (not error.isdigit())]
    # result += numbers + errors
    ###################################
    return result