import re


def take_key(elem):
    match = re.search(r'\d+', elem)
    number = elem[match.start():match.end()]
    head = elem.split(number)[0].lower()
    return head, int(number)


def solution(files):
    files.sort(key=take_key)
    return files


if __name__ == '__main__':
    # print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "a23.JPG"]))
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    # [“img1.png”, “IMG01.GIF”, “img02.png”, “img2.JPG”, “img10.png”, “img12.png”]
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
    # [“A-10 Thunderbolt II”, “B-50 Superfortress”, “F-5 Freedom Fighter”, “F-14 Tomcat”]
