from flask import Flask, request, Response, send_from_directory
from svelte_bridge import SvelteKitBridge
import atexit
import os
import re

app = Flask(__name__)

BUILD_DIR = './app-svelte/build'
STATIC_DIR = './app-svelte/static'
svelte_bridge = SvelteKitBridge(build_dir=BUILD_DIR)

node_process = svelte_bridge.start_node_server(port=3000)
atexit.register(svelte_bridge.stop_node_server)

@app.route('/videos/<path:filename>')
def serve_videos(filename):
    return send_from_directory(os.path.join(STATIC_DIR, 'videos'), filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(STATIC_DIR, 'images'), filename)

@app.route('/_app/immutable/<path:filename>')
def serve_immutable(filename):
    static_dir = os.path.join(BUILD_DIR, 'client', '_app', 'immutable')
    return send_from_directory(static_dir, filename)

@app.route('/<path:filename>')
def serve_static_files(filename):
    static_pattern = re.compile(r'\.(png|jpg|jpeg|gif|svg|ico|mp4|webm|ogg|mp3|css|js|woff|woff2|ttf|eot)$')
    
    if static_pattern.search(filename):
        return send_from_directory(STATIC_DIR, filename)
    else:
        return catch_all(filename)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('_app/') or re.search(r'\.(png|jpg|jpeg|gif|svg|ico|mp4|webm|ogg|mp3|css|js|woff|woff2|ttf|eot)$', path):
        return "Not found", 404

    request_data = {
        'headers': {key: value for key, value in request.headers.items()}
    }
    full_path = request.full_path if request.query_string else request.path
    html_content = svelte_bridge.render_page(full_path, request_data)
    
    response = Response(html_content)
    response.headers['Content-Type'] = 'text/html'
    
    return response

if __name__ == "__main__":
    app.run(debug=True)