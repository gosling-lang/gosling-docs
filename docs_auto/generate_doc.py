# %%

import json

# help me test in ipy


def obj2str(defs):
    obj_string = {}
    for k in defs['properties']:
        obj_string[k] = defs['properties'][k]['type']
    return json.dumps(obj_string)


def obj2table(defs, obj_name, doc_name):

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

            notes = []
            if p in defs['required']:
                notes.append('**required**')
            if p_const != '':
                notes.append(f'must be `"{p_const}"`')
            if 'description' in property_info:
                if property_info['description'] == 'experimental':
                    continue
                notes.append(property_info['description'])

            if p_type == 'array':
                if 'type' in property_info['items']:
                    p_type = f"array of {property_info['items']['type']}"
                    if property_info['items']['type'] == 'object':
                        notes.append(
                            f". Each object in the array follows the format {obj2str(property_info['items'])}")
            if p_type == 'object':
                notes.append(
                    f"This object follows the format {obj2str(property_info)}")

            f.write(
                f"|{p}| {p_type} | {'. '.join(notes)} |\n")
        f.write('\n')


def generate_table(obj_name, json_schema, doc_name):
    assert obj_name in json_schema["definitions"], f"{obj_name} is not in gosling schema"
    defs = json_schema["definitions"][obj_name]
    obj2table(defs, obj_name, doc_name)


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
