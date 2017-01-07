import os
import re

for (root, dirs, files) in os.walk('old'):
    for f in files:
        article = []
        if f[-2:] == 'md':
            file_path = '{}/{}'.format(root, f)
            with open(file_path, encoding='utf-8') as rf:
                for idx, row in enumerate(rf):
                    if idx == 0:
                        title = row.replace('#', '')
                        title = re.sub('\[.+\]', '', title)
                        title = title.strip()
                    elif idx == 1:
                        if row[0] == '_':
                            category = row.replace('_', '').strip()
                    else:
                        article.append(row)
            new_file_path = '_posts/{}-{}-{}-article.md'.format(f[:4], f[5:7], f[8:10])
            with open(new_file_path, 'w', encoding='utf-8') as wf:
                wf.write('--\n')
                wf.write('layout: post\n')
                wf.write('title: {}\n'.format(title))
                wf.write('categories: {}\n'.format(category))
                wf.write('--\n')
                wf.writelines(article)
