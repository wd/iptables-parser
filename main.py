import sys
import re
from jinja2 import Template

from constants import HTML_TEMPLATE


def read_iptables_file():
    tables = {}
    current_table_name = ''

    for line in sys.stdin:
        line = line.rstrip('\n')

        # *raw
        m = re.match(r'^\*(?P<table>[a-z]+)', line)
        if m:
            current_table_name = m.group('table')

            if tables.get(current_table_name, None) is None:
                tables[current_table_name] = {}

            continue

        table = tables.get(current_table_name)

        # :cali-to-host-endpoint - [0:0]
        # :OUTPUT ACCEPT [102892112:126461859873]
        m = re.match('^:(?P<chain>[^ ]+) (?P<policy>[A-Z-]+) .*', line)
        if m:
            chain = m.group('chain')
            policy = m.group('policy')

            if table.get(chain, None) is None:
                table[chain] = {
                    "policy": "",
                    "rules": [],
                }
            if policy != '-':
                table[chain]["policy"] = policy
            continue

        if line.startswith("-A"):
            # -A PREROUTING -m comment --comment "cali:6gwbT8clXdHdC1b1" -j cali-PREROUTING
            rule, *target = line.split(' -j ')
            target = target[0] if target else ''

            m = re.match('^-A (?P<chain>[^ ]+)(?P<rule>.*)', rule)

            chain = m.group('chain')
            rule = m.group('rule').lstrip(' ')

            table[chain]["rules"].append([rule, target])

            continue
    return tables

def render_html(tables):
    template = Template(HTML_TEMPLATE)
    html = template.render(
        tables=tables
    )
    print(html)


def main():
    tables = read_iptables_file()
    render_html(tables)

if __name__ == '__main__':
    main()

