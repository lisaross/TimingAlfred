#!/usr/bin/python
# encoding: utf-8

"""
Main search script for alfred-bear workflow.
"""

import sys
import argparse
import queries
import json
from workflow import Workflow, ICON_SYNC

SINGLE_QUOTE = "'"
ESC_SINGLE_QUOTE = "''"

LOGGER = None

# Update workflow from GitHub repo
UPDATE_SETTINGS = {'github_slug': 'elony314/alfred-timing'}
SHOW_UPDATES = True


def main(workflow):
    """
    I don't use pylint 
    """
    if SHOW_UPDATES and workflow.update_available:
        workflow.add_item('A new version is available',
                          'Action this item to install the update',
                          autocomplete='workflow:update',
                          icon=ICON_SYNC)

    LOGGER.debug('Started search workflow')
    args = parse_args()

    if args.query:
        query = args.query[0]
        LOGGER.debug("Searching tasks for %s", format(query))
        execute_search_query(args)

    workflow.send_feedback()


def parse_args():
    """
    Parses out the arguments sent to the script in the Alfred workflow.
    """
    parser = argparse.ArgumentParser(description="Parse Tasks Argument")

# TODO: Add new task    
#     parser.add_argument('-n', '--new', default=False, const=True, nargs=0, type=bool, help='New task or not')
#     
#     parser.add_argument('-t', '--taskname', nargs=1, type=str, help='Name of the new task')
   
    parser.add_argument('query', type=unicode, nargs=argparse.REMAINDER, help='query string')

    LOGGER.debug(WORKFLOW.args)
    args = parser.parse_args(WORKFLOW.args)
    return args


def execute_search_query(args):
    """
    Decides what search to run based on args that were passed in and executes the search.
    """
    query = None
    if args.query[0]:
        LOGGER.debug('Searching tasks')
        query = args.query[0]
        query = query.encode('utf-8')

        if SINGLE_QUOTE in query:
            query = query.replace(SINGLE_QUOTE, ESC_SINGLE_QUOTE)
        
        task_results =  queries.search_tasks_by_title(WORKFLOW, LOGGER, query)
    
    else:
        LOGGER.debug('List recent tasks')
        task_results = queries.list_recent_tasks(WORKFLOW, LOGGER, query)
    
    if not task_results:
        WORKFLOW.add_item("No tasks found")
    else:
        for task_result in task_results:
            LOGGER.debug(task_result)
            json_arg = json.dumps({"task_name": task_result[0], "proj_name":task_result[1], "proj_id":str( task_result[2])})
            LOGGER.debug(json_arg)
            WORKFLOW.add_item(title=task_result[0], subtitle="Project: {}".format(task_result[1]), arg=json_arg, valid=True)        

if __name__ == '__main__':
    WORKFLOW = Workflow(update_settings=UPDATE_SETTINGS)
    LOGGER = WORKFLOW.logger
    sys.exit(WORKFLOW.run(main))
