from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Папка с файлами схем
SCHEMES_FOLDER = 'schemes'

@app.route('/api/schemes')
def get_schemes():
    # Получаем список файлов в папке schemes
    files = os.listdir(SCHEMES_FOLDER)
    schemes = []
    for file in files:
        # Можно добавить проверку на тип файла
        schemes.append({
            'title': file,  # или можно извлечь название из файла
            'file': f'{SCHEMES_FOLDER}/{file}'
        })
    return jsonify(schemes)

@app.route('/schemes/<path:filename>')
def serve_scheme(filename):
    return send_from_directory(SCHEMES_FOLDER, filename)

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # для HTTPS в разработке