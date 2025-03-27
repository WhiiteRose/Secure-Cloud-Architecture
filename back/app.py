from flask import Flask, request, Response
from svelte_bridge import SvelteKitBridge
import atexit

app = Flask(__name__)

svelte_bridge = SvelteKitBridge(build_dir='./app-svelte/build')

node_process = svelte_bridge.start_node_server(port=3000)

atexit.register(svelte_bridge.stop_node_server)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
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