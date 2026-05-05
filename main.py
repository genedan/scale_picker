import random



major_scales = [
    'C Major',
    'G Major',  # 116
    'D Major',  # 104
    'A Major',  # 112
    'E Major',  # 112
    'B Major',  # 122
    'F# Major',
    'C# Major',
    'F Major',  # 104
    'Bb Major', # 104
    'Eb Major',
    'Ab Major',
    'Db Major',
    'Gb Major', # 116
    'Cb Major'
]

minor_scales = [
    'A Minor',
    'E Minor',
    'B Minor',  # 104
    'F# Minor',
    'C# Minor',  # 104
    'G# Minor',
    'D# Minor',
    'A# Minor',  # 104
    'D Minor',  # 114
    'G Minor',  # 112
    'C Minor',
    'F Minor',  # 104
    'Bb Minor',
    'Eb Minor', # 116
    'Ab Minor'  # 116
]

recent_scales = [
    ### Majors
    'G Major',
    'D Major',
    'A Major',
    'E Major',
    'F Major',
    'B Major',
    'Bb Major',
    'Gb Major',

    ### Minors
    'B Minor',
    'C# Minor',
    'A# Minor',
    'D Minor',
    'G Minor',
    'F Minor',
    'Eb Minor',
    'Ab Minor'
]

def pick_scales():

    available_majors = [x for x in major_scales if x not in recent_scales]
    available_minors = [x for x in minor_scales if (x not in recent_scales)]

    selected_majors = random.sample(available_majors, 2)
    selected_minors = random.sample(available_minors, 2)

    selected_scales = selected_majors + selected_minors

    print(selected_scales)


if __name__ == '__main__':

    pick_scales()