#!/usr/bin/env python3

import yaml
import argparse
from datetime import datetime
import sys
from typing import Dict, List, Optional

class TaskManager:
    def __init__(self, status_file: str = '../DEVELOPMENT_STATUS.yaml'):
        self.status_file = status_file
        self.load_status()

    def load_status(self):
        with open(self.status_file, 'r') as f:
            self.status = yaml.safe_load(f)

    def save_status(self):
        with open(self.status_file, 'w') as f:
            yaml.dump(self.status, f, sort_keys=False)

    def get_next_available_task(self) -> Optional[Dict]:
        """Returns the highest priority task that's ready to be worked on."""
        available = [t for t in self.status['next_available_tasks'] 
                    if t['status'] == 'ready' and t['assigned_to'] is None]
        if not available:
            return None
        return min(available, key=lambda x: x['priority'])

    def check_dependencies(self, task_id: int) -> bool:
        """Check if all dependencies for a task are completed."""
        task = self.find_task(task_id)
        if not task:
            return False
        
        # Check direct dependencies
        for dep_id in self.get_task_dependencies(task_id):
            dep_task = self.find_task(dep_id)
            if not dep_task or dep_task['status'] != 'completed':
                return False
        return True

    def get_task_dependencies(self, task_id: int) -> List[int]:
        """Get all dependencies for a task from the dependency graph."""
        for phase in self.status['dependency_graph'].values():
            for component in phase.values():
                for task in component:
                    if task['id'] == task_id:
                        return task['dependencies']
        return []

    def find_task(self, task_id: int) -> Optional[Dict]:
        """Find a task by its ID."""
        for task in self.status['next_available_tasks']:
            if task['id'] == task_id:
                return task
        return None

    def start_task(self, task_id: int, ai_id: str):
        """Mark a task as in progress and assign it to an AI."""
        task = self.find_task(task_id)
        if not task:
            raise ValueError(f"Task {task_id} not found")
        if task['status'] != 'ready':
            raise ValueError(f"Task {task_id} is not ready to be started")
        if task['assigned_to'] is not None:
            raise ValueError(f"Task {task_id} is already assigned to {task['assigned_to']}")
        
        task['status'] = 'in_progress'
        task['assigned_to'] = ai_id
        
        # Log the activity
        if 'ai_activity_log' not in self.status:
            self.status['ai_activity_log'] = []
        
        self.status['ai_activity_log'].append({
            'timestamp': datetime.now().isoformat(),
            'ai_id': ai_id,
            'action': 'started',
            'task_id': task_id
        })
        
        self.save_status()

    def complete_task(self, task_id: int, ai_id: str, commit_hash: str):
        """Mark a task as completed."""
        task = self.find_task(task_id)
        if not task:
            raise ValueError(f"Task {task_id} not found")
        if task['assigned_to'] != ai_id:
            raise ValueError(f"Task {task_id} is not assigned to {ai_id}")
        
        task['status'] = 'completed'
        task['assigned_to'] = None
        task['completion_date'] = datetime.now().strftime('%Y-%m-%d')
        
        # Update blocked tasks
        self.update_blocked_tasks()
        
        # Log the activity
        self.status['ai_activity_log'].append({
            'timestamp': datetime.now().isoformat(),
            'ai_id': ai_id,
            'action': 'completed',
            'task_id': task_id,
            'commit_hash': commit_hash
        })
        
        self.save_status()

    def update_blocked_tasks(self):
        """Update the status of tasks that might be unblocked."""
        for task in self.status['next_available_tasks']:
            if task['status'] == 'blocked':
                if self.check_dependencies(task['id']):
                    task['status'] = 'ready'
                    task['prerequisites_met'] = True
                    task['blocked_by'] = []

def main():
    parser = argparse.ArgumentParser(description='Manage development tasks')
    parser.add_argument('action', choices=['next', 'start', 'complete', 'status'])
    parser.add_argument('--task-id', type=int, help='Task ID')
    parser.add_argument('--ai-id', help='AI Assistant ID')
    parser.add_argument('--commit-hash', help='Commit hash for completed task')
    
    args = parser.parse_args()
    
    manager = TaskManager()
    
    if args.action == 'next':
        task = manager.get_next_available_task()
        if task:
            print(yaml.dump(task))
        else:
            print("No tasks available")
            
    elif args.action == 'start':
        if not args.task_id or not args.ai_id:
            print("Error: task-id and ai-id required for start action")
            sys.exit(1)
        manager.start_task(args.task_id, args.ai_id)
        print(f"Started task {args.task_id}")
        
    elif args.action == 'complete':
        if not all([args.task_id, args.ai_id, args.commit_hash]):
            print("Error: task-id, ai-id, and commit-hash required for complete action")
            sys.exit(1)
        manager.complete_task(args.task_id, args.ai_id, args.commit_hash)
        print(f"Completed task {args.task_id}")
        
    elif args.action == 'status':
        if args.task_id:
            task = manager.find_task(args.task_id)
            if task:
                print(yaml.dump(task))
            else:
                print(f"Task {args.task_id} not found")
        else:
            print(yaml.dump(manager.status['next_available_tasks']))

if __name__ == '__main__':
    main()
