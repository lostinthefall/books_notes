# coding=utf-8
# 《算法图解：像漫画小说一样有趣》.pdf

###

# P19 二分查找
# 接受一个有序数组和一个元素
def binary_search(list_a, item):
    low_index = 0
    high_index = len(list_a) - 1
    while low_index <= high_index:
        mid_index = (low_index + high_index) / 2
        mid_num = list_a[mid_index]
        if mid_num == item:
            return mid_index
        if mid_num > item:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return None


# list 需要按顺序排列
list_a = [1, 2, 3, 4, 5, 6, 45, 67, 78, 89, 245]


# print binary_search(list_a, 6)


###

# P28 选择排序
def findSmallestItem(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(0, len(arr)):
        index = findSmallestItem(arr)
        newArr.append(arr.pop(index))
    return newArr


# P47
def add(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        x = arr.pop(0)
        print arr
        return x + add(arr)


# P52
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        # 挑出一个数组除第一个以外比num小的数字放到一个列表里
        # - https://developers.google.com/edu/python/sorting List Comprehensions (optional)
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


# P111
# graph 的 key 是 node name，value 是 邻近节点的 name 和 value
# graph = {}
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2
# # {'a': 6, 'b': 2}
# print(graph["start"])
#
# costs = {}
# parents = {}
#
# # 保存已经处理的 node
# processed = []


# 开销指的是从起点前往该节点需要多长时间
def dijkstraAlgorithm():
    graph = {"start": {}, "a": {}, "b": {}, "c": {}, "d": {}, "fin": {}}
    graph["start"]["a"] = 5
    graph["start"]["b"] = 2
    graph["a"]["c"] = 4
    graph["a"]["d"] = 2
    graph["b"]["a"] = 8
    graph["b"]["d"] = 7
    graph["c"]["fin"] = 3
    graph["c"]["d"] = 6
    graph["d"]["fin"] = 1

    costs = {"a": 5, "b": 2, "c": float("inf"), "d": float("inf"), "fin": float("inf")}

    processed = []

    print("xyz graph = ", graph)
    print("xyz costs = ", costs)
    print("xyz processed = ", [])

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        # 获取到达该节点所需要的开销
        cost = costs[node]
        # 获取该节点的邻近节点
        neighbor_nodes = graph[node]
        # 遍历该节点的所有邻居
        for node_name in neighbor_nodes.keys():
            # 获取一条路径上的节点的开销
            new_cost = cost + neighbor_nodes[node_name]
            # 如果新的路径比原来的更近，就在costs散列表中更新为这个更短的路径
            if new_cost < costs[node_name]:
                # 更新为更小的开销
                costs[node_name] = new_cost
        processed.append(node)
        print("xyz graph = ", graph)
        print("xyz costs = ", costs)
        print("xyz processed = ", processed)
        node = find_lowest_cost_node(costs, processed)


# 在未处理的节点中找到开销最小的节点
def find_lowest_cost_node(costs, processed):
    # init
    lowest_cost = float("inf")
    lowest_cost_node = None
    # 找出 costs 中开销最低的 node
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# P123 贪心算法
# step 1. 找到覆盖最多所需要的州的station
# step 2. 在剩下的station中，找到覆盖最多所需要的州的station
# step 3. 重复上述操作
def greedyAlgorithm():
    # 包含要覆盖的州
    states_all = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    stations = {}
    # 电台和它所覆盖的州
    stations["kone"] = {"id", "nv", "ut"}
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])
    # 存储最终选择的广播台
    final_stations = set()

    while states_all:
        best_station = None
        # 包含该广播台覆盖的所有未覆盖的州
        states_covered = set()
        # for key , value in hash_table
        for station, states_for_station in stations.items():
            # print("station = ", station, "states_for_station = ", states_for_station)

            # 计算 states_all 和 states_for_station 的交集，
            # 表示这个 station 所能够覆盖的、我想要播放节目的州。
            states_covered_sub = states_all & states_for_station
            if len(states_covered_sub) > len(states_covered):
                best_station = station
                states_covered = states_covered_sub

        states_all -= states_covered
        final_stations.add(best_station)

    print(final_stations)


if __name__ == '__main__':
    # print add([1, 2, 3, 4, 5])

    # print quickSort([2, 5, 1, 87, 33, 26])

    # dijkstraAlgorithm()

    greedyAlgorithm()
