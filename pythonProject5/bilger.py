class HTMLBuilder:
    def __init__(self):
        self.__body = ""
    def __add_element(self, name: str, content: str = "", pair: bool = True, **params):
        element = "<" + name
        option = [f'{key}="{value}"' for key, value in params.items()]
        if option:
            element += " " + " ".join(option)
        if pair:
            element += f">{content}</{name}>"
        else:
            element += ">"
        return element
    def set_title(self, title: str):
        self.__title = title
    def add_paragraph(self, text: str):
        self.__body += self.__add_element("p", text, True) + "\n \t\t\t"
    def add_link(self, href: str, text: str):
        self.__body += self.__add_element("a", text, True, href=href) + "\n \t\t\t"
    def add_div(self, text: str):
        self.__body += self.__add_element("div", text, True) + "\n \t\t\t"
    def add_h(self, text: str):
        self.__body += self.__add_element("h1", text, True) + "\n \t\t\t"
    def add_img(self, URL: str):
        self.__body += self.__add_element("img", "", False, src=URL) + "\n \t\t\t"
    def add_list(self, array: list):
        self.__body += self.__add_element("ol", "", False) + "\n \t\t\t\t"
        for i in range(len(array)):
            self.__body += self.__add_element("li", array[i], True) + "\n\t\t\t\t"
        self.__body += f"</ol>"
    def change_text(self, text: str):
        self.__body += self.__add_element("b", text, True) + "\n \t\t\t"
    def get_body(self) -> str:
        return self.__body
    def render(self):
        return f"""
    <html>
        <head>
            {self.__add_element("title",self.__title, True)}
        </head>
        <body>
            {self.__body}
            </body>
    </html>
    """


html = HTMLBuilder()
html.set_title("Привет, лучший человек")
html.add_paragraph("123")
html.add_link("https://nfuunit.ru/", "ссылка")
html.add_div("2001")
html.add_h("Заголовок")
html.add_img("https://nfuunit.ru/")
html.change_text("Как дела")
html.add_list(["мяу", "2001"])
print(html.render())