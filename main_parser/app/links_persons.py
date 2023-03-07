'''

'''


def list_persons(
    links_cache
):
    ready_list = [None]
    ready_list_b = links_cache.lrange('links_list', 0, -1)
    for ready_links_b in ready_list_b:
        ready_links = ready_links_b.decode('utf-8')
        ready_list.append(ready_links)
    return ready_list[1:]                                   # Redis оставляет пустую ячейку под ключ