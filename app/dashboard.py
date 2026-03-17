from flask import Flask, render_template_string, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "data", "autosanp_logs.json")
STATES_FILE = os.path.join(BASE_DIR, "data", "policy_states.json")

# Ensure states file exists on startup
if not os.path.exists(STATES_FILE):
    initial_states = {
        "database_policy.yml": False,
        "server_policy.yml": False,

        "security_policy.yml": False
    }
    with open(STATES_FILE, 'w') as f:
        json.dump(initial_states, f)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AutoSANP Proactive Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0b0f19; color: white; padding: 20px;}
        .container { max-width: 900px; margin: auto; }
        h1 { text-align: center; color: #4ecca3; }
        
        /* Toggle Button Styles */
        .button-group { display: flex; gap: 15px; justify-content: center; margin-bottom: 30px; flex-wrap:wrap;}

        .policy-card { background: #1a1e2e; padding: 15px; border-radius:10px; text-align: center; width:180px; border:1px solid #333;}
        .policy-name { font-size: 0.9em; margin-bottom: 10px; display:block; color: #888;}
        
        button { width: 100%; padding: 10px; border: none; border-radius:5px; cursor:pointer;  font-weight:bold; transition:0.3s;}
        
        /* State Colors */
        .btn-on { background: #2ecc71; color: white; box-shadow: 0 0 10px rgba(46 , 204 , 113 , 0.4);}
        .btn-off { background: #e74c3c; color: white; opacity: 0.6; }
        button:hover { transform: scale(1.05); opacity: 1; }

        .log-entry { background: #16213e; padding: 15px; margin-bottom:12px; border-radius:8px; border-left:5px solid #4ecca3;}
        .REMEDIATED { border-left-color: #fca311; }
        .FAILED { border-left-color: #e94560; }
        .status-tag { float: right; font-size: 0.8em; padding: 2px 8px; border-radius:4px; background: #232946;}
    </style>
</head>
<body>
    <div class="container">
        <h1>AutoSANP Control Center</h1>
        
        <div class="button-group">
            {% for policy, is_active in states.items() %}
            <div class="policy-card">
                <span class="policy-name">{{ policy.replace('_', ' ').replace('.yml','').upper()}}</span>
                <form action="/toggle/{{ policy }}" method="POST">
                    <button class="{{ 'btn-on' if is_active else 'btn-off'}}">
                        {{ 'AUTOMATION: ON' if is_active else 'AUTOMATION: OFF'}}
                    </button>
                </form>
            </div>
            {% endfor %}
        </div>

        <div class="log-container">
                    <h3>Recent Activity Logs</h3>
            {% for log in logs %}
            <div class="log-entry {{ log.status }}">
                <span class="status-tag">{{ log.status }}</span>
                <strong>{{ log.timestamp }}</strong><br>
                Policy: <b style="color:#4ecca3">{{ log.policy }}</b><br>
                <em>{{ log.details }}</em>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    logs = []
    try:
        with open(LOG_FILE, 'r') as f:
            for line in f:
                logs.append(json.loads(line))
    except FileNotFoundError: pass

    with open(STATES_FILE, 'r') as f:
        states = json.load(f)

    return render_template_string(HTML_TEMPLATE, logs=reversed(logs), states= states)



@app.route('/toggle/<policy_name>', methods=['POST'])
def toggle_policy(policy_name):
    with open(STATES_FILE, 'r') as f:
        states = json.load(f)
    
    # Toggle logic
    states[policy_name] = not states.get(policy_name, False)
    
    with open(STATES_FILE, 'w') as f:
        json.dump(states, f)
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

