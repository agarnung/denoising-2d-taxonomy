def parse_tree(input_lines):
    tree = []
    stack = [(-1, tree)]  # Stack to track hierarchy levels

    for line in input_lines:
        indent_level = line.count('*') - 1  # Número de asteriscos indica el nivel
        label = line.strip('* ').strip()

        node = {"label": label, "children": []}
        
        while stack and stack[-1][0] >= indent_level:
            stack.pop()

        stack[-1][1].append(node)
        stack.append((indent_level, node["children"]))

    return tree

def tree_to_html(tree, is_last=False):
    html = ""

    for i, node in enumerate(tree):
        # Determinar si este nodo es el último hijo en su nivel
        is_last_child = (i == len(tree) - 1)

        if node["children"]:
            # Si el nodo tiene hijos, usar nested-caret a menos que sea el último
            if is_last_child:
                html += f'  <li>\n    <span class="caret">{node["label"]}</span>\n'
                html += f'    <ul class="nested">\n'  # Usar nested para el último nodo
            else:
                html += f'  <li>\n    <span class="caret">{node["label"]}</span>\n'
                html += f'    <ul class="nested-caret">\n'  # Usar nested-caret para los nodos intermedios
            html += tree_to_html(node["children"], is_last_child)  # Recursivamente generar los hijos
            html += f'    </ul>\n'  # Finalizar nested o nested-caret
            html += f'  </li>\n'
        else:
            # Para nodos hoja, usaremos la clase item y contenedor nested
            html += f'    <li class="item">{node["label"]}</li>\n'  # Nodos hoja

    return html

def fix_nested_caret_in_html(html_content):
    # Recorre el HTML generado y corrige los nested-caret por nested si el siguiente nodo es un item
    html_lines = html_content.splitlines()
    corrected_html = []
    for i, line in enumerate(html_lines):
        # Si el contenedor es nested-caret y el siguiente nodo es item, cambiamos nested-caret por nested
        if '<ul class="nested-caret">' in line and i + 1 < len(html_lines) and '<li class="item">' in html_lines[i + 1]:
            corrected_html.append(line.replace('nested-caret', 'nested'))
        else:
            corrected_html.append(line)
    return "\n".join(corrected_html)

def generate_html(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    tree = parse_tree(lines)
    
    # Comienza la estructura HTML con la raíz de la taxonomía
    html_content = '''
        <ul id="taxonomy">
            <h1>Image Denoising Taxonomy</h1>'''
    
    # Iterar sobre los nodos de la raíz
    for i, node in enumerate(tree):
        if node["children"]:
            html_content += f'  <li>\n    <span class="caret">{node["label"]}</span>\n'
            html_content += f'    <ul class="nested-caret">\n'  # Usar nested-caret para nodos padre
            html_content += tree_to_html(node["children"], is_last=False)  # Generar recursivamente los hijos
            html_content += f'    </ul>\n'  # Finalizar nested-caret
            html_content += f'  </li>\n'
        else:
            html_content += f'    <li class="item">{node["label"]}</li>\n'

    html_content += '''
        </ul>
    '''

    # Ahora corregimos los nested-caret por nested donde sea necesario
    corrected_html_content = fix_nested_caret_in_html(html_content)

    with open(output_file, 'w') as file:
        file.write(corrected_html_content)

if __name__ == "__main__":
    input_file = 'raw_taxonomy.txt'
    output_file = 'tree.html'
    generate_html(input_file, output_file)
