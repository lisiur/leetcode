import os
import re
import sys
import json
import requests

from typing import Dict


def get_title_slug(url: str) -> str:
    return url.split('/')[-2]


def get_question_data(title_slug: str) -> Dict:
    url = 'https://leetcode-cn.com/graphql'
    headers = {
        'context-type': 'application/json',
        'x-csrftoken': 'undefined',
        'origin': 'https://leetcode-cn.com',
        'referer': 'https://leetcode-cn.com/problems/add-two-numbers/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    payload = {
        "operationName": "questionData",
        "variables": json.dumps({
            "titleSlug": title_slug
        }),
        "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    __typename\n  }\n}\n"}
    r = requests.post(url, data=payload, headers=headers)
    return r.json()


def create_files(**kw):

    def write_file(path, content, show_message=True):
        colors = {
            'BLUE': '\033[94m',
            'RED': '\033[91m',
            'END': '\033[0m',
        }

        if os.path.exists(path):
            if show_message:
                print('{path} {RED}already exists!{END}'.format(path=path, **colors))
            pass
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)
                if show_message:
                    print('{path} {BLUE}created!{END}'.format(path=path, **colors))

    write_file(kw['solution_init_file_path'], kw['solution_init_file_content'], show_message=False)
    write_file(kw['init_file_path'], kw['init_file_content'], show_message=False)
    write_file(kw['md_file_path'], kw['md_file_content'])
    write_file(kw['source_file_path'], kw['source_file_content'])
    write_file(kw['test_init_file_path'], kw['test_init_file_content'], show_message=False)
    write_file(kw['test_file_path'], kw['test_file_content'])


if __name__ == '__main__':
    url = sys.argv[1]
    title_slug: str = get_title_slug(url)
    question_data = get_question_data(title_slug).get('data').get('question')

    code_snippets = question_data.get('codeSnippets')
    sample_test_case = question_data.get('sampleTestCase')
    translated_title = question_data.get('translatedTitle')
    translated_content = question_data.get('translatedContent')
    meta_data = question_data.get('metaData')

    python_template = next(x for x in code_snippets if x['lang'] == 'Python3').get('code')
    function_name: str = json.loads(meta_data).get('name')
    pascal_function_name = function_name[0].upper() + function_name[1:]
    directory_name = title_slug.replace('-', '_')

    test_template = "import unittest\nfrom solutions.{directory_name}.solution import Solution\n\n\nclass Test{pascal_function_name}(unittest.TestCase):\n\n    def test_1(self):\n        u_input = {{\n        }}\n        u_output = ()\n\n        solution = Solution()\n        u_result = solution.{function_name}(**u_input)\n        self.assertEqual(u_output, u_result)\n\n\nif __name__ == '__main__':\n    unittest.main()\n".format_map(vars())

    context = os.getcwd()
    solution_file_path = context + '/solutions'
    test_directory = context + '/tests'
    md_file_content = '<h1><a href="{url}">{translated_title}</a></h1>\n\n{translated_content}'.format_map(vars())

    source_file_content = python_template + '\n        pass\n'
    if re.search(r': List', python_template):
        source_file_content = 'from typing import List\n\n\n{source_file_content}'.format_map(vars())
    params = {

        'solution_init_file_path': solution_file_path + '/__init__.py',
        'solution_init_file_content': '\n',

        'init_file_path': solution_file_path + '/' + directory_name + '/__init__.py',
        'init_file_content': '\n',

        'source_file_path': solution_file_path + '/' + directory_name + '/solution.py',
        'source_file_content': source_file_content,

        'md_file_path': solution_file_path + '/' + directory_name + '/README.md',
        'md_file_content': md_file_content,

        'test_file_path': test_directory + '/test_' + directory_name + '.py',
        'test_file_content': test_template,

        'test_init_file_path': test_directory + '/__init__.py',
        'test_init_file_content': '\n',
    }
    create_files(**params)
