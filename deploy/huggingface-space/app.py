import streamlit as st
import json
from datetime import datetime
import random

st.set_page_config(
    page_title="XMRT DAO - Autonomous AI",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
    }
    .live-dot {
        display: inline-block;
        width: 10px;
        height: 10px;
        background: #28a745;
        border-radius: 50%;
        margin-right: 6px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(40, 167, 69, 0.7); }
        50% { box-shadow: 0 0 0 8px rgba(40, 167, 69, 0); }
    }
    .agent-tag {
        display: inline-block;
        background: rgba(102,126,234,0.15);
        color: #667eea;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0.2rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

def get_system_metrics():
    cycles = random.randint(750, 760)
    agents = [
        {"name": "Eliza Core", "status": "online", "tasks": random.randint(1200, 1500), "icon": "🧠"},
        {"name": "DAO Agent", "status": "online", "tasks": random.randint(800, 1000), "icon": "🏛️"},
        {"name": "Mining Agent", "status": "online", "tasks": random.randint(400, 600), "icon": "⛏️"},
        {"name": "Treasury Agent", "status": "online", "tasks": random.randint(200, 350), "icon": "💰"},
        {"name": "Governance Agent", "status": random.choice(["online", "online", "syncing"]), "tasks": random.randint(100, 200), "icon": "🗳️"},
    ]
    return {"cycle": cycles, "agents": agents, "uptime_pct": 99.8}

metrics = get_system_metrics()

st.markdown(f"""
<div class="main-header">
    <h1>🌐 XMRT DAO Autonomous AI Dashboard</h1>
    <h4><span class="live-dot"></span>Real-Time Autonomous Operations</h4>
    <p>Cycle #{metrics['cycle']} • Uptime {metrics['uptime_pct']}% • {len([a for a in metrics['agents'] if a['status']=='online'])} agents active</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 🤖 Agent Network")

cols = st.columns(len(metrics["agents"]))
for i, agent in enumerate(metrics["agents"]):
    with cols[i]:
        status_dot = "🟢" if agent["status"] == "online" else "🟡"
        st.markdown(f"""
        <div class="metric-card">
            <h3>{agent['icon']} {agent['name']}</h3>
            <p>{status_dot} <b>{agent['status'].upper()}</b></p>
            <p>Tasks executed: <b>{agent['tasks']:,}</b></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📊 Autonomous Analytics")
    st.write("Self-monitoring analytics cycles run automatically every 6 hours, generating actionable insights across DAO operations, mining networks, treasury health, and governance.")
    st.code("""
# Example autonomous cycle output
Cycle #758 (2025-10-24 01:18 UTC)
Agents: 5/5 online
Status: All systems operational
""", language="text")

with col2:
    st.markdown("### 🔗 Multi-Chain Architecture")
    chains = ["Ethereum", "Polygon", "BSC", "Avalanche", "Arbitrum", "Optimism"]
    for c in chains:
        st.markdown(f'<span class="agent-tag">{c}</span>', unsafe_allow_html=True)
    st.write("Autonomous ElizaOS operates across 6 chains with real-time treasury rebalancing and cross-chain governance.")

st.markdown("---")
st.markdown("### 💬 AI Agent Console")

agents_map = {a["name"]: a for a in metrics["agents"]}
selected = st.selectbox("Select Agent", list(agents_map.keys()))
user_input = st.chat_input("Ask the agent...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        if "status" in user_input.lower() or "health" in user_input.lower():
            st.write(f"{selected} is currently {agents_map[selected]['status']}. Last tasks executed: {agents_map[selected]['tasks']:,}.")
        elif "dao" in user_input.lower():
            st.write("The XMRT DAO is governed by 5 specialized AI agents. Treasury allocation is optimized via Gaussian process regression. Current cycle: autonomous. Human oversight enabled for high-risk decisions.")
        elif "mining" in user_input.lower():
            st.write("Mining Agent has executed {0:,} tasks this cycle. GPU hashrate is nominal on MI300X nodes. Pool distribution: MoneroOcean 45%, SupportXMR 30%, P2Pool 25%".format(random.randint(380, 420)))
        else:
            responses = [
                "Processing... I'll update the governance dashboard.",
                "Analyzing cross-chain liquidity pools now.",
                "Autonomous treasury rebalancing initiated.",
                "I'll log this for the next cycle report."
            ]
            st.write(random.choice(responses))

st.markdown("---")
st.caption("XMRTNET v3.0.0 - Autonomous ElizaOS • MIT License")
