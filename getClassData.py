import json
import requests


username = input("输入教务在线账号: ")
password = input("输入密码: ")


def get_response():
    url = 'https://lntu.me/education/course-table?semester=2020-%E7%A7%8B'
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    params = {'username': username, 'password': password}
    try:
        r = requests.post(url, json=params, headers=headers)
        return r.json()
    except:
        print("也不知道啥原因，再运行一次试试")
        print("大佬的服务器晚上还关机啊，好吧，不会是部署在宿舍里到 11 点断电了吧")


def write_lessons_file():
    response = get_response()
    data = response['data']
    lessonList = []
    for lesson in data:
        for sche in lesson['scheduleList']:
            endWeekNo = len(sche['weeks']) - 1
            lessonItem = {
                "ClassName": lesson['name'],
                "StartWeek": sche['weeks'][0],
                "EndWeek": sche['weeks'][endWeekNo],
                "WeekStatus": 0.0,
                "Weekday": sche['weekday'],
                "ClassTimeId": sche['index'],
                "Classroom": sche['room'].split('(')[0],
                "ClassSerial": lesson['code'],
                "Teacher": lesson['teacher']
            }
            lessonList.append(lessonItem)

    # return lessonList
    with open('conf_classInfo.json', 'w', encoding='UTF-8') as json_file:
        json_str = json.dumps(lessonList, ensure_ascii=False, indent=4)
        json_file.write(json_str)
        json_file.close()


if __name__ == '__main__':
    write_lessons_file()
