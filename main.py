
from bs4 import BeautifulSoup
import requests

# Optional arg: 0       => Ptint dashes standard
# Optional arg: 1       => Print dashes with newline char
def print_end_of_line(nl=0):
        if nl == 0:
                print("---------------------------------------------")
        elif nl == 1:
                print("---------------------------------------------\n")

if __name__ == "__main__":
        # Main page
        html_doc = requests.get("https://www.theodinproject.com/courses/ruby-programming")
        soup = BeautifulSoup(html_doc.text, 'html.parser')

        lesson_container_list = soup.find_all(class_='card-main course-section')
        #lesson_headings_list = soup.find_all(class_="course-section__title")

        print("\n================= Sections ==================\n")
        for i, lesson in enumerate(lesson_container_list):
                print(str(i+1) +". " +lesson.find(class_='course-section__title').text.strip())
                print_end_of_line()

        lesson_number = input("\nWhich lesson are you up to? > ")
        print("\n")
        lessons_in_section = lesson_container_list[int(lesson_number)-1].find_all(class_='section-lessons__item__link')
        lesson_heading = lesson_container_list[int(lesson_number)-1].find(class_='course-section__title').text

        print(lesson_number +". " +lesson_heading.strip())
        print_end_of_line()
        for i, lesson in enumerate(lessons_in_section):
                print(lesson.text)













