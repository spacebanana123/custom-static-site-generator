import os

def writeHTML(path, file):  
    source = os.path.join(path, file)
    destination = os.path.join("public", os.path.splitext(os.path.relpath(source, 'pages'))[0] + ".html")
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    with open(source, 'r') as file:
        html = file.read()
        lines = html.splitlines()
        if lines[0].startswith('Extends'):
            template = lines[0].split(' ')[1]
            with open(os.path.join('templates', template) + ".html", 'r') as file:
                template = file.read()
            html = html.split("\n", 1)[1]
            html = template.replace('{{ content }}', html)
    with open(destination, 'w') as file:
        file.write(html)