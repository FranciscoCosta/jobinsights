from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:

    data = read(path)
    salary_all = set()
    for job in data:
        if job["max_salary"].isdigit():
            salary_all.add(int(job["max_salary"]))
    max_value = max(salary_all)
    return max_value
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:

    data = read(path)
    salary_all = set()
    for job in data:
        if job["min_salary"].isdigit():
            salary_all.add(int(job["min_salary"]))
    min_value = min(salary_all)
    return min_value
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    try:
        max = job["max_salary"]
        min = job["min_salary"]
        if int(max) < int(min):
            raise ValueError

        return int(min) <= int(salary) <= int(max)

    except KeyError:
        raise ValueError

    except TypeError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    list_jobs_range = []
    for job in jobs:
        try:
            result = matches_salary_range(job, salary)
            if result:
                list_jobs_range.append(job)
        except ValueError:
            print("Values not valid")
    return list_jobs_range
