def parse_tree(input_lines):
    tree = []
    stack = [(-1, tree)]  # Stack to track hierarchy levels

    for line in input_lines:
        indent_level = line.count('*') - 1  # The number of asterisks indicates the level
        label = line.strip('* ').strip()  # Strip leading and trailing asterisks and spaces

        node = {"label": label, "children": []}
        
        while stack and stack[-1][0] >= indent_level:
            stack.pop()  # Pop elements from the stack until we find the correct parent level

        stack[-1][1].append(node)  # Add the current node to its parent's children
        stack.append((indent_level, node["children"]))  # Push the current level and node's children onto the stack

    return tree  # Return the final tree structure

def tree_to_html(tree, is_last=False):
    html = ""

    for i, node in enumerate(tree):
        # Determine if this node is the last child at its level
        is_last_child = (i == len(tree) - 1)

        if node["children"]:
            # If the node has children, use 'nested-caret' unless it's the last child
            if is_last_child:
                html += f'  <li>\n    <span class="caret">{node["label"]}</span>\n'
                html += f'    <ul class="nested">\n'  # Use 'nested' for the last child node
            else:
                html += f'  <li>\n    <span class="caret">{node["label"]}</span>\n'
                html += f'    <ul class="nested-caret">\n'  # Use 'nested-caret' for intermediate nodes
            html += tree_to_html(node["children"], is_last_child)  # Recursively generate the children
            html += f'    </ul>\n'  # Close the 'nested' or 'nested-caret' list
            html += f'  </li>\n'
        else:
            # For leaf nodes, use the 'item' class and 'nested' container
            html += f'    <li class="item">{node["label"]}</li>\n'  # Leaf nodes

    return html  # Return the generated HTML content

def fix_nested_caret_in_html(html_content):
    # Traverse the generated HTML and correct 'nested-caret' to 'nested' if the next node is an item
    html_lines = html_content.splitlines()
    corrected_html = []
    for i, line in enumerate(html_lines):
        # If the container is 'nested-caret' and the next node is 'item', replace 'nested-caret' with 'nested'
        if '<ul class="nested-caret">' in line and i + 1 < len(html_lines) and '<li class="item">' in html_lines[i + 1]:
            corrected_html.append(line.replace('nested-caret', 'nested'))
        else:
            corrected_html.append(line)
    return "\n".join(corrected_html)  # Return the corrected HTML content

def generate_html(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()  # Read the input file

    tree = parse_tree(lines)  # Parse the input lines into a tree structure
    
    # Start the HTML structure with the root of the taxonomy
    html_content = '''
        <ul id="taxonomy">
            <h1>Image Denoising Taxonomy</h1>'''
    
    # Iterate over the root nodes
    for i, node in enumerate(tree):
        if node["children"]:
            html_content += f'  <li>\n    <span class="caret">{node["label"]}</span>\n'
            html_content += f'    <ul class="nested-caret">\n'  # Use 'nested-caret' for parent nodes
            html_content += tree_to_html(node["children"], is_last=False)  # Recursively generate the children
            html_content += f'    </ul>\n'  # Close the 'nested-caret' list
            html_content += f'  </li>\n'
        else:
            html_content += f'    <li class="item">{node["label"]}</li>\n'  # Leaf node without children

    html_content += '''
        </ul>
    '''

    # Correct 'nested-caret' to 'nested' where necessary
    corrected_html_content = fix_nested_caret_in_html(html_content)

    with open(output_file, 'w') as file:
        file.write(corrected_html_content)  # Write the final HTML content to the output file

if __name__ == "__main__":
    input_file = 'raw_taxonomy.txt'  # Input file containing the taxonomy
    output_file = 'tree.html'  # Output HTML file
    generate_html(input_file, output_file)  # Generate the HTML from the input file
