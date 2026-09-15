from .application import JobApplication


def total_applications(applications:list[JobApplication]) -> int:
    return len(applications)



def counts_by_status(applications: list[JobApplication]) -> dict[str,int]:

    counts: dict[str,int] = {}

    for application in applications:
        status = application.status


        if status in counts:
            counts[status] += 1

        else:
            counts[status] = 1

    return counts




















