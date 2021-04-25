# Brett Meirhofer 2036955

def fat_burning_heart_rate(age):
    return .70 * (220 - age)

def get_age():
    age = float(input())
    if 18 <= age <= 75:
        return age
    else:
        raise ValueError("Invalid age.")


if __name__ == '__main__':
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a {:.0f} year-old: {:.1f} bpm".format(age,rate))

    except ValueError as ErrorText:
        print(ErrorText)
        print("Could not calculate heart rate info.\n")

