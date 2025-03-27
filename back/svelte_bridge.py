import os
import subprocess
import json
from pathlib import Path

class SvelteKitBridge:
    def __init__(self, build_dir='build'):
        self.build_dir = build_dir
        self.server_path = os.path.join(build_dir, 'index.js')
        self.manifest_path = os.path.join(build_dir, 'server', 'manifest.json')
        self.node_process = None
        
    def start_node_server(self, port=3000):
        """Démarre le serveur Node.js pour SvelteKit en arrière-plan"""
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
        
        # Attendez un moment pour que le serveur démarre
        import time
        time.sleep(1)
        
        return self.node_process
        
    def stop_node_server(self):
        """Arrête le serveur Node.js"""
        if self.node_process:
            self.node_process.terminate()
            self.node_process = None
            
    def render_page(self, path, request_data=None):
        """
        Fait une requête au serveur SvelteKit pour obtenir le rendu d'une page
        
        :param path: Le chemin de la page à rendre (ex: '/')
        :param request_data: Données supplémentaires pour la requête (headers, etc.)
        :return: Le HTML rendu par SvelteKit
        """
        import requests
        
        if request_data is None:
            request_data = {}
            
        # Fait une requête au serveur SvelteKit local
        try:
            response = requests.get(f'http://localhost:3000{path}', headers=request_data.get('headers', {}))
            return response.text
        except requests.RequestException as e:
            return f"<p>Erreur lors du rendu SvelteKit: {str(e)}</p>"