import os
import shutil
import WriteMarkdown
import WriteHTML

if not os.path.exists('public'):
    os.mkdir('public')
else:
    shutil.rmtree('public')
    os.mkdir('public')

if not os.path.exists('public/css'):
    os.mkdir('public/css')

if not os.path.exists('public/js'):
    os.mkdir('public/js')

if not os.path.exists('public/img'):
    os.mkdir('public/img')

for path, dirs, files in os.walk('pages'):
    for file in files:
        if file.endswith('.md'):
            WriteMarkdown.markdownProcess(path, file)
            continue
        if file.endswith('.css'):
            shutil.copy(os.path.join(path, file), os.path.join('public/', os.path.relpath(path, 'pages')))
            continue
        if file.endswith('.js'):
            shutil.copy(os.path.join(path, file), os.path.join('public/', os.path.relpath(path, 'pages')))
            continue
        if file.endswith('.png'):
            shutil.copy(os.path.join(path, file), os.path.join('public/', os.path.relpath(path, 'pages')))
            continue
        if file.endswith('.jpg'):
            shutil.copy(os.path.join(path, file), os.path.join('public/', os.path.relpath(path, 'pages')))
            continue
        if file.endswith('.html'):
            WriteHTML.writeHTML(path, file)
            continue
        if file.endswith('.ico'):
            shutil.copy(os.path.join(path, file), os.path.join('public', os.path.relpath(path, 'pages')))
            continue