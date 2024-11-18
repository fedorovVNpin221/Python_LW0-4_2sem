from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "lxml")

    main_headline = soup.find("h1", class_="main__title")
    headlines = soup.find("div", id="pagecontent").find_all("a")
    file = open("список_кафедр_омгту.txt", "w+", encoding='utf-8')
    file.write(main_headline.text.strip())
    file.write(':')
    file.write('\n')
    for item in headlines:
        faculty_text = item.text
        faculty_url = item.get("href")
        print(f"{faculty_text}: {faculty_url}", file=file)



# file.write("\n".join(headlines1).join("\n"))
# print(*headlines1, file=file)
# print(*main_headline1, file=file)
# file.writelines (main_headline)
# file.write("\n")
# file.writelines (headlines)