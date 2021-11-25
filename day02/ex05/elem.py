#!/usr/bin/python3


class Text(str):
    def __str__(self):
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    class ValidationError(Exception):
        def __init__(self):
            super().__init__("Element not correct")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.attr = self.__make_attr()
        self.content = []
        if content is not None:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        if self.tag_type == 'double':
            result = f"<{self.tag}{self.attr}>{self.__make_content()}</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{self.attr}>{self.__make_content()}"
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += str(elem) + '\n'
        result = "  ".join(result.splitlines(keepends=True))  # ['\n', '  <div></div>\n']
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    # text = Elem()
    text = Elem('html', content=[
        Elem('head', content=Elem(
            'title', content=Text('"Hello ground!"'))),
        Elem('body', content=[Elem('h1', content=Text('"Oh no, not again!"')),
                              Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')])])
    # text = Elem(content=Elem(content=Elem(content=Elem())))
    # text = Elem(content=[Text('foo'), Text('bar'), Elem()])
    # text = Elem('div', {}, None, 'double')
    # text = Elem(tag='body', attr={}, content=Elem(),
    #             tag_type='double')
    print(text)
