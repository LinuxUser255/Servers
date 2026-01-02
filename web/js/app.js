// API Routes
//  "/", get(serve_html))
//  "/health", get(health))
//  "/api/echo", post(echo))
//  "/web/:filename", get(serve_static));
//  == API Helper Functions ==
const api = {
    async get(endpoint, params = {}) {
        const url = new URL(endpoint, window.location.origin);
        Object.entries(params).forEach(([k, v]) => {
            if (v !== null && v !== undefined) {
                url.searchParams.set(k, v);
            }
        });

        const response = await fetch(url);
        if (!response.ok) {
            const error = await response.json().catch(() => ({ error: 'Request failed' }));
            throw new Error(error.error || 'Request failed');
        }
        return response.json();
    },

    async post(endpoint, data = {}) {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        if (!response.ok) {
            throw new Error(result.error || 'Request failed');
        }
        return result;
    }
};

// Helper function to format JSON with syntax highlighting
function formatJSON(data) {
    const json = JSON.stringify(data, null, 2);
    return json
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"([^"]+)":/g, '<span style="color: #9cdcfe;">"$1"</span>:')
        .replace(/: "([^"]*)"/g, ': <span style="color: #ce9178;">"$1"</span>')
        .replace(/: (\d+)/g, ': <span style="color: #b5cea8;">$1</span>')
        .replace(/: (true|false|null)/g, ': <span style="color: #569cd6;">$1</span>');
}

// == Event Listeners ==
document.addEventListener('DOMContentLoaded', () => {
    const pythonButton = document.getElementById('click-me');
    const rustButton = document.getElementById('rust-button');
    const pythonContainer = document.getElementById('servers-container');
    const rustContainer = document.getElementById('rust-servers-container');

    // Click event handler for Python button
    pythonButton.addEventListener('click', async () => {
        try {
            pythonButton.disabled = true;
            pythonButton.textContent = 'Loading...';
            pythonContainer.innerHTML = '<p style="color: gray;">Loading Python server data...</p>';

            // Fetch health endpoint from Python server (port 8000)
            const response = await fetch('http://localhost:8000/health');
            const data = await response.json();

            pythonContainer.innerHTML = `
            <div style="color: #fff; padding: 20px; background: #3a3a3a; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.3);">
                <h3 style="margin-bottom: 15px;">✅ Python Server is Running</h3>
                <p style="margin-bottom: 10px;"><strong>Status:</strong> ${data.status}</p>
                <pre style="
                    background: #1e1e1e;
                    padding: 15px;
                    border-radius: 6px;
                    overflow-x: auto;
                    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                    font-size: 14px;
                    line-height: 1.5;
                    margin: 0;
                    border: 1px solid #404040;
                    text-align: left;
                    white-space: pre;
                ">${formatJSON(data)}</pre>
             </div>
             `;
        } catch (error) {
            pythonContainer.innerHTML = `
                <div style="color: #ff6b6b; padding: 20px; background: #3a3a3a; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.3);">
                    <h3>❌ Python Server Not Running</h3>
                    <p>${error.message}</p>
                    <p>Make sure the Python server is running on port 8000</p>
                </div>
            `;
        } finally {
            pythonButton.disabled = false;
            pythonButton.textContent = 'Fetch Python Servers';
        }
    });

    // Rust server button click handler
    rustButton.addEventListener('click', async () => {
        try {
            rustButton.disabled = true;
            rustButton.textContent = 'Loading...';
            rustContainer.innerHTML = '<p style="color: #fff;">Fetching Rust server data...</p>';

            // Fetch health endpoint from Rust server (port 3000)
            const data = await api.get('/health');

            rustContainer.innerHTML = `
                <div style="color: #fff; padding: 20px; background: #3a3a3a; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.3);">
                    <h3 style="margin-bottom: 15px;">✅ Rust Server is Running</h3>
                    <p style="margin-bottom: 10px;"><strong>Status:</strong> ${data.status}</p>
                    <pre style="
                        background: #1e1e1e;
                        padding: 15px;
                        border-radius: 6px;
                        overflow-x: auto;
                        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                        font-size: 14px;
                        line-height: 1.5;
                        margin: 0;
                        border: 1px solid #404040;
                        text-align: left;
                        white-space: pre;
                    ">${formatJSON(data)}</pre>
                </div>
            `;
        } catch (error) {
            rustContainer.innerHTML = `
                <div style="color: #ff6b6b; padding: 20px; background: #3a3a3a; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.3);">
                    <h3>❌ Rust Server Not Running</h3>
                    <p>${error.message}</p>
                    <p>Make sure the Rust server is running on port 3000</p>
                </div>
            `;
        } finally {
            rustButton.disabled = false;
            rustButton.textContent = 'Fetch Rust Servers';
        }
    });
});
