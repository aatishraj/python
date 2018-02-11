ppl_queue = [8, 3, 1, 2, 5, 4, 7, 6]
priority = {2, 3, 5, 7}
sort_priority(ppl_queue, priority)
print(ppl_queue)

def sort_priority(people, priority):
    def serving(x):
        if x in priority:
            return (1, x)
        return (2, x)
    people.sort(key=serving)
