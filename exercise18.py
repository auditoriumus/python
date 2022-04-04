# Создать функцию, которая вернет ближайшую к текущей странице главу.
# Если две главы одинаково близко, то выбирается та, которая находится на большей по порядку странице.

def nearest_chapter(list: list, page: int):
    chapter = ''
    for key in list:
        if chapter == '':
            chapter = key
        else:
            if abs(list[chapter] - page) > (abs(list[key] - page)):
                chapter = key
            elif abs(list[chapter] - page) == (abs(list[key] - page)):
                if list[chapter] < list[key]:
                    chapter = key

    return chapter

print(nearest_chapter({
  "Chapter 1" : 1,
  "Chapter 2" : 15,
  "Chapter 3" : 37
}, 10))

print(nearest_chapter({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200))

print(nearest_chapter({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3))