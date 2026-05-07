import random

identification = [
    'Note Identification',
    'Key Signature Identification',
    'Staff Interval Identification',
    'Chord Identification',
    'Keyboard Interval Identification',
    'Keyboard Chord Identification'
]

construction = [
    'Note Construction',
    'Key Signature Construction',
    'Interval Construction',
    'Chord Construction'
]

ear_training = [
    'Interval Ear Training'
]


if __name__ == '__main__':

    exercise_pics = [1, 2]

    random.shuffle(exercise_pics)

    exercises = []

    exercises += random.sample(identification, exercise_pics[0])

    exercises += random.sample(construction, exercise_pics[1])

    random.shuffle(exercises)

    exercises += ear_training

    print(exercises)
