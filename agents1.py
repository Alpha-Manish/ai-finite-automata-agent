import re

class FiniteAutomataAgent:
    def __init__(self):
        print("🤖 AI Finite Automata Agent Initialized.")

    def parse_input_to_regex(self, rule_input: str) -> str:
        """
        Optimized Parsing Layer: Maps natural language constraints 
        to efficient formal machine patterns.
        """
        cleaned = rule_input.strip().lower()
        
        # 1. Compound Rule: Starts with X and Ends with Y
        if "start" in cleaned and "end" in cleaned:
            matches = re.findall(r"['\"]([a-zA-Z0-9]+)['\"]", cleaned)
            if len(matches) >= 2:
                return f"^{matches[0]}.*{matches[1]}$"
        
        # Extract targeted token within quotes if available
        match = re.search(r"['\"]([a-zA-Z0-9]+)['\"]", cleaned)
        pattern = match.group(1) if match else cleaned.split()[-1]
        
        # 2. Counting Rules ("at least X")
        if "least" in cleaned or "atleast" in cleaned:
            count = 2 if ("two" in cleaned or "2" in cleaned) else 3 if ("three" in cleaned or "3" in cleaned) else 1
            return f".*({pattern}.*){{{count},}}"
        
        # 3. Simple Positional Rules
        if "start" in cleaned:
            return f"^{pattern}.*"
        elif "end" in cleaned:
            return f".*{pattern}$"
            
        return rule_input

    def run_interactively(self):
        """
        Optimized Master Execution Loop
        """
        while True:
            print("\n==========================================")
            print("     DEFINE SYSTEM STATE ENVIRONMENT       ")
            print("==========================================")
            print("Type 'exit' to terminate the program.")
            
            # 1. Clean and store alphabet set
            raw_alphabet = input("\n🔤 Define allowed alphabet characters (e.g., ab or 012): ").strip()
            if raw_alphabet.lower() == 'exit': break
            alphabet_set = set(raw_alphabet.replace(",", "").replace(" ", "").lower())
            
            # 2. Parse and pre-compile the rule automaton
            user_rule = input("👉 Enter custom rule logic: ").strip()
            if user_rule.lower() == 'exit': break
            
            regex_str = self.parse_input_to_regex(user_rule)
            
            try:
                # Pre-compiling here saves CPU cycles inside the string loop
                compiled_automaton = re.compile(regex_str, re.IGNORECASE)
                print(f"\n🤖 System Configured Rule Pattern: {regex_str}")
                print(f"🔤 Restricting characters to: {{{', '.join(sorted(list(alphabet_set)))}}}")
                print("------------------------------------------")
                print("Type 'new' to change your configuration environment.")
            except re.error as e:
                print(f"❌ Configuration Error: Invalid state logic generated: {e}")
                continue

            # 3. Optimized Evaluation Loop
            while True:
                target_str = input("\n📝 Enter string to validate: ").strip()
                target_lower = target_str.lower()
                
                if target_lower == 'new':
                    print("\n🔄 Resetting environment parameters...")
                    break 
                if target_lower == 'exit':
                    print("\nShutting down Agent. Goodbye! 👋")
                    return
                
                # Check alphabet constraint instantly
                if not all(char in alphabet_set for char in target_lower):
                    invalid_chars = [c for c in target_str if c.lower() not in alphabet_set]
                    print(f"Result: ❌ INVALID! Out of alphabet characters detected: {set(invalid_chars)}")
                    continue
                
                # Execute pre-compiled match verification
                if compiled_automaton.fullmatch(target_str):
                    print("Result: 🎉 VALID string matches all system criteria.")
                else:
                    print("Result: ❌ INVALID string breaks pattern layout criteria.")

if __name__ == "__main__":
    agent = FiniteAutomataAgent()
    agent.run_interactively()
