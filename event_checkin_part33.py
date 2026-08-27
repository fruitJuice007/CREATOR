# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: EventCheckin
class ActionRevert:
    def revert(self, action: str) -> None:
        if action == "checkin":
            for table in self.tables.values():
                for guest in list(table.guests):
                    if guest.status == "checked_in":
                        guest.status = "checked_out"
                        return
        elif action == "checkout":
            for table in self.tables.values():
                for guest in list(table.guests):
                    if guest.status == "checked_out":
                        guest.status = "checked_in"
                        return
        elif action == "add_ticket":
            for table in self.tables.values():
                for guest in list(table.guests):
                    if guest.ticket_id == action:
                        guest.ticket_id = None
                        return
        elif action == "add_list":
            for table in self.tables.values():
                for guest in list(table.guests):
                    if guest.list_id == action:
                        guest.list_id = None
                        return
        elif action == "add_status":
            for table in self.tables.values():
                for guest in list(table.guests):
                    if guest.status_id == action:
                        guest.status_id = None
                        return
        else:
            raise ValueError(f"Unknown action type: {action}")
