from flask import Flask, request, Response, send_from_directory
import atexit
import os
import re
import subprocess

class SvelteKitBridge:
    def __init__(self, build_dir='build'):
        self.build_dir = build_dir
        self.server_path = os.path.join(build_dir, 'index.js')
        self.manifest_path = os.path.join(build_dir, 'server', 'manifest.json')
        self.node_process = None
        
    def start_node_server(self, port=3000):
        env = os.environ.copy()
        env['PORT'] = str(port)
        
        if not os.path.exists(self.server_path):
            raise FileNotFoundError(f"Le fichier server {self.server_path} n'existe pas. Assurez-vous de build SvelteKit d'abord.")
            
        self.node_process = subprocess.Popen(
            ['node', self.server_path],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        import time
        time.sleep(1)
        
        return self.node_process
        
    def stop_node_server(self):
        if self.node_process:
            self.node_process.terminate()
            self.node_process = None
            
    def render_page(self, path, request_data=None):
        import requests
        
        if request_data is None:
            request_data = {}
        try:
            response = requests.get(f'http://localhost:3000{path}', headers=request_data.get('headers', {}))
            return response.text
        except requests.RequestException as e:
            return f"<p>Erreur lors du rendu SvelteKit: {str(e)}</p>"

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
