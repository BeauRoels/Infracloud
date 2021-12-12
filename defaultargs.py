def ask_yes(prompt, retries = 3, reminder= 'please try again'):
    while True:
        yes = input(prompt)
        if yes in ('y', 'yes', 'ye'):
            return True
            if yes in ('n'):
                return False
                retries = retries-1
                if retries <0:
                    raise ValueError('invalid')
                    print(reminder)