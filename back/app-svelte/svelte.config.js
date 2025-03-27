import adapter from '@sveltejs/adapter-node';  // Changé de adapter-auto à adapter-node
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		// Utiliser l'adaptateur node avec le dossier de sortie "build"
		adapter: adapter({
			out: 'build'
		})
	}
};

export default config;