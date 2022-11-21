def study_schedule(permanence_period, target_time):
    try:
        posStudents = 0
        pos = 0
        while pos < len(permanence_period):
            if (
                permanence_period[pos][0]
                <= target_time <= permanence_period[pos][1]
            ):
                posStudents += 1
            pos += 1
        return posStudents
    except TypeError:
        return None


# if __name__ == '__main__':
#     print(study_schedule(
# [(2, None), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5))
