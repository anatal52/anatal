# https://www.tocode.co.il/bundles/python/lessons/19-data-lab

# Always write all imports at the top of the file
# (it's easier to understand that way)
from collections import defaultdict
import sys

def ex19_1():
    """1. get user & password and verify """
    users_dict = {
        "apple": "red",
        "lettuce": "green",
        "lemon": "yellow",
        "orange": "orange",
    }
    user = input("User name: ")
    password = input("Password: ")

    if user in users_dict.keys() and users_dict[user] == password:
        print("Welcome Master")
    else:
        print("INTRUDER ALERT")


def ex19_2():
    """2. Calc grades avg and print higher grades """
    # No need to specify the end here (sys.argv[1:] seems nicer)
    grades_list = [float(x) for x in sys.argv[1:21]]
    # I would calculate the average in advance outside the loop,
    # as in current code you calculate the sum again and again for each check
    # i.e.
    # average = sum(grades_list) / len(grades_list)
    # higher_grades = [x for x in grades_list if x > average]
    high_grades_list = [x for x in grades_list if x > sum(grades_list) / len(grades_list)]
    print(f"These grades are higher then the average: {high_grades_list}")


def ex19_3():
    """3. Get hostnames from cmd and print ip from host file """
    hosts_dict = defaultdict(lambda: "IP Not found")
    hosts_list = [x for x in sys.argv[1:]]
    with open('hosts', 'r', encoding='UTF-8') as f:
        for line in f:
            hostname, ip = line.strip().split("=")
            hosts_dict[hostname] = ip
    for host_request in hosts_list:
        # I would use a normal dictionary and display a completely different message
        # if value is not there
        print(f"{host_request}'s IP: {hosts_dict[host_request]}")


def ex19_4():
    """4. Print anagrams from file """
    from collections import defaultdict
    anagrams_dict = defaultdict(list)
    with open('anagrams.txt', 'r', encoding='UTF-8') as f:
        file_list = f.read().splitlines()
    for word in file_list:
        anagrams_dict["".join(sorted(word))].append(word)
    for key, val in anagrams_dict.items():
        print(" ".join(map(str, val)))


ex19_1()
