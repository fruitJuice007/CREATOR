# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: EventCheckin
def delete_records(prompt, delete_fn, confirm_fn, message_fn, ok_fn, no_fn):
    print(prompt)
    user_input = input().strip()
    if user_input.lower() in ("y", "yes"):
        print(message_fn())
        if confirm_fn():
            deleted = delete_fn()
            print(ok_fn(deleted))
    else:
        print(no_fn())
