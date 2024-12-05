def validate_phone(phone, contacts):
    if not phone.isdigit() or len(phone) < 10:
        return False
    for contact in contacts:
        if contact["Phone"] == phone:
            return False
    return True
