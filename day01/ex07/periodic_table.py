def parse_elem(line):
    equal = line.find("=")
    elem_name = line[:equal -1]
    val = line[equal + 1:-1].split(',')
    elem = [elem_name]
    for x in val:
        colon = x.find(":")
        key = x[1:colon]
        value = x[colon + 1:].strip()
        elem.append((key,value))
    return elem

def print_header(f):
    header="""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>periodic_table</title>
        <style>
            table{
              border-collapse: collapse;
              /* empty-cells: show; */
            }
            h4 {
              text-align: center;
            }
            .tdata {
                border: 1px solid black;
                padding:10px;
                width : 200px;
            }
            td {
                width : 200px;
            }
            ul {
              list-style:none;
              padding-left:0px;
            }
          </style>
    </head>
    <body>
        <table>
"""
    f.write(header)

def print_elem(f, element):
    f.write("\t\t<td class=\"tdata\">\n")
    f.write(f"\t\t\t<h4>{element[0]}</h4>\n")
    f.write(f"\t\t\t<ul><li>No {element[1][1]} </li></h4>\n")
    f.write(f"\t\t\t<li>{element[3][1]}</li>\n")
    f.write(f"\t\t\t<li>{element[4][1]}</li>\n")
    f.write(f"\t\t\t<li>{element[5][0]}</li>\n")
    f.write(f"\t\t\t<li>{element[5][1]}</li>\n")
    f.write(f"\t\t\t</ul>\n\t\t</td>\n")

def print_footer(f):
    footer = """        </table>
    </body>
</html>
"""
    f.write(footer)

def print_table(f, elements):    
    f.write("\t\t<tr>\n")
    pos = 0
    for x in elements:
        # print(x[1][1])
        if pos > int(x[1][1]):
            f.write("\t\t\t<tr>\n\t\t\t</tr>\n")
            pos = 0
        for _ in range(pos, int(x[1][1]) - 1):
            f.write("\t\t<td></td>\n")
        pos = int(x[1][1])
        print_elem(f, x)
    f.write("\t\t</tr>\n")

if __name__ == "__main__":
    with open("periodic_table.txt",'r') as f:
        elements = []
        line = f.readline()
        while line:
            elements.append(parse_elem(line))
            line = f.readline()
    with open("period_table.html", 'w') as f:
        print_header(f)
        print_table(f, elements)
        print_footer(f)



