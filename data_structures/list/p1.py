# Merging Meeting Times

def merge_meeting_times(m):
    if len(m) == 0:
        return m

    m.sort(key=lambda x: x[0])
    merged_list = [(m[0])]

    for current_start_time, current_end_time in m[1:]:
        last_merged_start, last_merged_end = merged_list[-1]

        if current_start_time <= last_merged_end:
            merged_list[-1] = (last_merged_start,
                               max(current_end_time, last_merged_end))
        else:
            merged_list.append((current_start_time, current_end_time))

    return merged_list
