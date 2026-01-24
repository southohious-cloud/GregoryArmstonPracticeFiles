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
            try:
                self.results.remove(value)
            except ValueError:
                print(f"[WARN] Cannot remove '{value}' — not in list.")
                return
        else:
            print(f"[WARN] Unknown action: {action}")
            return

        # Real-time update
        print(f"[UPDATE] {action}({value})")
        print(f"Current list → {self.results}\n")

        # Log the change
        self.log.append({
            "action": action,
            "value": value,
            "snapshot": self.results.copy()
        })

    def show_log(self):
        print("\n===== AUDIT LOG =====")
        for entry in self.log:
            print(entry)
        print("=====================\n")


def main():
    engine = ListTrackingEngine()

    print("Commands:")
    print("  append <value>")
    print("  extend <v1,v2,v3>")
    print("  remove <value>")
    print("  log")
    print("  quit\n")

    while True:
        action = input("Action: ").strip()

        if action == "quit":
            break

        elif action == "log":
            engine.show_log()

        elif action.startswith("append "):
            value = action.replace("append ", "", 1)
            engine.apply("append", value)

        elif action.startswith("remove "):
            value = action.replace("remove ", "", 1)
            engine.apply("remove", value)

        elif action.startswith("extend "):
            raw = action.replace("extend ", "", 1)
            values = [v.strip() for v in raw.split(",") if v.strip()]
            engine.apply("extend", values)

        else:
            print("Invalid command.\n")


main()
