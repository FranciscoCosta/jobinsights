from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path, "r") as file:
        array_of_jobs = csv.DictReader(file)
        return list(array_of_jobs)

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:

    data = read(path)
    job_types = set()

    for job in data:
        job_types.add(job["job_type"])
    return job_types

    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


# print(read("data/jobs.csv"))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:

    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]
    return filtered_jobs

    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
