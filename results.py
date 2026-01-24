class ListTrackingEngine:
    def __init__(self, initial=None):
        self.results = initial or []
        self.log = []

    def apply(self, action, value):
        # Perform the action
        if action == "append":
            self.results.append(value)
        elif action == "extend":
            self.results.extend(value)
        elif action == "remove":
            self.results.remove(value)
        else:
            print(f"[WARN] Unknown action: {action}")
            return

        # Real-time update printout
        print(f"[UPDATE] {action}({value})")
        print(f"Current list → {self.results}\n")

        # Log the change
        self.log.append({
            "action": action,
            "value": value,
            "snapshot": self.results.copy()
        })

    def run(self, operations):
        for action, value in operations:
            self.apply(action, value)

    def show_log(self):
        print("\n===== AUDIT LOG =====")
        for entry in self.log:
            print(entry)


# -------------------------
# Example usage
# -------------------------

engine = ListTrackingEngine(["Mario", "Luigi"])

operations = [
    ("append", "Princess"),
    ("append", "Yoshi"),
    ("append", "Koopa Troopa"),
    ("append", "Toad"),
    ("extend", ["Bowser", "Donkey Kong Jr."]),
    ("remove", "Yoshi"),
    ("append", "Princess"),
    ("extend", ["Bowser", "Donkey Kong Jr."])
]

engine.run(operations)
engine.show_log()
