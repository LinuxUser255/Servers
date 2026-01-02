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

            // Show popup alert
            alert('✅ The Python Server is running on port 8000!');

            pythonContainer.innerHTML = `
            <div style="color: #fff; padding: 20px; background: #2a3f5f; border-radius: 8px;">
                <h3>✅ The Python Server is running</h3>
                <p><strong>Status:</strong> ${data.status}</p>
                <pre>${JSON.stringify(data, null, 2)}</pre>
             </div>
             `;
        } catch (error) {
            // Show error popup
            alert('❌ Python Server Not Running!\n\nMake sure the Python server is running on port 8000');

            pythonContainer.innerHTML = `
                <div style="color: #ff6b6b; padding: 20px; background: #2a3f5f; border-radius: 8px;">
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

            // Show popup alert
            alert('✅ The Rust Server is running on port 3000!');

            rustContainer.innerHTML = `
                <div style="color: #fff; padding: 20px; background: #2a3f5f; border-radius: 8px;">
                    <h3>✅ The Rust Server is running</h3>
                    <p><strong>Status:</strong> ${data.status}</p>
                    <pre>${JSON.stringify(data, null, 2)}</pre>
                </div>
            `;
        } catch (error) {
            // Show error popup
            alert('❌ Rust Server Not Running!\n\nMake sure the Rust server is running on port 3000');

            rustContainer.innerHTML = `
                <div style="color: #ff6b6b; padding: 20px; background: #2a3f5f; border-radius: 8px;">
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
