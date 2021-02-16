# Client ID： 3ofWAlsw50dBueZlaryN7h
# Client Secret： J6FzkSFd5rsqULpBFH9KsbhuMkOR7akyvesRBfs5iI3
# token AmykTg1d9r45haOguoUf2FHvNGhxKm4SgTq5KTFswoa

from bs4 import BeautifulSoup
import requests
import time

def sendMessage():
    response = requests.get("http://www.j4.com.tw/james/remoip.php")
    soup = BeautifulSoup(response.text, "html.parser")

    result = soup.find('div')
    ip = str(result)
    ip = ip[47:62]
    # print(ip)
    for i in range(len(ip)-1, 1, -1):
        if (str(ip[i]) == str('<')):
            ip = ip[:i]
            break

    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)

    headers = {
        "Authorization": "Bearer " + "AmykTg1d9r45haOguoUf2FHvNGhxKm4SgTq5KTFswoa",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message": '\n' + result + '\n' + ip}

    r = requests.post("https://notify-api.line.me/api/notify",
                        headers=headers, params=params)

    print(result, r.status_code)  #200


if __name__ == '__main__':

    while True:
        sendMessage()
        time.sleep(1800)

