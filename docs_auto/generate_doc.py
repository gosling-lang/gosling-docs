# %%

import json

# help me test in ipy


def json2table(defs, obj_name, doc_name):

    if 'description' in defs and defs['description'] == 'experimental':
        return

    # with open(f'./{obj_name}.md', 'w') as f:
    with open(doc_name, 'a') as f:

        f.write(f"### {obj_name}\n")
        try:
            f.write(defs['description'] + '\n')  # add description if exist
        except Exception:
            pass
        f.write(f'**properties of {obj_name}**\n')

        f.write('| property | type | description |\n')  # head
        f.write('|----|----|-----|\n')

        # put required property at first
        property_names = [k for k in defs['properties']]
        property_names.sort(
            key=lambda x: x in defs['required'], reverse=True)

        for p in property_names:
            property_info = defs['properties'][p]
            p_type = property_info['type']
            p_const = property_info['const'] if 'const' in property_info else ''

            required_info = '**required**,' if p in defs['required'] else ''
            default_info = f'must be `"{p_const}"`, ' if p_const != '' else ''
            description = property_info['description'] if 'description' in property_info else ''

            if description == 'experimental':
                continue

            f.write(
                f"|{p}| {p_type} | {required_info + default_info + description} |\n")
        f.write('\n')


def generate_table(obj_name, json_schema, doc_name):
    assert obj_name in json_schema["definitions"], f"{obj_name} is not in gosling schema"
    defs = json_schema["definitions"][obj_name]
    json2table(defs, obj_name, doc_name)


# %%

def generate_data_md():
    with open('./gosling.schema.json') as f:
        json_schema = json.load(f)

    data_list = [f["$ref"].replace('#/definitions/', '')
                 for f in json_schema["definitions"]['DataDeep']['anyOf']]

    doc_name = './data.md'
    with open(f'./data.md', 'w') as f:
        f.write('## Data\n')

    for d in data_list:
        generate_table(d, json_schema, doc_name)


# %%
generate_data_md()
# %%
