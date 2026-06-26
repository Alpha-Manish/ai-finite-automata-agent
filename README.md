# 🤖 AI-Powered Finite Automata Testing Agent

Welcome to the **AI Finite Automata Agent** repository! This project bridges the gap between natural language processing and formal language theory by translating human-readable validation rules into functional software state machines. 

Instead of writing complex regular expressions manually, users can define data validation rules using conversational English. The agent's processing layer compiles those rules into strict, deterministic matching patterns.

---

## 🚀 Key Features

* **Dynamic Alphabet Restrictions ($\Sigma$):** Enforces user-defined language bounds (e.g., binary `01`, lowercase `abc`, or custom sets like `dfg`).
* **Natural Language Parsing:** Automatically converts conversational phrases like *"starts with 'a'"*, *"ends with 'baby'"*, or *"contains at least two '1's"* into regular expressions.
* **Pre-Compiled Optimization:** Compiles structural state criteria instantly upon configuration to minimize CPU cycles during iterative testing.
* **Compound Logic Support:** Handles synchronized boundary checks, such as verifying that a string simultaneously starts and ends with specified characters.

---

## 🛠️ How It Works (Conceptual Layout)

The agent operates like a standard **Finite State Machine (FSM)**. It takes your input string and processes it character-by-character through a series of sequential states:

1. **Alphabet Filter:** Instantly rejects strings containing rogue characters outside your specified alphabet criteria.
2. **State Transition Evaluation:** Streams the remaining characters through a pre-compiled regular expression matcher acting as the deterministic automaton transition layer.
3. **Acceptance Verification:** Outputs a `🎉 VALID` or `❌ INVALID` response based on whether the string finishes execution in a valid accepting state.

---

## 💻 Setup & Usage

1. Open your terminal or command line and run the script:
   ```bash
   python agent.py
