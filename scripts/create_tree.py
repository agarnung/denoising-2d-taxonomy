def parse_tree(input_lines):
    """
    Parses indented lines (using asterisks) into a nested tree structure.
    """
    tree = []
    stack = [(-1, tree)]  # (level, children)

    for line in input_lines:
        level = line.count('*') - 1  # Asterisk count determines depth
        label = line.strip('* ').strip()

        node = {"label": label, "children": []}

        # Adjust the stack to match the current level
        while stack and stack[-1][0] >= level:
            stack.pop()

        # Add node to its parent's children
        stack[-1][1].append(node)

        # Push current node to the stack
        stack.append((level, node["children"]))

    return tree


def tree_to_html(tree):
    """
    Recursively generates HTML for the tree structure, marking leaf nodes with the class 'item'.
    """
    html = ""
    for node in tree:
        if node["children"]:
            # Node with children
            html += f'<li><span class="caret">{node["label"]}</span>\n'
            html += '<ul class="nested">\n'
            html += tree_to_html(node["children"])
            html += '</ul>\n</li>\n'
        else:
            # Leaf node with 'item' class
            html += f'<li class="item">{node["label"]}</li>\n'
    return html


def generate_main_content(input_file, output_file):
    """
    Reads a structured text file, parses it into a tree, and writes the HTML for the <main> section to an output file.
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()

    tree = parse_tree(lines)

    # Build the HTML structure for the taxonomy
    html_content = '''
<ul id="taxonomy">
    <h1>Image Denoising Taxonomy</h1>
    <h3>~ A non-rigorous classification of image denoising methods ~</h3>
'''
    html_content += tree_to_html(tree)
    html_content += '''
</ul>
'''

    with open(output_file, 'w') as file:
        file.write(html_content.strip())


if __name__ == "__main__":
    input_file = 'raw_taxonomy.txt'
    output_file = 'tree.html'
    generate_main_content(input_file, output_file)
    print(f"HTML content written to {output_file}")
