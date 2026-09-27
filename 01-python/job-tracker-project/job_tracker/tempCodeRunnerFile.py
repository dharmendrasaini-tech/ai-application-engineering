    print(
        f"ID: {application.unique_id}\n"
        f"Company: {application.company}\n"
        f"Role: {application.role}\n"
        f"Status: {application.status}\n"
        f"Date_applied: {application.date_applied}\n"
    )

    print("Notes - \n")
    for note in application.notes:
        print(f"{note}\n")
