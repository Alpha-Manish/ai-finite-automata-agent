import streamlit as st
import re

# Import or include your optimized parsing logic
def parse_input_to_regex(rule_input: str) -> str:
    cleaned = rule_input.strip().lower()
    if "start" in cleaned and "end" in cleaned:
        matches = re.findall(r"['\"]([a-zA-Z0-9]+)['\"]", cleaned)
        if len(matches) >= 2:
            return f"^{matches[0]}.*{matches[1]}$"
    match = re.search(r"['\"]([a-zA-Z0-9]+)['\"]", cleaned)
    pattern = match.group(1) if match else cleaned.split()[-1]
    if "least" in cleaned or "atleast" in cleaned:
        count = 2 if ("two" in cleaned or "2" in cleaned) else 3 if ("three" in cleaned or "3" in cleaned) else 1
        return f".*({pattern}.*){{{count},}}"
    if "start" in cleaned:
        return f"^{pattern}.*"
    elif "end" in cleaned:
        return f".*{pattern}$"
    return rule_input

# --- Streamlit UI Layout ---
st.set_page_config(page_title="AI Finite Automata Agent", page_icon="🤖")
st.title("🤖 AI Finite Automata Agent")
st.write("Convert conversational English rules into live deterministic state machines.")

st.sidebar.header("⚙️ Machine Configuration")
raw_alphabet = st.sidebar.text_input("🔤 Define Allowed Alphabet", value="012")
user_rule = st.sidebar.text_input("👉 Enter Custom Rule Logic", value="starts with '0' and ends with '2'")

# Process configuration parameters
alphabet_set = set(raw_alphabet.replace(",", "").replace(" ", "").lower())
regex_str = parse_input_to_regex(user_rule)

st.sidebar.subheader("System State Compile")
st.sidebar.code(f"Pattern: {regex_str}\nAlphabet: {sorted(list(alphabet_set))}", language="text")

# String Testing Section
st.subheader("📝 Test a String")
target_str = st.text_input("Enter a string to validate through the state machine:", value="01112")

if target_str:
    target_lower = target_str.lower()
    # 1. Check alphabet constraints
    if not all(char in alphabet_set for char in target_lower):
        invalid_chars = [c for c in target_str if c.lower() not in alphabet_set]
        st.error(f"❌ INVALID! Out of alphabet characters detected: {set(invalid_chars)}")
    else:
        # 2. Check state machine regex pattern
        try:
            compiled = re.compile(regex_str, re.IGNORECASE)
            if compiled.fullmatch(target_str):
                st.success("🎉 VALID! The string successfully matches all criteria states.")
            else:
                st.sidebar.error("❌ INVALID! String breaks the pattern criteria rule.")
        except Exception as e:
            st.error(f"Engine Configuration Error: {e}")
