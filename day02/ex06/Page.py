from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br
from elem import Elem, Text


def all1(iterable):
    for element in iterable:
        if not element:
            return False
    return True


class Page:
    def __init__(self, elem: Elem):
        self.elem = elem
        if not self.is_valid():
            raise self.elem.ValidationError()

    def is_valid(self):
        return Page.reverse(self.elem)

    @staticmethod
    def reverse(elem):
        if not isinstance(elem, (Html, Head, Body, Title, Meta,
                                 Img, Table, Th, Tr, Td, Ul, Ol,
                                 Li, H1, H2, P, Div, Span, Hr, Br, Text)):
            return False
        if isinstance(elem, Html):
            if len(elem.content) == 2 \
                    and not isinstance(elem.content[0], Head) \
                    and not isinstance(elem.content[1], Body):
                return False
            elif len(elem.content) > 2:
                return False
        if isinstance(elem, Head):
            count = 0
            for x in elem.content:
                if isinstance(x, Title):
                    count += 1
            if count > 1:
                return False
        if isinstance(elem, (Body, Head)):
            for x in elem.content:
                if not isinstance(x, (H1, H2, Div, Table, Ul, Ol, Span or Text)):
                    return False
        if isinstance(elem, (Title, H1, H2, Li, Th, Td)) and len(elem.content) > 0:
            if not isinstance(elem.content[0], Text) or len(elem.content) > 1:
                return False
        if isinstance(elem, P):
            for x in elem.content:
                if not isinstance(x, Text):
                    return False
        if isinstance(elem, Span):
            for x in elem.content:
                if not isinstance(x, (Text, P)):
                    return False
        if isinstance(elem, (Ul, Ol)):
            count = 0
            for x in elem.content:
                if isinstance(x, Li):
                    count += 1
            if count == 0:
                return False
        if isinstance(elem, Tr):
            count_th = 0
            count_td = 0
            for x in elem.content:
                if isinstance(x, Th):
                    count_th += 1
                elif isinstance(x, Td):
                    count_td += 1
            if (count_td == 0 and count_th == 0) or (count_td > 0 and count_th > 0):
                return False
        if isinstance(elem, Table):
            for x in elem.content:
                if not isinstance(x, Tr):
                    return False
        if all(Page.reverse(x) for x in elem.content if isinstance(x, Elem)):
            return True
        return False

    def write_to_file(self, name):
        with open(f'{name}' + '.html', 'w') as f:
            res = ""
            if isinstance(self.elem, Html):
                res += "<!doctype html>\n"
            f.write(res + self.__str__())

    def __str__(self) -> str:
        res = str(self.elem)
        return res


if __name__ == "__main__":
    target = Page(P(H1()))
#     page = Page(Html([Head(), Body([Span(P("Goodbuy"))])]))
#     # page = Page(Span([P(content=Text("Hello")),P()]))
#     # page = Page(Ul([P("Hello"), P(), Li()]))
#     # page = Page(Body(Span(P())))
#     # page = Page(Body(Span(H1())))
#     # test1 = Html()
#     # test2 = Html
#     # print(type(test1))
#     # print(type("ewfew"))
#     page.write_to_file("page")
    print(target)
