import os
import subprocess

class BebGptSuperEngine:
    def __init__(self):
        self.name = "CyberMind AI"
        self.system_prompt = (
            "You are CyberMind AI, an elite next-generation intelligence system. "
            "Personality: Highly analytical, professional, and efficient. "
            "Expertise: Agentic Coding, Cyber Security Lab Research, Web Architecture, and Digital Second Brain. "
            "You provide ultra-fast and accurate solutions in the user's preferred language (Bengali/English)."
        )

    def ask_ai(self, prompt, provider="google"):
        return f"**CyberMind AI**: Input processed through neural nodes. Response for '{prompt}' is ready."

    def execute_terminal(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=20)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Execution Error: {str(e)}"
