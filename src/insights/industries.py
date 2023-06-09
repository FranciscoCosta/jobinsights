from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:

    data = read(path)
    job_industries = set()

    for job in data:
        if job["industry"] != "":
            job_industries.add(job["industry"])
    return job_industries
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:

    filtered_industry = [job for job in jobs if job["industry"] == industry]
    return filtered_industry
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
