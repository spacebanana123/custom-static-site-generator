import os
import markdown

def markdownProcess(path, f):
    source = os.path.join(path, f)
    destination = os.path.join("public", os.path.splitext(os.path.relpath(source, 'pages'))[0] + ".html")
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))
    with open(source, 'r') as file:
        data = file.read()
    lines = data.splitlines()
    if lines[0].startswith('Extends'):
        template = lines[0].split(' ')[1] + ".html"
        with open(os.path.join('templates', template), 'r') as file:
            template = file.read()
        html = markdown.markdown(data)
        html = html.split("\n", 1)[1]
        html = template.replace("{{ content }}", html)
    else:
        html = markdown.markdown(data)
    with open(destination, 'w') as file:
        file.write(html)