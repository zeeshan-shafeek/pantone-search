from flask import Flask, render_template, request
from pycolorname.pantone.pantonepaint import PantonePaint

app = Flask(__name__)

# Initialize the Pantone color system
pantone_colors = PantonePaint()

def get_color_info(pantone_code):
    full_key = f'PMS {pantone_code}'
    for key, value in pantone_colors.items():
        if full_key in key:
            color_rgb = value
            hex_value = '#{:02x}{:02x}{:02x}'.format(*color_rgb)
            color_name = key.split('(', 1)[1].rsplit(')', 1)[0]
            return pantone_code, color_name, hex_value
    return None, None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    color_info = None
    if request.method == 'POST':
        pantone_code = request.form.get('pantone_code')
        color_info = get_color_info(pantone_code)
    return render_template('index.html', color_info=color_info)

if __name__ == '__main__':
    app.run(debug=True)
