from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    status = request.form['status']

    template = Image.open("static/template.png").convert("RGB")
    draw = ImageDraw.Draw(template)


    name_font = ImageFont.truetype("comic.ttf", size=70)
    status_font = ImageFont.truetype("arialbd.ttf", size=50)


    # Position where you want to write (you can adjust)
    name_position = (950, 750)
    status_position = (1290, 875)

    # Draw the text
    draw.text(name_position, name, font=name_font, fill="red", anchor="mm")
    draw.text(status_position, status, font=status_font, fill="black", anchor="mm")

    # Save the final personalized certificate
    template.save(f"static/{name}_certificate.png")
    return send_file(f"static/{name}_certificate.png", as_attachment=True, download_name=f"{name}_certificate.png", mimetype='image/png')
    
    

 
if __name__ == '__main__':
    app.run(debug=True)
