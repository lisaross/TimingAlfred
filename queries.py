#!/usr/bin/python
# encoding: utf-8

"""
Defines queries and execution functions for calling the Timing sqlite DB.
"""

import sqlite3
import os

DB_PATH = "Library/Application Support/info.eurocomp.Timing2/SQLite.db"

RECENT_TASKS =  "SELECT DISTINCT TaskActivity.title, Project.title, Project.id FROM TaskActivity INNER JOIN Project ON TaskActivity.projectID=Project.id WHERE TaskActivity.isDeleted=0 ORDER BY TaskActivity.endDate DESC LIMIT 10"
  
TASKS_BY_TITLE = "SELECT DISTINCT TaskActivity.title, Project.title, Project.id FROM TaskActivity INNER JOIN Project ON TaskActivity.projectID=Project.id WHERE TaskActivity.isDeleted=0 AND lower(TaskActivity.title) LIKE lower('%{0}%')"

def list_recent_tasks(workflow, log, query):
    """
    List recent tasks
    """
    sql_query = RECENT_TASKS
    return run_query(workflow, log, sql_query)
    
def search_tasks_by_title(workflow, log, query):
    """
    Searches for tasks by the title of the task.
    """
    sql_query = TASKS_BY_TITLE.format(query)
    return run_query(workflow, log, sql_query)
    
def run_query(workflow, log, sql):
    """
    Takes a SQL command, executes it, and returns the results.
    """
    home = os.path.expanduser("~")
    db_path = os.path.join(home, DB_PATH).encode("utf-8")
    log.debug(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    log.debug(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    log.debug("Found {0} results".format(len(results)))
    cursor.close()
    return results
